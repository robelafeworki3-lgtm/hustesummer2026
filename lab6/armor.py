import random

class Armor:
    def __init__(self, name, max_block):
        """
        Instance properties:
        name: String
        max_block: Integer
        """
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        """
        Returns random block amount
        between 0 and max_block
        """
        return random.randint(0, self.max_block)


if __name__ == "__main__":
    shield = Armor("Energy Shield", 30)

    print(shield.name)
    print(shield.block())