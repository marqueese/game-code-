inventory = []

mods =input('>1 = use mods\n>2 = dont need them\n')
if mods=="1":
     mods = True
 
while mods == True: 
        print(inventory)
        print("use ****")
        action = input("What do you do?: ").lower().strip()
       
 
        if action == "use bayonette" and ("bayonette") not in inventory:
            print("you do not have this item")
            mods = False
            
        elif action == "use bayonette" and ("bayonette") in inventory:
            print("you " + action)
            inventory.remove("bayonette")
       
        if action == "use barrel extension" and ('barrel extension') not in inventory:
            print("you do not have this item")
            mods = False
            
        elif action == "use barrel extension" and ("barrel extension") in inventory:
            print("you " + action)
            inventory.remove("barrel extension")
        
        if action == "use advanced scope" and ('advanced scope') not in inventory:
            print("you do not have this item")
            mods = False
            
        elif action == "use advanced scope" and ("advanced scope") in inventory:
            print("you " + action)
            inventory.remove("advanced scope")
            
        if action == "use exit" and ('exit') not in inventory:
            print("you do not have this item")
            mods = False
            
        elif action == "exit" and ("exit") in inventory:
            print("you " + action)
            inventory.remove("exit")
            mods = False
            
if mods == "2" :
    print("my god you really like making life hard".upper())