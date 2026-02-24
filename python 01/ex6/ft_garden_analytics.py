class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_report_line(self):
        return f"- {self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_report_line(self):
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def get_report_line(self):
        return f"{super().get_report_line()}, Prize points: {self.points}"

class GardenManager:
    total_gardens = 0  # Atributo de clase

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.growth_tracked = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.growth_tracked += 1

    # --- Helper Anidado (Nested Component) ---
    class GardenStats:
        @staticmethod
        def calculate_score(plants):
            # Lógica para calcular un score basado en altura y puntos
            score = 0
            for p in plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.points * 10
            return score

        @staticmethod
        def count_types(plants):
            regular = flowering = prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower): prize += 1
                elif isinstance(p, FloweringPlant): flowering += 1
                else: regular += 1
            return regular, flowering, prize

    # --- Tipos de Métodos Requeridos ---

    @classmethod
    def create_garden_network(cls):
        # Método que trabaja sobre el tipo del manager (la clase)
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_height(height):
        # Utilidad que no necesita datos de la instancia
        return height >= 0

    def generate_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(p.get_report_line())
        
        reg, flow, prz = self.GardenStats.count_types(self.plants)
        print(f"Plants added: {len(self.plants)}, Total growth: {self.growth_tracked}cm")
        print(f"Plant types: {reg} regular, {flow} flowering, {prz} prize flowers")

# --- Ejecución del Demo ---

if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    # Crear jardín de Alice
    alice_garden = GardenManager("Alice")
    
    # Añadir plantas de la cadena de herencia
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    
    print()
    alice_garden.help_plants_grow()
    print()
    
    # Generar reporte
    alice_garden.generate_report()
    
    # Validaciones y Estadísticas
    print(f"Height validation test: {GardenManager.validate_height(100)}")
    
    # Segundo jardín para las estadísticas globales
    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Pine", 92))
    
    score_a = alice_garden.GardenStats.calculate_score(alice_garden.plants)
    score_b = bob_garden.GardenStats.calculate_score(bob_garden.plants)
    
    print(f"Garden scores - Alice: {score_a}, Bob: {score_b}")
    print(GardenManager.create_garden_network())