



def addInventory(item):
    if item.lower() in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

inventory = {"baguette": 0, "stick": 0}
list = [1000, "sigma", True]

addInventory("baguette")
addInventory("stick")
print(inventory)
inventory["baguette"] += 1
addInventory("monke")
inventory["monke"] -= 1


for key, value in inventory.items():
    print(key + ": " + str(value))



