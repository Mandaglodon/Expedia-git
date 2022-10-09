from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('grass_block.png')
brick_texture = load_texture('brick_block.png')
stone_texture = load_texture('stone_block.png')


def update():
    global block_pick

    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    #if held_keys['4']: block_pick = 4


block_pick = 1


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='block_head',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position=self.position
                                  + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    voxel = Voxel(position=self.position
                                  + mouse.normal, texture=brick_texture)
                if block_pick == 3:
                    voxel = Voxel(position=self.position
                                  + mouse.normal, texture=stone_texture)
                #if block_pick ==1: voxel = Voxel(position=self.position + mouse.normal, texture= grass_texture)
            if key == 'right mouse down':
                destroy(self)


for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController()
app.run()
