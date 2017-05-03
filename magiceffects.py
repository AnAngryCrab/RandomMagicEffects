from random import randint

class MagicEffects:

    lines=[]
    def __init__(self, inlist):
        self.lines=inlist

    def geteffect(self):
        r = randint(0, 9999)
        if len(self.lines[r]) > 5:
            return self.lines[r]
        else:
            return self.lines[(r + 1) % 10000]
