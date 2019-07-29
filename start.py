from resources import objects, temp_objects
from user import User
from world import World


user = User()


def main():
    w = World()
    objects.add(w)
    time = 0
    while True:
        for obj in objects:
            obj.run(time)

        objects.update(temp_objects)

        time += 1


if __name__ == '__main__':
    try:
        main()
    except:
        user.save_game()
