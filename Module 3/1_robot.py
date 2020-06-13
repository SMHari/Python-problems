import math

x, y = 0, 0

if __name__ == '__main__':
    distance = 0
    while True:
        directions = input("Enter the direction UP, DOWN, LEFT, RIGHT with #no.of steps")

        if directions == '':
            break
        else:
            directions,step = directions.split(" ")

            if directions == 'UP':
                y = y + int(step)
            elif directions == 'DOWN':
                y = y - int(step)
            elif directions == 'LEFT':
                x = x - int(step)
            elif directions == 'RIGHT':
                x = x + int(step)

    distance = int(round(math.sqrt(x ** 2 + y ** 2)))
    print(distance)
