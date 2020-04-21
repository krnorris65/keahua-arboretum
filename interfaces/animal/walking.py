from .terrestrial import ITerrestrial

class IWalking(ITerrestrial):

    def __init__(self, leg_count=2):
        super().__init__()
        self.leg_count = leg_count
        self.move_speed = 0
