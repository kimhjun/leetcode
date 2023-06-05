import math

bombs = [[1,1,5],[10,10,5]]

class Bomb:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

def in_detonation_range(bomb_1: Bomb, bomb_2: Bomb):
    distance = math.sqrt((bomb_1.x - bomb_2.x) ** 2 + (bomb_1.y - bomb_2.y) ** 2)
    longer_rad = bomb_1.radius if bomb_1.radius >= bomb_2.radius else bomb_2.radius
    return distance <= longer_rad


bbs = [Bomb(*b) for b in bombs]

print(in_detonation_range(bbs[0], bbs[1]))