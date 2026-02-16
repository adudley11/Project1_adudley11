from direct.showbase.ShowBase import ShowBase
from direct.task import Task
import math, sys, random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        self.SetupScene()

        
        self.accept('escape', self.quit)
    # Prepare message if server wants to quit
    def quit(self):
        sys.exit()

    def SetupScene(self):
        self.Universe = self.loader.loadModel('./Assets/Universe/Universe.x')
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex, 1)
        
        self.Planet1 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(180, 4300, 70)
        self.Planet1.setScale(350)
        
app = MyApp()
app.run()
