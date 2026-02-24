class Plant:
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age = age
    def display_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    def grow_up(self,days):
        self.height = self.height + (1 * days)
    def age_up(self,days):
        self.age = self.age + (1 * days)
        
def main():
    plants = [Plant("Rose",25,30),Plant("Sunflower",80,45),Plant("Cactus",15,120)]
    days = 7
    
    for plant in plants:
        print("=== Day 1 ===")
        plant.display_info()
        star_height = plant.height
        print(f"=== Day {days} ===")
        plant.age_up(days)
        plant.grow_up(days)
        plant.display_info()
        print(f"Growth this week: +{plant.height-star_height}cm")
if __name__ == "__main__":
    main()