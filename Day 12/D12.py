import numpy as np


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    commands = [[line[0], line[1:]] for line in lines]


class ShipQ1:

    def __init__(self):
        self.heading = 0
        self.x_pos = 0
        self.y_pos = 0

    def left(self, degrees):
        self.heading += degrees
        while self.heading >= 360:
            self.heading -= 360

    def right(self, degrees):
        self.heading -= degrees
        while self.heading <= 360:
            self.heading += 360

    def north(self, amount):
        self.y_pos += amount

    def south(self, amount):
        self.y_pos -= amount

    def east(self, amount):
        self.x_pos += amount

    def west(self, amount):
        self.x_pos -= amount

    def forward(self, dist):
        self.y_pos += int(np.sin(np.deg2rad(self.heading)) * dist)
        self.x_pos += int(np.cos(np.deg2rad(self.heading)) * dist)

    def man_dist(self):
        return abs(self.y_pos) + abs(self.x_pos)

    def __str__(self):
        return f"Heading : {self.heading}\nPosition : {self.x_pos}, {self.y_pos}\n" \
               f"Manhattan distance : {self.man_dist()}"


class ShipQ2:

    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.wp = Weapon()

    def left(self, degrees):
        self.wp.left(degrees, self.x_pos, self.y_pos)

    def right(self, degrees):
        self.wp.right(degrees, self.x_pos, self.y_pos)

    def north(self, amount):
        self.wp.north(amount)

    def south(self, amount):
        self.wp.south(amount)

    def east(self, amount):
        self.wp.east(amount)

    def west(self, amount):
        self.wp.west(amount)

    def forward(self, times):
        for _ in range(times):
            x = self.wp.x - self.x_pos
            y = self.wp.y - self.y_pos
            self.y_pos = self.wp.y
            self.x_pos = self.wp.x
            self.wp.y = self.y_pos + y
            self.wp.x = self.x_pos + x

    def man_dist(self):
        return abs(self.y_pos) + abs(self.x_pos)

    def __str__(self):
        return f"Position : {self.x_pos}, {self.y_pos}\n" \
               f"Manhattan distance : {self.man_dist()}"


class Weapon:

    def __init__(self):
        self.x = 10
        self.y = 1

    def rotate(self, degrees, x_pos, y_pos):
        x = (self.x - x_pos) * np.cos(np.deg2rad(degrees)) - (self.y - y_pos) * np.sin(np.deg2rad(degrees))
        y = (self.y - y_pos) * np.cos(np.deg2rad(degrees)) + (self.x - x_pos) * np.sin(np.deg2rad(degrees))
        self.x = x + x_pos
        self.y = y + y_pos

    def left(self, degrees, x_pos, y_pos):
        self.rotate(degrees, x_pos, y_pos)

    def right(self, degrees, x_pos, y_pos):
        self.rotate(-degrees, x_pos, y_pos)

    def north(self, amount):
        self.y += amount

    def south(self, amount):
        self.y -= amount

    def east(self, amount):
        self.x += amount

    def west(self, amount):
        self.x -= amount


boat = ShipQ2()

for line in commands:

    if line[0] == "N":
        boat.north(int(line[1]))

    elif line[0] == "S":
        boat.south(int(line[1]))

    elif line[0] == "E":
        boat.east(int(line[1]))

    elif line[0] == "W":
        boat.west(int(line[1]))

    elif line[0] == "L":
        boat.left(int(line[1]))

    elif line[0] == "R":
        boat.right(int(line[1]))

    elif line[0] == "F":
        boat.forward(int(line[1]))

print(boat)


