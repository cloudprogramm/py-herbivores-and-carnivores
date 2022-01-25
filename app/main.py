class Animal:
    alive = []

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False

        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):

    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore):
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50

            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
