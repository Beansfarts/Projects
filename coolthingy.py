from ursina import *
import random
import time

Text.default_font = 'Minecraft.ttf'
Text.default_resolution = 10000* Text.size

game = Ursina(title = "Ursina Test Game")
enemyhp = 100
zombheal = 100
power = 10


##FUNCTIONS## 
baguette = 0
def beta():
    global baguette
    baguette +=1
    print("You got a baguette!")
    time.sleep(0.1)
    e1.enabled = False
    time.sleep(0.1)
    rand = random.randint(1,2)
    if rand == 1:
        zombie.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
    if rand == 2:
        e1.enabled = True
        bgtxt.enabled = True
        zombie.enabled = False
        zombtxt.enabled = False
def sigma():
    rand = random.randint(1,2)
    if rand == 1:
        zombie.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
    if rand == 2:
        e1.enabled = True
        bgtxt.enabled = True
        zombie.enabled = False
        zombtxt.enabled = False
def skibidi2():
    button.texture = 'dice2' 
def alpha2():
    button.texture = 'dice'
def introplay():
    rand = random.randint(1,2)
    if rand == 1:
        zombie.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True
    if rand == 2:
        buttonplay.enabled = False
        e1.enabled = True
        bgtxt.enabled = True
        zombie.enabled = False
        zombtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True
def close():
    rand = random.randint(1,2)
    if rand == 1:
        closeButton.enabled = False
        zombie.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True
        shopGuy.enabled = False
        grug.enabled = False
    if rand == 2:
        buttonplay.enabled = False
        e1.enabled = True
        bgtxt.enabled = True
        zombie.enabled = False
        zombtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True
        shopGuy.enabled = False
        grug.enabled = False
        closeButton.enabled = False
def sigma():
    rand = random.randint(1,2)
    if rand == 1:
        zombie.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
        buttonplay.enabled = False
    if rand == 2:
        buttonplay.enabled = False
        e1.enabled = True
        bgtxt.enabled = True
        zombie.enabled = False
        zombtxt.enabled = False
def zombie():
    print("hi")
def playerturn(enemyheal):
    rand = random.randint (8,30)
    print ("You attacked the enemy.")
    rand (power * .05)
    enemyheal -= rand


    rand=random.randint(23,35)
    print("w zombie fight ")
    closeButton.enabled = False
    zombie.enabled = True
    zombtxt.enabled = False
    e1.enabled = False
    bgtxt.enabled = False
    buttonplay.enabled = False
    button.enabled = False
    intro.enabled = False
    shopbutton.enabled = False
    inventorybutton.enabled = False
    shopGuy.enabled = False
    grug.enabled = False
    hp -= rand
    if hp <= 0:
        print("you lost :/")

def playerAtk():
    enemyhp -= 28
    if enemyhp <= 0:
        print("hehehe zombie lost")
        zombie.enabled = False


def alpha2():
    button.texture = 'dice'
def skibidi():
    buttonplay.texture = "HoverButton" 
def alpha():
    buttonplay.texture = "playbutton"
def inventory():
    print("Inventory Opened.")
def shop():
    print("Shop opened.")
    buttonplay.enabled = False
    e1.enabled = False
    bgtxt.enabled = False
    zombie.enabled = False
    zombtxt.enabled = False
    buttonplay.enabled = False
    button.enabled = False
    intro.enabled = False
    shopGuy.enabled = True
    grug.enabled = True
    closeButton.enabled = True
def qte():
    while True:
        arrow.x +=0.3
        time.sleep(0.3)

##ENTITIES##
grug = Text(
    text='wanna buy something? (RHYMES WITH GRUG)',
    scale=2,
    color=color.black,
    origin=(0,0.6)
    )
e1 = Entity(model='cube', texture='Images/baguette.png',
    on_click=beta,
    collider= "box")
button = Entity(model = "quad", texture="dice", 
    #color=color.yellow,
    origin=(-6,-2.8),
    collider = "box",
    on_click= sigma,
    on_mouse_enter= skibidi2,
    on_mouse_exit= alpha2)
inventorybutton = Entity(model = "quad", texture="inventory", 
    #color=color.yellow,
    origin=(6,2.8),
    collider = "box",
    on_click= inventory)
shopbutton = Entity(model = "quad", texture="shopButton", 
    origin=(6, 1.4),
    collider = "box",
    on_click= shop)
closeButton = Entity(model = "quad", texture="closeButton", 
    origin=(-6,-2.8),
    collider = "box",
    on_click= close)
shopGuy = Entity(model = "quad", texture="grugGood", 
    origin=(0,0.5),
    scale=4.7,
)
intro = Text(
    text='cool ursina game!!!!!',
    scale=2,
    color=color.black,
    origin=(0,-2)
    )
buttonplay = Entity(model = "quad", 
    texture="playbutton", 
    collider ="box",
    on_click= introplay,
    on_mouse_enter= skibidi,
    on_mouse_exit = alpha,
)
bar = Entity(model = "quad",
    texture="bar1",
    scale = (4,2),
    origin=(0,1)
)


greenBar = Entity(model = "quad",
    color = color.green,
    scale = (0.8,0.56),
    origin=(0,3.17)
)

arrow = Entity(model = "quad",
    scale = 0.7,
    origin=(2.3,3),
    on_click = qte,
    collider= "box",
    texture="bar0")

arrow.world_position = Vec3(0,0,-2.1)
greenBar.world_position = Vec3(0,0,-2)
buttonplay.world_position = Vec3(0,0,-1)
bgtxt = Text(
    text='You found a baguette!',
    origin=(0,-2),
    scale=2,
    color=color.black,
    )
zombtxt = Text(
    'You found a Zombie!',
    origin=(0,-2),
    scale=2,
    color=color.black
)

def update():
    baguettes.text = baguette
    
baguettes = Text(
    text= str(baguette),
    origin=(0,-5),
    scale=2,
    color=color.black
)
baguetteCounter = Entity(model='cube', texture='Images/baguette.png',
    collider= "box",
    origin=(-1,-5))
zombie = Entity(model = "quad", texture="zombie", 

origin=(0,0),
scale=2,
collider = "box",
on_click = zombie
)

##BEGINNING-VARIUBLES##
zombie.enabled = False
zombtxt.enabled = False
bgtxt.enabled = False
e1.enabled = False
button.enabled = False
shopbutton.enabled = False
inventorybutton.enabled = False
shopGuy.enabled = False
grug.enabled = False
closeButton.enabled = False
greenBar.enabled = True
bar.enabled = True
arrow.enabled = True
##GAME-STARTER##
game.run()