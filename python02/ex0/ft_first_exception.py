def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None
        return temp
    except ValueError as e:
        print(f"Error: '{temp_str}' is not a valid number {e}\n")
        return None


def test_temperature_input():
    temp_list = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for temp in temp_list:
        print(f"Testing temperature: {temp}")
        temp_int = check_temperature(temp)
        if temp_int is not None and temp_int >= 0 and temp_int <= 40:
            print(f"Temperature {temp_int}°C is perfect for plants!\n")
    print("All test completed - program dind`t crash!!")


if __name__ == "__main__":
    test_temperature_input()
