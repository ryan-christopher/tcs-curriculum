from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController

window.borderless = False

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
blackstone_texture = load_texture('assets/blackstone.png')
punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)

block_pick = 1

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1'] or held_keys['2'] or held_keys['3'] or held_keys['4'] or held_keys['5']:
        global block_pick
    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys['5']:
        block_pick = 5


class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture, model = 'assets/block', scale = 0.5, origin_y = 0.5):
        super().__init__(
            parent = scene,
            position = position,
            model = model,
            origin_y = origin_y,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.rgb(230,230,230),
            scale = scale
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(
                        position = self.position + mouse.normal,
                        texture = grass_texture
                    )
                if block_pick == 2:
                    voxel = Voxel(
                        position = self.position + mouse.normal,
                        texture = stone_texture
                    )
                if block_pick == 3:
                    voxel = Voxel(
                        position = self.position + mouse.normal,
                        texture = brick_texture
                    )
                if block_pick == 4:
                    voxel = Voxel(
                        position = self.position + mouse.normal,
                        texture = dirt_texture
                    )
                if block_pick == 5:
                    voxel = Voxel(
                        model = 'cube',
                        origin_y = 0.3,
                        scale = 1,
                        position = self.position + mouse.normal,
                        texture = blackstone_texture
                    )
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    def active(self):
        self.position = Vec2(0.3, -0.5)
    def passive(self):
        self.position = Vec2(0.35, -0.55)


for z in range(-15,15):
    for x in range(-15,15):
        voxel = Voxel((x,0,z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()