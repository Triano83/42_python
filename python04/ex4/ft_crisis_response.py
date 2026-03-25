def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    archives: list[str] = ["lost_archive.txt", "classified_vault.txt",
                           "standard_archive.txt"]

    for archive_name in archives:
        if archive_name == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{archive_name}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{archive_name}'...")

        try:
            with open(archive_name, "r") as file:
                content: str = file.read()
                print(f"SUCCESS: Archive recovered - \"{content}\"")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
        finally:
            if archive_name == "lost_archive.txt":
                print("STATUS: Crisis handled, system stable")
            elif archive_name == "classified_vault.txt":
                print("STATUS: Crisis handled, security maintained")
            else:
                print("STATUS: Normal operations resumed")
            print()
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
