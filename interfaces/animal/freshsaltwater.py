from .aquatic import IAquatic

class IFreshSaltwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "isotonic"