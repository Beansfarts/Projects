
from ursina import *
import time
import random


game = Ursina()

bar = Entity()
greenBar = Entity(model = "quad", color = color.green)
arrow = Entity(model = "quad", texture="theBarMouse")
arrow.world_position = Vec3(0,0,-2)

game.run()