from enum import Enum
class Direct(Enum):
    
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    LEFT_UP = 5
    RIGHT_UP = 6
    LEFT_DOWN = 7
    RIGHT_DOWN = 8

    def getDirect(pos1, pos2):
        if pos1[0] < pos2[0]:
            if pos1[1] == pos2[1]:
                return  Direct.RIGHT
            elif pos1[1] > pos2[1]:
                return  Direct.RIGHT_UP
            else:
                return Direct.RIGHT_DOWN
        elif pos1[0] > pos2[0]:
            if pos1[1] == pos2[1]:
                return  Direct.LEFT
            elif pos1[1] > pos2[1]:
                return  Direct.LEFT_UP
            else:
                return Direct.LEFT_DOWN
        elif pos1[1] < pos2[1]:
            return  Direct.UP
        elif pos1[1] > pos2[1]:
            return Direct.DOWN
        return None

    def getArrow(x, y, r, direct):
        if direct == Direct.RIGHT:
            return ((x, y+r), (x, y-r), (x+r, y))
        elif direct == Direct.LEFT:
            return ((x, y+r), (x, y-r), (x-r, y))
        elif direct == Direct.UP:
            return ((x+r, y), (x-r, y), (x, y+r))
        elif direct == Direct.DOWN:
            return ((x+r, y), (x-r, y), (x, y-r))
        elif direct == Direct.RIGHT_UP:
            return ((x+r, y-r), (x+r, y), (x, y-r))
        elif direct == Direct.LEFT_UP:
            return ((x-r, y-r), (x-r, y), (x, y-r))
        elif direct == Direct.RIGHT_DOWN:
            return ((x+r, y+r), (x+r, y), (x, y+r))
        else:
            return ((x-r, y+r), (x-r, y), (x, y+r))
