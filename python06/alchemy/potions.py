import elements as root_elements
import alchemy.elements as alchemy_elements


def healing_potion() -> str:
    return (f"Healing potion brewed with '{alchemy_elements.create_earth()}'"
            f"and '{alchemy_elements.create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed "
            f"with {root_elements.create_fire()}"
            f"and '{root_elements.create_water()}'")
