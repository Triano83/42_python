def ft_archive_creation() -> None:
    file_name: str = "new_discovery.txt"

    print(" === CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        print(f"Initializing new storage unit: {file_name}")
        archive = open(file_name, "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        entry1: str = "[ENTRY 001] New quantum algorithm discovered\n"
        entry2: str = "[ENTRY 002] Efficiency increased by 347%\n"
        entry3: str = "[ENTRY 003] Archived by Data Archivist trainee\n"

        archive.write(entry1)
        archive.write(entry2)
        archive.write(entry3)

        print(entry1, end="")
        print(entry2, end="")
        print(entry3, end="")

        archive.close()

        print("\nData inscription complete.", end=" ")
        print("Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except PermissionError:
        print("ERROR: Security protocols deny write access to this sector.")
    except OSError:
        print("ERROR: System anomaly during archive creation.")


if __name__ == "__main__":
    ft_archive_creation()
