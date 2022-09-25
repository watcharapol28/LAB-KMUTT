from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController


class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube', 
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

for z in range(10):
    for y in range(10):
        for x in range(10):
            voxel = Voxel(position = (x,y,z))
player = FirstPersonController()

app.run()