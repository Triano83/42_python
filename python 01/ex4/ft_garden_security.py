class SecurePlant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        
        print(f"=== Garden Security System ===")
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    # Getters
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    # Setters 
    def set_height(self, value):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print(f"Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, value):
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print(f"Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def display_status(self):
        print(f"Current plant: {self.name} ({self.__height}cm, {self.__age} days)")
def main()->None:
    my_plant = SecurePlant("Rose",25,30)
    print()
    my_plant.set_height(-5)
    print()
    my_plant.display_status()
if __name__ == "__main__":
    main()