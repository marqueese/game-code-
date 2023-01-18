import random
def battle():

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
 
while battle_continue == True:
    print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
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
battle()