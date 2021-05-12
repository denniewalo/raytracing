from Color import Color
class CheckerBoardMaterial(object):
    def __init__(self):
        self.baseColor = Color(255, 255, 255)
        self.otherColor = Color(0, 0, 0)
        self.checkSize = 1
        self.counter = 0

    def ColorAt(self, p, collide):
        amb = 0.7
        p = p * (1. / self.checkSize)
        if collide:
            if (int(abs(p[0] + 0.5) + int(abs(p[1] + 0.5) + int(abs(p[2] + 0.5))))) % 2:
                return self.otherColor.getColor()
            return Color.multiplayColor(self.baseColor, amb).getColor()
        else:
            if (int(abs(p[0] + 0.5) + int(abs(p[1] + 0.5) + int(abs(p[2] + 0.5))))) % 2:
                return self.otherColor.getColor()
        return self.baseColor.getColor()