class Point:
    """Implement your Point class in here!"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, point):
        new_x = self.x + point.x
        new_y = self.y + point.y
        return Point(new_x, new_y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == '__main__':
    # This won't work until you finish implementing the Point class.
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)