def garden_operations():
    try:
        print("Testing ValueError...")
        number = int("abc")
        print(f"{number}")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        division = 10 / 0
        print(f"{division}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        archive = open("test.txt")
        print(f"{archive}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        errorDict = {"Rose": 1, "SunFlower": 2}
        print(f"{errorDict['Missing']}")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types():
    print(" === Garden Error Types Demo ===\n")
    garden_operations()

    try:
        print("Testing multiple errors together...")
        int("esto_no_es_un_numero")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error, but program continues!: {e}\n")
    print("All error types tested succesfully!")


if __name__ == "__main__":
    test_error_types()
