import json

from resources import cats


class User:
    def __init__(self):
        pass

    def save_game(self):
        result = {}
        for cat in cats:
            result[cat.name] = cat.dump()
        # print(result)
        with open('save.json', 'w') as f:
            json.dump(result, f, indent=2)
