from ursina import *
import math

class Player:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

        self.RUN_SPEED = 0.1
        self.TURN_SPEED = 0.6
        self.GRAVITY = -0.01
        self.JUMP_POWER = 2

        self.TERRAIN_HEIGHT = 0

        self.currentSpeed = 0
        self.currentTurnSpeed = 0
        self.upwardsSpeed = 0

        self.isInAir = False

        self.position = [0,0,0]
        self.rotation = [0,0,0]

    def move(self):
        Yrot               = 1.0 * (self.currentTurnSpeed * self.engine.getFrameTimeSeconds())       
        distance           = 1.0 * (self.currentSpeed * self.engine.getFrameTimeSeconds())
        self.upwardsSpeed += 1.0 * (self.GRAVITY * self.engine.getFrameTimeSeconds())
        dx = 1.0 * (distance * math.sin(Yrot+self.rotation[1]))
        dz = 1.0 * (distance * math.cos(Yrot+self.rotation[1]))

        self.increaseRotation(0,Yrot,0)
        self.increasePosition(dx, 0, dz)

        dy = 1.0 * (self.upwardsSpeed * self.engine.getFrameTimeSeconds())
        self.increasePosition(0, dy, 0)
        if self.position[1] < self.TERRAIN_HEIGHT:
            self.upwardsSpeed = 0
            self.position[1] = 0
            self.isInAir = False

    def jump(self):
        if not self.isInAir:
            self.upwardsSpeed = self.JUMP_POWER
            self.isInAir = True

    def render(self):
        self.model.draw(pos=self.position, rotations=self.rotation)

    def handleEvents(self, event):
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.currentSpeed = self.RUN_SPEED
            elif event.key == K_s:
                self.currentSpeed = -self.RUN_SPEED

            if event.key == K_a:
                self.currentTurnSpeed = self.TURN_SPEED
            elif event.key == K_d:
                self.currentTurnSpeed = -self.TURN_SPEED

            if event.key == K_SPACE:
                self.jump()

        else:
            self.currentSpeed = 0
            self.currentTurnSpeed = 0
    def increaseRotation(self,dx,dy,dz):
        self.rotation = [self.rotation[0]+dx,
                         self.rotation[1]+dy,
                         self.rotation[2]+dz]

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'quad', 
            origin_y = 10,
            texture = 'brick', 
            color = color.color(0,0,random.uniform(0.7,0.8)), 
            highlight_color = color.color(1,0.8,10),
            )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            

app = Ursina()

for x in range(10):
    for y in range(10):
            voxel = Voxel(position = (x,y))


player = Player()

app.run()