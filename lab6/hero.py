import random
from ability import Ability
from armor import Armor


class Hero:

    def __init__(self, name, starting_health=100):

        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = []
        self.armors = []

    def add_ability(self, ability):

        self.abilities.append(ability)

    def add_armor(self, armor):

        self.armors.append(armor)

    def attack(self):

        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):

        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):

        damage -= self.defend()

        if damage > 0:
            self.current_health -= damage

    def is_alive(self):

        return self.current_health > 0

    def battle(self, opponent):

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.is_alive() and opponent.is_alive():

            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

        if self.is_alive():
            print(self.name + " won!")

        elif opponent.is_alive():
            print(opponent.name + " won!")

        else:
            print("Draw")


if __name__ == "__main__":

    my_hero = Hero("Spider-Man", 150)

    my_hero.add_ability(Ability("Web Shooter", 25))
    my_hero.add_ability(Ability("Spider Sense", 10))

    my_hero.add_armor(Armor("Spider Suit", 15))

    opponent = Hero("Captain America", 200)

    opponent.add_ability(Ability("Shield Throw", 30))
    opponent.add_armor(Armor("Vibranium Shield", 20))

    my_hero.battle(opponent)