from threading import Timer
from ursina import *
import random
import time

inventory = {"Stick": 1, "Baguette" : 2}
inventoryKeys = list(inventory.keys())
spritemaps = {"Baguette": "baguette", "Stick": "stick"}

array = []
Text.default_font = 'Minecraft.ttf'
Text.default_resolution = 10000* Text.size
GreenBarScaleX = 1

playerheal = 100
inBattle = False
gameStart = True
idkmaybeon = False
rand = random
game = Ursina(title = "Ursina Test Game")
zombheal = 100
power = 10
dir = +0.1
dir2 = +0.1
arrowEnabled = True
timedelay = 5
##FUNCTIONS## 
def zombie():
    global inBattle
    inBattle = True
    #global timer
   #timer = Timer(2, attack)
    #print("hello you battle me now >:)")
    #ShowBar()
    #if ray.hit:
        #print("ow")
        #timer.start()
    #else
#def attack():
    #rand = random.randint(27,49)
    #playerheal -= rand
    #print("ow goes you")


#inventoryKeys = list(inventory.keys())
def GetInventoryAsText():
    text = ""
    for item in inventory:
        if inventory [item] != 0:
            text += "\t" + item + "= " + str (inventory [item])
    return text

def PrintInventory():
    for item in inventory:
        if inventory [item] != 0:
            print("\t" + item + "= " + str (inventory [item]))

def ChangeInventory(item, quantity):
    if item in inventory:
        inventory [item] += quantity
        if inventory[item] <= 0:
            del inventory[item]
        print (inventory)
    elif quantity > 0:
        inventory[item] = quantity
        PrintInventory()

def displayInventory():
    print(inventory)
    i = 0
    for key, value in inventory.items():
        square = Entity(model = "quad", texture="HoverButton",
        origin=(7.8-i*2,-3.4),
        scale = 0.67
        )
        variuble = spritemaps[key]
        item = Entity(model = "quad", texture = variuble,
            origin=(9.3-i*2.36,-4),
            scale = 0.56,
            always_on_top = True
        )
        array.append(square)
        array.append(item)
        txtVariuble = Text(
            text=value,
            color =color.black,
            scale = 1,
            origin=(54 - i * 15, -9),  
            always_on_top = True                                    
        )
        print(txtVariuble.origin, txtVariuble.scale)
        array.append(txtVariuble)
        i += 1
zombie1 = Entity(model = "quad", texture="zombie", 
origin=(0,0),
scale=2,
collider = "box",
on_click = zombie

)
def beta():
    global baguette
    ChangeInventory("Baguette", 1)
    print("You got a baguette!")
    time.sleep(0.1)
    e1.enabled = False
    time.sleep(0.1)
    rand = random.randint(1,2)
    if rand == 1:
        zombie1.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
    if rand == 2:
        e1.enabled = True
        bgtxt.enabled = True
        zombie1.enabled = False
        zombtxt.enabled = False
def sigma():
    rand = random.randint(1,2)
    if rand == 1:
        zombie1.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
    if rand == 2:
        e1.enabled = True
        bgtxt.enabled = True
        zombie1.enabled = False
        zombtxt.enabled = False
def openinventory():
        displayInventory()
        button0Text.enabled = False
        baguetteInventory.enabled = False
        dolla.enabled = False
        closeButton.enabled = True
        zombie1.enabled = False
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
        panel.enabled = False
        buttonshop.enabled = False
def skibidi2():
    button.texture = 'dice2' 
def alpha2():
    button.texture = 'dice'
def introplay():
    rand = random.randint(1,2)
    if rand == 1:
        zombie1.enabled = True
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
        zombie1.enabled = False
        zombtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True

def sigma():
    rand = random.randint(1,2)
    if rand == 1:
        zombie1.enabled = True
        zombtxt.enabled = True
        e1.enabled = False
        bgtxt.enabled = False
        buttonplay.enabled = False
    if rand == 2:
        buttonplay.enabled = False
        e1.enabled = True
        bgtxt.enabled = True
        zombie1.enabled = False
        zombtxt.enabled = False
def playerturn(enemyheal):
    rand = random.randint (8,10)
    print ("You attacked the enemy.")
    rand (power * .02)
    enemyheal -= rand
def billy():
    rand=random.randint(23,35)
    print("w zombie1 fight ")
    closeButton.enabled = False
    zombie1.enabled = True
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
        print("hehehe zombie1 lost")
        zombie1.enabled = False


def alpha2():
    button.texture = 'dice'
def skibidi():
    buttonplay.texture = "HoverButton" 
def alpha():
    buttonplay.texture = "playbutton" 
def shop():
    global inBattle
    print("Shop opened.")
    baguetteInventory.enabled = True
    dolla.enabled = True
    buttonplay.enabled = False
    e1.enabled = False
    bgtxt.enabled = False
    zombie1.enabled = False
    zombtxt.enabled = False
    buttonplay.enabled = False
    button.enabled = False
    intro.enabled = False
    shopGuy.enabled = True
    grug.enabled = True
    closeButton.enabled = True
    inBattle = False
def ShowBar():
    ##to delay it from starting this use invoke(ShowBar, delay = ???) and put that in a function or something
    arrow.enabled = True
    bar.enabled = True
    greenBar.enabled = True
    ##finish enabling/disabling qte
def HideBar():
    arrow.enabled = False
    bar.enabled = False
    greenBar.enabled = False
def start():
    HideBar()
def gudbutton():
    button0Text.enabled = True
    print("you uhhh open smth :0")
    panel.enabled = True
    buttonshop.enabled = True

def butttoncool():
    global baguette
    bobbity.enabled = True
    ChangeInventory("Baguette", 1)
    bobbity.enabled = False
def Baguetter():
    global timer
    global baguette

    timer = Timer(timedelay, butttoncool)
    timer.start()
    print("hello :0")
    bobbity.enabled = True
    ChangeInventory("Baguette", -1)
def win():
    winner.enabled = False



##ENTITIES##

grug = Text(
    text='wanna buy something? (RHYMES WITH GRUG)',
    scale=2,
    color=color.black,
    origin=(0,-6)
    )
e1 = Entity(model='cube', texture='Images/baguette.png',
    on_click=beta,
    collider= "box")
bobbity = Text(
    text='wow you... bought a baguette... with a baguette. uhm....',
    scale=2,
    color=color.white,
    origin=(0,0),
)
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
    on_click= openinventory)
shopbutton = Entity(model = "quad", texture="shopButton", 
    origin=(6, 1.4),
    collider = "box",
    on_click= shop)
shopGuy = Entity(model = "quad", texture="grugGood", 
    origin=(-0.05,0.5),
    scale=4.7,
)
dolla = Entity(model = "quad", texture="billy",
    origin = (0,-0.8),
    scale=2.5,
    collider = "box",
    on_click= gudbutton)
intro = Text(
    text='cool ursina game!!!!!',
    scale=2,
    color=color.black,
    origin=(0,-2)
    )
panel = Entity(model = "quad", texture ="panel",
    scale=(3,4.9),
    origin=(0,0)
    )
buttonshop = Entity(model = "quad", texture ="buttonShop",
    scale=1.2,
    origin=(0,0),
    collider = "box",
    on_click= Baguetter
    )
button0Text = Text(
    text='baguette',
    scale=0.7,
    color=color.black,
    origin=(0,0)
)
buttonshop1 = Entity(model = "quad", texture ="buttonShop",
    scale=1.2,
    origin=(0,2.5),
    enabled = False
    )
buttonshop2 = Entity(model = "quad", texture ="buttonShop",
    scale=1.2,
    origin=(0,1.5),
    enabled = False
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
    scale = (GreenBarScaleX, 0.56),
    collider= "box",
    origin=(random.randrange(bar.origin.X - bar.scale.X , bar.origin.X + bar.scale.X ) * 0.5 ,3)
)

arrow = Entity(model = "quad",
    scale = 0.7,
    origin=(2.3,3),
    texture="bar0"
)

panel.always_on_top_setter(True)
buttonshop.always_on_top_setter(True)
buttonshop1.always_on_top_setter(True)
buttonshop2.always_on_top_setter(True)
arrow.world_position = Vec3(0,0,-3)
arrow.always_on_top_setter(True)
greenBar.world_position = Vec3(0,0,-3)
buttonplay.world_position = Vec3(0,0,-1)
dolla.world_position = Vec3(0,0,3)
buttonshop.world_position = Vec3(0,0,-1)
bgtxt = Text(
    text='You found a baguette!',
    origin=(0,-2),
    scale=2,
    color=color.black,
    )
zombtxt = Text(
    'You found a zombie1!',
    origin=(0,-2),
    scale=2,
    color=color.black
)
winner = Text(
    'You win !1!!',
    origin=(0,-2),
    scale=2,
    color=color.black
)
baguetteInventory = Text(
    origin = (0,0),
    scale=2,
    color=color.black
)
baguettes = Text(
    origin=(0,-5),
    scale=2,
    color=color.black
)
winText = False
def update():
    global winText
    global rand
    global zombheal
    global dir
    global baguette
    global arrowEnabled
    global idkmaybeon
    global gameStart
    global inBattle
    global timer
    baguetteInventory.text = GetInventoryAsText()
    if "Baguette" in inventory:
        baguettes.text = inventory["Baguette"]
    else:
        baguettes.text = "0"
    ray = raycast(arrow.position - Vec2.one * 2 + Vec2(arrow.scale_x_getter() / 2, 0), direction=Vec2(0, 1), distance=2, debug=True)
    if gameStart == True:
        start()
        gameStart = False
    if arrowEnabled == True:
       arrow.x += dir
    if arrow.x >= 3:
          dir = -0.1
    if arrow.x <= -0:
           dir = +0.1
    #--INACURATE--# ray = raycast(arrow.position - Vec2.one * 2 + Vec2(0.35, 0), direction=Vec2(0, 1), distance=2, debug=True)
    #--ACCURATE--#
    
    if held_keys ["q"] and inBattle == True:
        ShowBar()
        invoke(HideBar, delay=5)
    if winText == True:
        winner.enabled = True
        timer = Timer(timedelay, win)
        timer.start()
        winText = False
    if held_keys ["space"] and arrowEnabled:
        dir = 0
        if ray.hit == True and inBattle == True:
            rand = random.randint(25,48)
            print("ya hit it !1!!")
            print(ray.hit)
            ChangeInventory("Baguette", 1)
            zombheal -= rand
            time.sleep(2)
            HideBar()
            dir = 0.1
            print(zombheal)
        if ray.hit == False and inBattle == True:
            print("you missed.. :(")
            time.sleep(2)
            HideBar()
            dir = 0.1
#fixed (trust me PLEASE) >:) >:) >:) >:) >:) >:)
    if zombheal <= 0:
        print("you win! woohoo")
        inBattle = False
        zombie1.enabled = False
        zombtxt.enabled = False
        winText = True
        newtimer = Timer(3, win)
        newtimer.start()
        zombheal = 100

        


baguetteCounter = Entity(model='cube', texture='Images/baguette.png',
    collider= "box",
    origin=(-1,-5))



##BEGINNING FUNCTIONS
def close():
    rand = random.randint(1,2)
    for item in array:
        item.enabled = False 
    array.clear()  
    if rand == 1:
        button.enabled = True
        print("button :)")
        button0Text.enabled = False
        baguetteInventory.enabled = False
        dolla.enabled = False
        closeButton.enabled = False
        zombie1.enabled = True
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
        panel.enabled = False
        buttonshop.enabled = False
    if rand == 2:
        button.enabled = True
        print("button :)")
        buttonplay.enabled = False
        e1.enabled = True
        button0Text.enabled = False
        bgtxt.enabled = True
        zombie1.enabled = False
        zombtxt.enabled = False
        buttonplay.enabled = False
        button.enabled = True
        intro.enabled = False
        shopbutton.enabled = True
        inventorybutton.enabled = True
        shopGuy.enabled = False
        grug.enabled = False
        closeButton.enabled = False
        dolla.enabled = False
        panel.enabled = False
        buttonshop.enabled = False
closeButton = Entity(model = "quad", texture="closeButton", 
    origin=(-6,-2.8),
    collider = "box",
    on_click= close)
##BEGINNING-VARIUBLES##
zombie1.enabled = False
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
dolla.enabled = False
panel.enabled = False
buttonshop.enabled = False
bobbity.enabled = False
button0Text.enabled = False
winner.enabled = False
baguetteInventory.enabled = False
##GAME-STARTER##
game.run()