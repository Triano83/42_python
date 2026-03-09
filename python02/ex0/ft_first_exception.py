def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input() -> None:
    temp_list: list[str] = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")

    for temp in temp_list:
        print(f"Testing temperature: {temp}")
        temp_int = check_temperature(temp)
        if temp_int is not None:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")

    print("All tests completed - program didn't crash!!")


if __name__ == "__main__":
    test_temperature_input()
