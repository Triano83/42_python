class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def simular_problema(tipo: str) -> None:
    if tipo == "planta":
        raise PlantError("The tomato plant is wilting!")
    elif tipo == "agua":
        raise WaterError("Not enough water in the tank!")


def test_ejercicio() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        simular_problema("planta")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        simular_problema("agua")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for t in ["planta", "agua"]:
        try:
            simular_problema(t)
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_ejercicio()
