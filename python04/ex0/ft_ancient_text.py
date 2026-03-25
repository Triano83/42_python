def recover_data() -> None:
    file_name: str = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        vault = open(file_name, "r")
        print(f"Accesing Storage Vault: {file_name}")
        print("Connection established...")
        vault_text = vault.read()
        print("RECOVERED DATA:")
        print(f"{vault_text}\n")
        vault.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_data()
