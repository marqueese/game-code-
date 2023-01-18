import random 
import time
import os 

inventory = []
inventory.append("exit")
Locations = ("HMS Albion",'Cape Helles','Aegan sea')
characters = {
    'player':{'name':'Commander','dialogue':[
    "dont let them past this point.",
    'i dont want silence until we have won.'
   ]}
    },
enemy = {
    'enemy':{'name':'General',"dialogue":[
    'lay down your weapons and we may let you live',
    'fight to the last man falls'
    ]}
}

class charachter:
	def __init__(self, name, country, class_):
		self.name = name
		self.country = country
		self.class_ = class_
		self.hp = 100
		self.ammo = 50
		
		def show_info(self):
			print(f'Name: {self.name}')
			print(f'Country: {self.Country}')
			print(f'Class: {self.Class}')
			print(f'HP: {self.hp}')
			print(f'Ammo: {self.ammo}')
			
player = charachter('Whyatt','Australian','Medic')
player.show_info()

with open('letter.txt', 'r') as file:

print("you can visit the shop before deployment")

items = {'bayonette': 10, 'advanced scope': 20, 'extended barrell': 30}
def display_items():
     for item, price in items.items():
        print(f'{item}: ${price}')
def purchase_item(item):
    if item in items:
        price = items[item]
        print(f'you have purchased {item} for ${price}.')
        inventory.append(item)
    else:
      print(f'{item} is not available in this shop.')
display_items()
item = input('enter the name of the item you would like to purchase: ')
purchase_item(item)

print("with your items you can equip them to your weapon \n")

print("would you like to equip weapon modifications")
mods =input('>1 = use mods\n>2 = dont need them')
if mods=="1":
     mods = True
 print("applicable items follow:\n>bayonette\n>advanced scope\n>barrell extension\n>exit")
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

print('heres the plan, find any of these 4 if you get in danger because i will not be leaving the ship')
with open('names.txt', 'r') as file:
print("everyone understand.... good")
print("you leave in 5 hours")
time.sleep(5)

def start_battle():
    
    print("welcome to war, if you die that sucks but ill get over it, Let it begin.")

    def __init__(self, attack_choice):
 
        self.__attack_choice = attack_choice
 
 
    def attack(self):
 
        if self.__attack_choice == 1:
            attack_points = random.randint(8,15)
            return attack_points
 
        elif self.__attack_choice == 2:
            attack_points = random.randint(12,25)
            return attack_points
 
        else:
            print("That is not an option, you forefit your turn")
 
    def heal(self):
 
        heal_points = random.randint(18,25)
        return heal_points    
 
    user_health = 200
    enemy_health = 80
    battle_continue = True
 
    print(characters['player']['name'] + ': ' + characters['player']['dialogue'][0])

    time.sleep(0.5)

    print(characters['player']['name'] + ': ' + characters['player']['dialogue'][1])

    while battle_continue == True:
     print("\nATTACK CHOICES\n1. melee\n2. Single shot\n3. Heal")
    attack_choice = eval(input("\nSelect an attack: "))
  
    if enemy_health == 100:
        enemy_choice = random.randint(1,2)
 
    else:
        enemy_choice = random.randint(1,3)
 
    enemy = battle(enemy_choice)
    user_battle = battle(attack_choice)
 
    if attack_choice == 1 or attack_choice == 2:
        damage_to_enemy = user_battle.attack()
        heal_self = 0
        print("You dealt",damage_to_enemy,"damage.")
 
    if enemy_choice == 1 or enemy_choice ==2:
        damage_to_user = enemy.attack()
        heal_enemy = 0
        print("enemy dealt", damage_to_user, "damage.")
 
    if attack_choice == 3:
        heal_self = user_battle.heal()
        damage_to_enemy = 0
        print("You healed",heal_self,"health points.")
 
    if enemy_choice == 3:
        heal_enemy = enemy.heal()
        damage_to_user = 0
        print("enemy healed", heal_enemy, "health points.")
 
    user_health = user_health - damage_to_user + heal_self
    enemy_health = enemy_health - damage_to_enemy + heal_enemy
 
    if user_health > 100:
        user_health = 100
        
    elif user_health <= 0:
        user_health = 0
        battle_continue = False
 
    if enemy_health > 100:
        enemy_health = 100
 
    elif enemy_health <= 0:
        enemy_health = 0
        battle_continue = False
 
    print("Your current health is", user_health)
    print("enemy's current health is", enemy_health)
 
    print("Your final health is", user_health)
    print("enemy's final health is", enemy_health)
print('we need artillery support, find a radio and call them in')

def Move(map, x, y, items):
    move = ""
    error = 0
    print('you are currently here, %c.\n' % (map[y][x]))
    move = input(' w, a, s, d, if you have ever played a game its quite simple\n')
    if move == 'w':
        y = y -1
    elif move == 's':
        y = y + 1
    elif move == "d":
        x = x + 1
    elif move == "a"
        x = x - 1
    else:
        What = 1
    if (x < 0 or y < 0) or ( x > 3 or y > 3):
        x = 3 if x > 3 else x  
        x = 0 if x > 0 else x  
        y = 3 if y > 3 else y  
        y = 0 if y > 0 else y 
        What = 1
    for i in range(len(items)):
        if x == items[i][0] and y == items [i][1]:
            print("you have found:" + items[i][2])
            inventory.append(items)
            items.pop(i)
            break
    clrscr()
    if error ==1:
        print("THATS A MINEFILED OVER THERE\n")
    Move(map, x , y , items)
print("youve got the radio now call it in here\n")
with open('locations.txt', 'r') as file: