



0
import time
import random
import sys


'''
print("Lets start this tiny game thingy")
score = 0
question = input ("What is the capital of the U.S?\n")
if question == "Washington DC":
    print ("Correct!")
    score = score +5
    print ("Your score is "+ str (score) +".")
else:
    print ("Wrong, go back to school.")
    score = score -5
    sys.exit
if score >0:
    print ("Here is question 2.")
    question = input ("What is the capital of the capital of the U.K?\n")
if question == "Can i have a BOTTLE OF WATERRRRRRRRRRRRRRRRRRRRRRRRRRRRRR":
    print ("Decent job.")
else:
    question != "Can i have a BOTTLE OF WATERRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
    print ("You are pretty bad.")
    score = score -5
    print ("Your score is now "+ str (score) +".")
'''
'''
x=0
while x != 5:
    print ("Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope!")
    x +=1

print("\n\n")

for i in range(5):
    print ("Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope,Nope!")
'''
#We stopped here (Copy)

inventory = {"Baguette":50,"Stick":0}
inventoryKeys = list(inventory.keys())

#Tutorial: Done
#World 1: not done :( 

stick = 0

hunger = 0
thirst = 0

def playerturn(enemyheal):
    rand = random.randint (8,30)
    if "Sword" in inventory:
        question = input("How would you like to attack?\n1. Stab with a stick\n2. Whack With a baguette\n3. Slash Sword")
        if question == "1":
                print ("You attacked the enemy.")
                rand (power * .05)
                enemyheal -= rand
        if question == "2":
                print ("You attacked the enemy!")
                rand + (power * .05)
                print ("\nYou did"+ str (rand) +"damage.")
                enemyheal -= rand
        if question == "3":
                print ("You attacked the enemy!")
                enemyheal -= 99999999999
                return enemyheal
        
    if "Dirty Rag" and "Sword" in inventory:
        question = input("How would you like to attack?\n1. Stab with a stick\n2. Whack With a baguette\n3. Throw dirty rag\n4. Slash Sword")
        if question == "1":
            print ("You attacked the enemy.")
            rand (power * .05)
            enemyheal -= rand
        if question == "2":
            print ("You attacked the enemy!")
            rand + (power * .05)
            print ("\nYou did"+ str (rand) +"damage.")
            enemyheal -= rand
        if question == "3":
            print ("You attacked the enemy!")
            rand + (power *.03)
            enemyheal -= rand
        if question == "3":
            print ("You attacked the enemy!")
            enemyheal -= rand
        if question == "4":
            print("You attacked the enemy!")
            enemyheal -= 35
            return enemyheal
        
    if  "Sword" and "Dagger" in inventory:
        question = input("How would you like to attack?\n1. Stab with a stick\n2. Whack With a baguette\n3. Throw dirty rag\n4. Slash Sword\n5.Use dagger")
        if question == "1":
            print ("You attacked the enemy.")
            rand (power * .05)
            enemyheal -= rand
        if question == "2":
            print ("You attacked the enemy!")
            rand + (power * .05)
            print ("\nYou did"+ str (rand) +"damage.")
            enemyheal -= rand
        if question == "3":
            print ("You attacked the enemy!")
            rand + (power *.03)
            enemyheal -= rand
        if question == "3":
            print ("You attacked the enemy!")
            enemyheal -= rand
        if question == "4":
            print("You attacked the enemy!")
            enemyheal -= 35
            return enemyheal
        if question == "4":
            rand = random.randint(30,50)
            print("You attacked the enemy!")
            enemyheal-= rand

    question = input ("How Would you like to attack?\n1. Stab with a stick\n2. Whack with a baguette")
    if question == "1":
        print ("You attacked the enemy!")
        rand = newpower + (power * .05)
        enemyheal -= rand
    if question == "2":
        print ("You attacked the enemy!")
        newpower = rand + ( rand * (baguette * .40))
        print ("\nYou did "+ str (rand) +" damage.")
        enemyheal -= rand


    if "Dirty Rag" in inventory:
        question = input("How would you like to attack?\n1. Stab with a stick\n2. Whack With a baguette\n3. Throw dirty rag")
        if question == "1":
            print ("You attacked the enemy.")
            rand (power * .05)
            enemyheal -= rand
        if question == "2":
            print ("You attacked the enemy!")
            rand + (power * .05)
            print ("\nYou did"+ str (rand) +"damage.")
            enemyheal -= rand
        if question == "3":
            print ("You attacked the enemy!")
            rand + (power *.03)
            enemyheal -= rand
        return enemyheal

    question = input ("How Would you like to attack?\n1. Stab with a stick\n2. Whack with a baguette")
    if question == "1":
        print ("You attacked the enemy!")
        rand = newpower + (power * .05)
        enemyheal -= rand
    if question == "2":
        print ("You attacked the enemy!")
        newpower = rand + ( rand * (baguette * .40))
        print ("\nYou did "+ str (rand) +" damage.")
        enemyheal -= rand
    return enemyheal
    
def addInventory(item):
    if item.lower() in inventory:
        inventory [item] +=1
        print (inventory)
    else:
        inventory[item] = 1
        Inventory()

def enemy(enemyhp, attack, name):
    while True:
        playerturn(enemyhp)
        if enemyhp > 0:
            enemyturn(attack, name)
        else:
            print ("You killed the enemy succesfully! Nice!")
        
#Enemy function works for each enemy, attacks, players can attack it, shows enemy names, etc.

def enemyturn(attack, name):
    global health
    health -= attack

def zombie(hp):
    cehp = zombheal
    while True:
        # CEHP = current enemy HP
        global health
        cehp = playerturn(cehp)
        print ("The enemy has "+ str (cehp) +".") 
        if cehp <=0:
            return True
        hp = zombTurn(hp)
        if hp <=0:
            health = hp
            return False

def shop(temp):
    print("You have "+ str (temp)+ " baguettes.")
    question = input("Shopkeeper: you wanna trade me something or buy something?")
    if question == "buy":
        rand = random.randint(1,2)
        if rand == 1:
            question = input("\nYou can purchase an AK47(75 Baguettes), a dagger(25 Baguettes), or a rock(1 Baguette). What do you want to buy?")
            if question == "AK47":
                if inventory["Baguette"] >= 75:
                    print ("You just got an AK47!")
                    addInventory("AK47")
                else:
                    print("You don't have enough money!")
            if question == "dagger":
                if inventory["Baguette"] >= 10:
                    print("You just got a dagger.")
                    addInventory("Dagger")
                else:
                    print("Your broke.")
            if question == "rock":
                if inventory["Baguette"] >= 1:
                    print ("You just got a rock.")
                    addInventory("Rock")
                else:
                    print("BRO HOW BROKE ARE YOU")

        if rand == 2:
            question = input("\nYou can purchase a RNG Crate(50 Baguettes)or an RNG rock(25 Baguettes). What do you want to buy?").lower()
            if question == "crate":
                if inventory["Baguette"] >= 50:
                    print ("You just got a RNG Crate!")
                    addInventory("rngCrate")
                    time.sleep(1)
                    print("Opening crate...")
                    rand = random.randint(1,4)
                    if rand == 1:
                        print("You got a bunch of baguettes!")
                        inventory["Baguette"] += 50
                    if rand == 2:
                        print("You just got.... nothing...")
                    if rand == 3:
                        print("You just got a banana! This banana is powerful, and can give you +1000 health!")
                        health += 1000
                    if rand == 4:
                        print("You just got.... nothing...")
                else:
                    print("You don't have enough money!")
            if question == "gun":
                if inventory["Baguette"] >= 25:
                    print("You just got a RNG Flintlock!")
                    addInventory("rngGun")
                else:
                    print("Your broke.")


massMurders = 9


def zombTurn(chealth):
    rand = random.randint (1,20)

    print ("\nThe enemy has attacked! You lost "+ str (rand) +" health!")
    chealth = chealth - rand
    print ("\nYou now have "+ str (chealth) +" health.")
    return chealth
##############
zombheal = 120
##############
def bigboi():
    global health
    rand = random.randint (45,85)
    bosshp = 350
    while True:
        bosshp = playerturn(bosshp)
        health -= rand 
        if bosshp <= 0:
            print ("You killed some random guy on the street! you are sooooo kind :)")
            return True
        if health <= 0:
            print ("YOU SUCK BUDDY GET BETTER HSADFATCHEREURYES")
            return False
        print ("BigBoi has attacked! He did " + str (rand) + "damage!")
        time.sleep(0.8)
        print (" You now have "+ str (health) + " health.")




def Inventory():
    for item in inventory:
        if inventory [item] != 0:
            print("\t" + item + ": " + str (inventory [item]))

        

    
print("Choose your first item.")
time.sleep(0.5)
print ("\nStick or baguette. Choose.")

##########################
question= ""
##########################
health=100
power= 10
##########################
backpack=0
baguette=0
##########################
question=input ("Type item here.\n").lower()
if question=="stick":
    inventory ["Stick"] += 1
    print ("Thats gonna make the French very mad. How dare you.")
if question=="baguette":
    inventory ["Baguette"] += 1
    print ("The french are coming... Maybe because the baguette?")
question = input("Do you want to skip the introduction?\n").lower()
if question == "yes":
    time.sleep(0)
else:
    time.sleep(3)
    print("\n\n\n\nIn this world, Everyone loves baguettes. They love it so much that it is their currency.")
    time.sleep(3)
    print ("\nGold coins? Down the toilet. (I flushed it)")
    time.sleep(0.8)
    print("Cold, hard cash? Nu uh. But wait, isnt it just paper? I still think they hate it.")
    time.sleep(0.8)
    

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nhollup, the french are here.")
time.sleep(0.8)

print("FRENCH: aye. im tired. want a baguette? i have 18180^717389 baguettes in my pocket. just pocket change.")
question=input("YES OR NO\n").lower
if question=="yes":
    inventory [baguette] += 1 
    print ("You now have "+ str (baguette) +" baguette(s).")
    if question =="yes":
        time.sleep(0.8)
        print ("FRENCH: Ya welcome.")
        time.sleep(2)
    if question =="no":
        print ("FRENCH: dang, dats crazy.")
        time.sleep(2)
print ("You walked away.")
time.sleep(0.3)
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(Akward silence)")

##########################
rand = random.randint(1,10)
seconds = 0
##########################

#World 1
while True:
    if massMurders == 10:
        print ("(Thump, Thump, THUMP)")
        time.sleep(0.2)
        print ("BigBoi has appeared!")
        print ("Bigboi is a giant ogre that is VERY strong.\nKill BigBoi to save the town, and for no apparent reason teleport to some other random world.")
        result = bigboi()
        if result ==True:
            print("You killed BigBoi! But now that the village knows you can LITERALLY KILL A GIANT WALKING MAN now they are scared of YOU.")
            massMurders += 1
        if result == False:
            print("You are dead.")
            massMurders -= 1
    if massMurders == 11:
        ("\n Nice job! You have saved the town from the enemies! You will now be teleported to World 2, The Fields.")
        time.sleep (0.5)
        print("\nYou have been teleported to The Fields.")
        break

    else:
        question = input("Do you want to start explore, sleep, or check your inventory?").lower()
        if question == "inventory":
            Inventory()

        if question == "sleep":
            print ("You are asleep. FUN FACT: Loud sounds, or enemies, will wake you up.")
            print("You will gain HP by the second!")
            seconds = 20
            while seconds != 0:
                health += 2
                seconds -= 1
                time.sleep(0.3)
            if rand ==5:
                print ("A loud noise has woken you up. You cannot fall asleep for a couple seconds.")
                time.sleep(2)
                
        if question == "explore":
            print ("You began to explore.")
            time.sleep(0.5)
            rand = random.randint(1,3)
            if rand == 1:
                print("You found a baguette on the floor!")
                inventory ["Baguette"] += 1

            if rand == 2:
                time.sleep(0.3)
                print("You recieved a sword!")
                addInventory("Sword")
            if rand == 3:
                print ("You found a wandering zombie! Do you want to duel it?")
                question = input ("Fight?").lower()
                if question == "yes":
                    result = zombie(health)
                    if result ==True:
                        rand = random.randint(1,4)
                        print ("You won! Nice job!")
                        massMurders += 1
            
                        
                        if rand == 1:
                            time.sleep (0.3)
                            print ("You obtained a baguette!")
                            inventory ["Baguette"] += 1
                            Inventory()
                        if rand == 2:
                            time.sleep (0.3)
                            print ("You obtained a stick!")
                            inventory ["Stick"] += 1
                            Inventory()
                        if rand == 3:
                            time.sleep (0.3)
                            print ("You obtained a dirty rag!")
                            addInventory("Dirty Rag")
                        if rand == 4:
                            time.sleep (0.3)
                            print ("You obtained 14^9 lbs of dirt!")
                            addInventory("Dirt")
                    else:
                        print ("too bad, too sad! cry about it :(\n")
                        print ("Leaving...")
                        time.sleep (0.3)
                        sys.exit

while True:
    question = input("Do you want to explore, sleep, go to the shop, or check your inventory?").lower()
    if question == "inventory":
        Inventory()
    if question == "explore":
        rand=random.randint(1,3)
        if rand > 1:
            print ("You found a baguette.")
            inventory ["Baguette"] +=1
        if rand == 1:
            question = input ("You found a zombie. Do you want to fight?").lower()
            if question == "yes":
                 result = zombie(health)
                 if result ==True:
                    rand = random.randint(1,4)
                    print ("You won! Nice job!")
                    massMurders += 1
                 if result ==False:
                     print("u bad how are you on The Fields and can't beat a ZOMBIE????")
                     sys.exit
    if question == "sleep":
        print ("You are asleep. FUN FACT: Loud sounds, or enemies, will wake you up.")
        print("You will gain HP by the second!")
        seconds = 15
        while seconds != 0:
            health += 2
            seconds -= 1
            time.sleep(0.3)
            if rand ==5:
                print ("A loud noise has woken you up- Now you cannot fall asleep for a couple seconds.").lower()
                time.sleep(2)
    if question == "shop":
        shop(inventory["Baguette"])
