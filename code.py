#Pranav Maini
#22/06/17


import random
def story_line():
    """
    Function: story_line
    this function prints the intro to the game and also asks the user if they would like to continue, else, exit program.
    Parameters: None
    """
    print("You are summoned by the gods, and you're given an assignment to save the world! The world is being attacked by 5 mythical creatures and without you, the gods think humanity will not survive any longer. Do you wish to proceed and fight the creatures?")
    print("Welcome to boss battle version 1.0.1\n this is not an ordinary game, mistakes can make you loose all your progress\nInstructions:\n\nYou will be given a new pokemon each level of the game you sucseed. Otherwise, you will have to start from the start, there is a cheatcode option..\nIf you wish to win fast then you may choose that.Oh and! If you wish to win the game with the cheatcode you are able to do so.")    
    #q_continue = input("shall we continue (yes/no): ").lower()
    while True:
        q_continue = input("shall we continue (yes/no): ").lower()
        if q_continue == "yes":
            print("ok, lets continue")
            break
        elif q_continue == "no":
            print("you have exited the game!")
            exit()
        
def name():
    """
    The idea of this function is to retrieve a name offered by us incase a user is very indecisive, after 2 
    invalid attempts it will let them use there own.
    parameters: None
    Return: None
    """
    name_options = ["Big Papa","Cosmo","Mad Dog","K-9"]
    print("Choose your name\n",)
    for i,names in enumerate(name_options):
        print(i+1,")",names)
    name = input("enter one of the following names: ").title()
    counter = 0
    while name not in name_options:
        counter += 1
        name = input("ENTER THE VALID NAME OPTIONS!; ")
        if counter == 2:
            name = input("okay, fine. You can chose your name: ")
            return name
            #find way to print users name!
    return name
name = name()
print("You have selected:", "\"", name, "\"") 

def cheatcode():
    """
    This function gives the key to win!
    Parameters: None
    Return values: None
    """
    acceptable_awnsers = ["yes","no"]
    offer_cheatcode = input("would you like the cheatcode (yes/no)?: ").lower()
    while offer_cheatcode not in acceptable_awnsers:
        offer_cheatcode = input("would you like the cheatcode (yes/no)?: ").lower()
    if offer_cheatcode == "yes":
        print("\nLvl 1: Maximum damage attack: punch hard\nLvl 2: Maximum damage attack: decoy\nLvl 3: Maximum damage attack: claws\nLvl 4: Maximum damage attack: Biggest banana\nLvl 5: Maximum damage attack: Random2 = 1 shot!\n By the way there is a chance you still loose.\n")
        
def boss_battle(boss_name,boss_health,boss_attacks,boss_corresponding_damages,pokemon_name,pokemon_health,pokemon_attacks,pokemon_corresponding_damages):
    """
    This function is the boss fight. The code is the general idea of a boss fight and the parameters
    customize the fights.The boss picks attacks at random, using the random.randint between 0 and 
    the length of attacks, this way its not set to a specifc amount of attacks for player or boss.
    lists were crucial in this code because it helps use index's and identify which attack is what
    and damage.As shown in code we used the the function .index() to locate that specific thing 
    inside that variable, and to store the int which is used later in the code.
    Parameters:
    1) boss_name, this is the name of the boss
    2)boss_health, this is the health of the boss
    3)boss_attacks, the boss attacks, using a list! Which is best because we can use index's and since its alrdy a list its simple.
    4) boss_corresponding_damages, the boss attack damages (int), this also uses a list to correspond with the attacks at the exact index's
    5)pokemon_name, is the pokemon name
    6)pokemon_health, is the pokemon's health
    7) pokemon_attacks, is the attacks availible for the pokemon to use.
    8)pokemon_corresponding_damages, is the corresponding damage for the attack.
    """
    while True: 
        boss_random_attack = random.randint(0,len(boss_attacks)-1) #stores a random value
        boss_damage_choice = boss_corresponding_damages[boss_random_attack] #uses same random value stored, also this is damage
        boss_attack_choice = boss_attacks[boss_random_attack] #uses the same random value stored.
        for i, attacks in enumerate(pokemon_attacks): #this displays users options.
            print(i+1,")",attacks)
        choose_attack = input("please choose a valid attack: ").lower() #takes input for attack 
        while choose_attack not in pokemon_attacks: #invalid responce will trigger while loop.
            choose_attack = input("try again: ").lower()
        index_of_damage_pokemon = pokemon_attacks.index(choose_attack) #using .index() to find index of the attack from the list of pokemon_attacks, which gives us the correct index. len() would work too but index is ideal for this case. with len we'd need to -1.
        damage_results = pokemon_corresponding_damages[index_of_damage_pokemon] #the damage is found by using the index we found earlier and using that as the argument being passed to the list of attack damages, which selects the correct index of that attack.
        boss_health -= damage_results #calculates the health for boss
        pokemon_health -= boss_damage_choice #calculates the health for pokemon
        print("\nPokemon Stats:\nattack:",choose_attack,"\nDamage delt:",damage_results,"\n\nBoss Stats:","\nboss attack:",boss_attack_choice,"\nDamage delt:",boss_damage_choice,"\n\nHealths:","\nHealth of Pokemon:",pokemon_health,"\nHealth of boss:",boss_health,"\n")
        if pokemon_health <= 0 or boss_health <= 0: #determines when to exit loop
          if pokemon_health > boss_health: #determines if pokemon won
                print("You won, good job! The next level will be harder so be prepared!")
                break
          else: #if pokemon did not win then boss won.
            print("You lost, please start again!")
            exit() #and it will exit the program and the user would have to restart! 
            #At first the game was much harder but it let the player retry, but i thought that will get boring since they dont have much to loose and risk brings excitement.
story_line() #calls the function of the storyline
cheatcode() #calls the cheatcode function to offer the user

#theese are how the fights are predetermined. If the user wins, they will have text displayed on the next attack, else in the function of the battles, it will exit if loss.
fight_one = boss_battle("Potato Eater",200,["eat","bite"],[25,30],"Sir Potato",200,["throw potato","punch hard","potato shower"],[25,60,5])
print("Thats how you do it! You have stumbeled across zombie territory, uh oh... This may be tough, but you got this!")
fight_two = boss_battle("Zombie",200,["eat brain","attack","hypnotism"],[30,35,40],"ZombieDestroyer",180,["fight zombie","attack with sword","decoy"],[10,30,45])
print("wow that was incredible! While youre on a roll,This time you\'ve been assigned to fight stray dogs and to protect the citizens of winnipeg")
fight_three = boss_battle("Evill Dog",225,["Woof","bark","super attack"],[10,15,60],"SuperCat",200,["meow","fly and attack","claws"],[35,20,60])
print("This was a tough match! Great job!!! Now youve been assigned in the jungles thousands of kilometers from any people. Gorillas are attacking you, you msut deffend your position!")
fight_four = boss_battle("Angry gorilla",500,["Angry gorilla sounds","Gorilla army","Gorilla attack"],[25,50,75],"Flying Banana",500,["throw banana","throw big banana","biggest banana"],[30,45,60])
print("Incredible! Youve exceeded my expectations, This is the last fight, the boss fight!! You have 6 attacks and one of them is 500 damage! Pick wisely before you die. good luck")
fight_five = boss_battle("Angry gorilla",500,["Belly Flop","Squish","super gorilla punch"],[100,25,75],"Superman",350,["random1","random2","random3","random4","random5","random6"],[20,500,10,25,20,1])
print("Wow, you won! Congratulations, version 1.0.2 coming out soon!") #this only prints if they make it this far
#last print statement is when they win!
