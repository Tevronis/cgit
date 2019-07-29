from cats.wildlife import Wildlife
from resources import temp_objects, cats


class World:
    def __init__(self):
        pass

    def run(self, t):
        if t % 1000000 == 0:
            cat = Wildlife(name='Kiska %s' % t)
            temp_objects.add(cat)
            cats.add(cat)
