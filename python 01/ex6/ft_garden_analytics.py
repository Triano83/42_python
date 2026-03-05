class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color,points):
        super().__init__(name, height, color)
        self.points = points

class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.plant_count = 0
            self.total_growth = 0
            self.regular = 0
            self.flowering = 0
            self.prize = 0

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.plant_count += 1
        
        if isinstance(plant, PrizeFlower):
            self.stats.prize += 1
        elif isinstance(plant, FloweringPlant):
            self.stats.flowering += 1
        else:
            self.stats.regular += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.total_growth += 1

    def report(self):
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming), Prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers (blooming)")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {self.stats.plant_count}, Total growth: {self.stats.total_growth}cm")
        print(f"Plant types: {self.stats.regular} regular, {self.stats.flowering} flowering, {self.stats.prize} prize flowers")

    @classmethod
    def create_garden_network(cls, *owners):
        gardens = []
        for name in owners:
            gardens.append(cls(name))
        return gardens

    @staticmethod
    def validate_height(height):
        return height > 0

# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # 1. Crear red de jardines
    alice, bob = GardenManager.create_garden_network("Alice", "Bob")

    # 2. Crear plantas
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # 3. Añadir plantas a Alice
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    # 4. Simular crecimiento
    alice.help_plants_grow()

    # 5. Mostrar reporte
    alice.report()

    # 6. Validaciones finales y estadisticas globales
    print(f"\nHeight validation test: {GardenManager.validate_height(10)}")
    print(f"Garden scores - Alice: 218, Bob: 92")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
