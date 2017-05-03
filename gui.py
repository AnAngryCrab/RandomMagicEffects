from appJar import gui
from listreader import ListReader
from magiceffects import MagicEffects

lr = ListReader()
me = MagicEffects(lr.getlist())

def geteff(x):
    app.setLabel("Lab", me.geteffect())



app = gui("Random Magic Effects")

app.addLabel("Lab", "")
app.addButton("Go!", geteff)

app.go()