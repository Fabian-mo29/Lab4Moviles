import { createContext, useContext, useEffect, useState, PropsWithChildren } from "react";
import { api, getToken, setToken, clearToken } from "../api/client";

type User = {
  id: string;
  email: string;
  name?: string;
};

type AuthContextType = {
  user: User | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (data: { name: string; email: string; password: string }) => Promise<void>;
  logout: () => Promise<void>;
  refreshProfile: () => Promise<void>;
};

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: PropsWithChildren) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  async function refreshProfile() {
    try {
      const profile = await api.getProfile();
      setUser(profile);
    } catch {
      setUser(null);
      await clearToken();
    }
  }

  useEffect(() => {
    (async () => {
      const token = await getToken();
      if (token) {
        await refreshProfile();
      }
      setIsLoading(false);
    })();
  }, []);

  async function login(email: string, password: string) {
    const data = await api.login({ email, password });
    await setToken(data.access_token);
    await refreshProfile();
  }

  async function register(data: { name: string; email: string; password: string }) {
    await api.register(data);
    await login(data.email, data.password);
  }

  async function logout() {
    await clearToken();
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, isLoading, login, register, logout, refreshProfile }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth debe usarse dentro de AuthProvider");
  return ctx;
}