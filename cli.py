from listreader import ListReader
from magiceffects import MagicEffects
import time

lr = ListReader()
me = MagicEffects(lr.getlist())

while True:
    print(me.geteffect())
    time.sleep(1)
