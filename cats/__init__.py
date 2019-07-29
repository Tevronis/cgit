
GREEN = 'green'
BLUE = 'blue'

RARITIES = [GREEN, BLUE]


class Cat:

    def __init__(self, name='', age=None, color=None,
                 rarity=GREEN, value=1):
        self.name = name
        self.age = age
        self.color = color
        self.rarity = rarity
        self.value = value
        # preferencies food

    def sleep(self):
        raise NotImplementedError()

    def dump(self):
        return {
            'name': self.name,
            'age': self.age,
            'color': self.color,
            'rarity': self.rarity,
            'value': self.value,
            'class': self.__class__.__name__
        }
