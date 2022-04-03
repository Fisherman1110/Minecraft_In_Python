from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random


app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
granite_texture = load_texture('assets/granite_texture.png')
barrel_texture = load_texture('assets/barrel_bottom.png')
acacia_log_texture = load_texture('assets/acacia_log.png')
acacia_planks_texture = load_texture('assets/acacia_planks.png')
bedrock_texture = load_texture('assets/bedrock.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
punch_sound   = Audio('assets/punch_sound.wav',loop = False, autoplay = False)
block_pick = random.randint(1,9)


window.fps_counter.enabled = True
window.exit_button.visible = False
window.fullscreen = False

def update():
	global block_pick

	if held_keys['right mouse'] or held_keys['left mouse']:
		hand.active()
	else:
		hand.passive()



	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4
	if held_keys['5']: block_pick = 5
	if held_keys['6']: block_pick = 6
	if held_keys['7']: block_pick = 7
	if held_keys['8']: block_pick = 8
	if held_keys['9']: block_pick = 9



class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			origin_y = 0.5 ,
			model = 'assets/block',
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)




	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = granite_texture)
				if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = barrel_texture)
				if block_pick == 7: voxel = Voxel(position=self.position + mouse.normal, texture=acacia_log_texture)
				if block_pick == 8: voxel = Voxel(position=self.position + mouse.normal, texture=acacia_planks_texture)
				if block_pick == 9: voxel = Voxel(position=self.position + mouse.normal, texture=bedrock_texture)



			if key == 'left mouse down':
				punch_sound.play()
				destroy(self)



class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 1000,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))



	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)





for z in range(30):
	for x in range(30):
		voxel = Voxel(position = (x,0,z),texture=('assets/grass_block.png'))
		voxel = Voxel(position = (x,-1,z),texture=('assets/dirt_block.png'))
		voxel = Voxel(position=(x, -2, z),texture=('assets/stone_block.png'))
		voxel = Voxel(position=(x,-3,z),texture=('assets/granite.png'))
		voxel = Voxel(position=(x, -4, z), texture=('assets/bedrock.png'))


player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()


