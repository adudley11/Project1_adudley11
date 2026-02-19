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
        # Scenes Background
        self.Universe = self.loader.loadModel('./Assets/Universe/Universe.x')
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        space = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(space, 1)
        
        # Space Station
        self.Station = self.loader.loadModel('./Assets/SpaceStation/spaceStation.x')
        self.Station.reparentTo(self.render)
        self.Station.setPos(50, 3000, 575)
        self.Station.setScale(10)
        tex1 = self.loader.loadTexture("./Assets/SpaceStation/SpaceStation1_Dif2.png")
        self.Station.setTexture(tex1, 1)
        
        # Space Ship
        self.Ship = self.loader.loadModel('./Assets/Spaceships/Dumbledore.x')
        self.Ship.reparentTo(self.render)
        self.Ship.setPos(0, 500, -30)
        self.Ship.setScale(10)
        tex2 = self.loader.loadTexture("./Assets/Spaceships/spacejet_C.png")
        self.Station.setTexture(tex2, 1)
        
        # Planets
        self.Planet1 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(-1500, 4300, 70)
        self.Planet1.setScale(350)
        surf1 = self.loader.loadTexture("./Assets/Planets/Planet-1.jpg")
        self.Planet1.setTexture(surf1, 1)

        self.Planet2 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(-270, 1000, -300)
        self.Planet2.setScale(72)
        surf2 = self.loader.loadTexture("./Assets/Planets/Planet-2.jpg")
        self.Planet2.setTexture(surf2, 1)

        self.Planet3 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(400, 2500, 250)
        self.Planet3.setScale(135)
        surf3 = self.loader.loadTexture("./Assets/Planets/Planet-3.jpg")
        self.Planet3.setTexture(surf3, 1)

        self.Planet4 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(1000, 10000, -1180)
        self.Planet4.setScale(239)
        surf4 = self.loader.loadTexture("./Assets/Planets/Planet-4.jpg")
        self.Planet4.setTexture(surf4, 1)

        self.Planet5 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(2000, 6000, -90)
        self.Planet5.setScale(60)
        surf5 = self.loader.loadTexture("./Assets/Planets/Planet-5.jpg")
        self.Planet5.setTexture(surf5, 1)

        self.Planet6 = self.loader.loadModel('./Assets/Planets/protoPlanet.x')
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(-1116, 5000, 1500)
        self.Planet6.setScale(240)
        surf6 = self.loader.loadTexture("./Assets/Planets/Planet-6.jpg")
        self.Planet6.setTexture(surf6, 1)
        

app = MyApp()
app.run()
