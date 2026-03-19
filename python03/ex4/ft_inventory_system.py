import sys


def ft_inventory_system() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py "
              "item:count item:count ...")
        return

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        name, count = arg.split(":")
        inventory[name] = int(count)

    print("=== Inventory System Analysis ===")
    total_units: int = sum(inventory.values())
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for name, count in inventory.items():
        percent = (count / total_units) * 100
        print(f"{name}: {count} units ({percent:.1f}%)")

    print("\n=== Inventory statistics ===")
    most_name: str = ""
    most_count: int = -1
    for name, count in inventory.items():
        if count >= most_count:
            most_count = count
            most_name = name
    print(f"Most abundant: {most_name} ({most_count} units)")
    least_name: str = ""
    least_count: int = most_count
    for name, count in inventory.items():
        if count <= least_count:
            least_count = count
            least_name = name
    print(f"Least abundant: {least_name} ({least_count}"
          f"{' unit' if least_count == 1 else ' units'})\n")

    print("=== Item Categories ===")
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}

    for name, count in inventory.items():
        if count >= 5:
            moderate[name] = count
        else:
            scarce[name] = count

    categories: dict[str, dict[str, int]] = {}
    categories.update({"Moderate": moderate})
    categories.update({"Scarce": scarce})

    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")
    print("\n=== Management Suggestions ===")
    restock_list: list[str] = []
    for name, count in inventory.items():
        if count <= 1:
            restock_list.append(name)

    suggestions: str = ", ".join(restock_list)
    print(f"Restock needed: {suggestions}")

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ", ".join(inventory.keys())
    values_str = ", ".join([str(v) for v in inventory.values()])

    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    ft_inventory_system()
