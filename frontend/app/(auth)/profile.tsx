import { View, Text, Button, StyleSheet, ActivityIndicator } from "react-native";
import { router } from "expo-router";
import { useAuth } from "../../context/AuthContext";

export default function Profile() {
  const { user, logout, isLoading } = useAuth();

  async function handleLogout() {
    await logout();
    router.replace("/(auth)/login");
  }

  if (isLoading || !user) {
    return (
      <View style={styles.container}>
        <ActivityIndicator />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Mi perfil</Text>
      <Text style={styles.label}>Nombre: {user.name}</Text>
      <Text style={styles.label}>Email: {user.email}</Text>

      <View style={{ marginTop: 24 }}>
        <Button title="Cerrar sesión" onPress={handleLogout} color="red" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", padding: 24 },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 24, textAlign: "center" },
  label: { fontSize: 16, marginBottom: 8 },
});