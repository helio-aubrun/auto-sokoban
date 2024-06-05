class MapGenerator:
    WALL = -1
    EMPTY = 0
    GOAL = 1
    BOX = 2
    BOX_ON_GOAL = 4

    @staticmethod
    def generate(level):
        if level == 1:
            return MapGenerator.level1()
        elif level == 2:
            return MapGenerator.level2()
        elif level == 3:
            return MapGenerator.level3()

    @staticmethod
    def level2():
        return [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  2,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  0, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  2,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]



    @staticmethod
    def level3():
        return [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1,  0, -1],
        [-1,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  2,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1,  0,  0,  0,  2,  0,  0,  0,  1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1, -1, -1,  0, -1, -1,  0, -1],
        [-1,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0,  0,  2,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]



    @staticmethod
    def level1():
        return [
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1, -1],
        [-1,  0,  0,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1,  -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  0, -1],
        [-1,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  0, -1],
        [-1,  0, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1],
        [-1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  1, -1],
        [-1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  0, -1],
        [-1,  0, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1],
        [-1,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1,  0,  1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0, -1, -1,  0,  1, -1],
        [-1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  1,  0,  2,  0,  0, -1],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]

