import random
import matplotlib.pyplot


class Predator:
    def __init__(self):
        self._size = random.randint(1, 2)

    def get_size(self):
        return self._size


class Prey:
    def __init__(self):
        self._color = self.color_selection()

    def color_selection(self):
        colors = ['red', 'blue', 'green', 'purple', 'orange']
        return colors[random.randint(0, 4)]

    def get_color(self):
        return self._color


def simulate():
    # Generate Prey Array
    red = 0
    blue = 0
    green = 0
    purple = 0
    orange = 0
    the_prey = []
    for i in range(100):
        prey = Prey()
        the_prey.append(prey)
        if the_prey[i].get_color() is 'red':
            red += 1
        if the_prey[i].get_color() is 'blue':
            blue += 1
        if the_prey[i].get_color() is 'green':
            green += 1
        if the_prey[i].get_color() is 'purple':
            purple += 1
        if the_prey[i].get_color() is 'orange':
            orange += 1

    # Generate Predator Array
    the_predators = []
    for i in range(10):
        predator = Predator()
        the_predators.append(predator)

    # Simulate 70 attacks
    for i in range(70):
        prey = the_prey[random.randint(0, len(the_prey) - 1)]
        predator = the_predators[random.randint(0, len(the_predators) - 1)]
        if predator.get_size() == 2:
            the_prey.remove(prey)

    red_after = 0
    blue_after = 0
    green_after = 0
    purple_after = 0
    orange_after = 0
    for i in the_prey:
        if i.get_color() is 'red':
            red_after += 1
        if i.get_color() is 'blue':
            blue_after += 1
        if i.get_color() is 'green':
            green_after += 1
        if i.get_color() is 'purple':
            purple_after += 1
        if i.get_color() is 'orange':
            orange_after += 1

    print('decimal chance of survival: ')
    print('red: ' + str((red - red_after) / red))
    print('blue: ' + str((blue - blue_after) / blue))
    print('green: ' + str((green - green_after) / green))
    print('purple: ' + str((purple - purple_after) / purple))
    print('orange: ' + str((orange - orange_after) / orange))

    matplotlib.pyplot.bar('blue', ((blue - blue_after) / blue))
    matplotlib.pyplot.bar('orange', ((orange - orange_after) / orange))
    matplotlib.pyplot.bar('green', ((green - green_after) / green))
    matplotlib.pyplot.bar('red', ((red - red_after) / red))
    matplotlib.pyplot.bar('purple', ((purple - purple_after) / purple))

    matplotlib.pyplot.show()


simulate()
