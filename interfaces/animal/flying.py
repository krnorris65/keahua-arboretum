from .terrestrial import ITerrestrial
class IFlying(ITerrestrial):

    def __init__(self, wing_count=2):
        super().__init__()
        self.flight_speed = 0
        self.wing_count = wing_count

    def fly(self):
        print("Flap flap, I'm flying!")
