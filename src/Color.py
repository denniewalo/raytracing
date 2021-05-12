class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getColor(self):
        return (round(self.r), round(self.g), round(self.b))

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __mul__(self, other):
        return Color(self.r * other.r, self.g * other.g, self.b * other.b)

    def divColor(self, value):
        return Color(self.r / value, self.g / value, self.b / value)

    def multiplayColor(self, value):
        return Color(self.r * value, self.g * value, self.b * value)
