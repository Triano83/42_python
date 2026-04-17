class Film:
    def __init__(self, name, director, year, cast):
        # a. Atributos de la clase
        self.name = str(name)
        self.director = str(director)
        self.year = int(year)
        self.cast = list(cast)

    # b. Modificación de la visualización del objeto
    def __str__(self):
        return f"{self.name} ({self.director}), {self.year}"

    # c. Comprobar si el director actúa en la película
    def is_director_in_cast(self):
        # i. Devolvemos True si el director está en la lista cast
        return self.director in self.cast

    # d. Obtener miembros del reparto comunes con otra película
    def match_cast(self, other_film):
        # i. Lista vacía para el resultado
        common_actors = []
        
        # ii. Bucle sobre el reparto de la película actual
        for actor in self.cast:
            # iii. Comprobar si el actor está en la otra película
            if actor in other_film.cast:
                common_actors.append(actor)
        
        # iv. Devolver la lista
        return common_actors

    # e. Añadir un nuevo miembro al reparto
    def add_member_in_cast(self, new_member):
        # i. Comprobar si ya existe
        if new_member not in self.cast:
            # ii. Si no está, lo añadimos
            self.cast.append(new_member)
        else:
            # Si ya está, imprimimos el aviso
            print(f"Member {new_member} is already in the cast")

# --- Pruebas de los objetos ---

def main():
    # Creamos los objetos de ejemplo
    jurassic = Film("Jurassic Park", "Steven Spielberg", 1993, 
                    ["Sam Neill", "Laura Dern", "Jeff Goldblum", "Richard Attenborough", "Bob Peck"])
    
    titanic = Film("Titanic", "James Cameron", 1998, 
                   ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"])

    # Probamos el punto b (visualización)
    print(jurassic)

    # Probamos el punto c (director en el reparto)
    # Agreguemos a Spielberg al reparto de Jurassic Park para probar
    print(f"¿Está Spielberg en el reparto? {jurassic.is_director_in_cast()}") # False

    # Probamos el punto e (añadir miembro)
    jurassic.add_member_in_cast("Samuel L. Jackson")
    jurassic.add_member_in_cast("Jeff Goldblum") # Debería decir que ya está

    # Probamos el punto d (match_cast)
    # Creamos otra película para ver si hay actores repetidos
    mundo_perdido = Film("The Lost World", "Steven Spielberg", 1997, 
                         ["Jeff Goldblum", "Julianne Moore", "Vince Vaughn"])
    
    actores_comunes = jurassic.match_cast(mundo_perdido)
    print(f"Actores en ambas películas: {actores_comunes}")

if __name__ == "__main__":
    main()