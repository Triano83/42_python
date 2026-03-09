class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self):
        self.plantNames = []

    def add_plant(self, name):
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plantNames.append(name)
        print(f"Added {name} successfully!")

    def water_plants(self):
        print("Opening watering system")
        try:
            for name in self.plantNames:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name, water, sun):
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        elif water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")

        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management():
    print("=== Garden Management System ===\n")
    gm = GardenManager()
    print("Adding plants to garden...")
    for plant in ["tomato", "lettuce", ""]:
        try:
            gm.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    gm.water_plants()
    print("\nChecking plant health...")
    try:
        gm.check_health("tomato", 5, 8)
    except (PlantError, WaterError) as e:
        print(f"Error checking tomato: {e}")
    try:
        gm.check_health("lettuce", 15, 8)
    except (PlantError, WaterError) as e:
        print(f"Error checking lettuce: {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
