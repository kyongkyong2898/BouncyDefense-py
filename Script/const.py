class Color():
    black = (0, 0, 0)
    white = (255, 255, 255)

class Level_List():
    position = {
        1 : [160, 160],
        2 : [320, 160],
        3 : [480, 160],
        4 : [480, 320],
        5 : [480, 480],
        6 : [640, 480],
        7 : [800, 480],
        8 : [800, 320],
        9 : [800, 640]
    }

    connection = {
        1 : [2],
        2 : [3],
        3 : [4],
        4 : [5],
        5 : [6],
        6 : [7],
        7 : [8, 9]
    }