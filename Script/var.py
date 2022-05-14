screen = None
clock = None
FPS = 40

scene = 'title'
state = ''
menu = False

class Level_Select():
    camera = [0, 0]

class Battle():
    player_energy = 0
    player_energy_max = 0
    player_life = 0
    player_life_max = 0
    
class Save():
    level_status = {
        1 : 1,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
    }