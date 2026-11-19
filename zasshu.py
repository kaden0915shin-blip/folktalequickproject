import time
lives = int(3)
def hearts():
    if lives == 3:
        print("You get scratched. (-1 Life, 2/3 remaining)")
        lives -= 1
    elif lives == 2:
        print("You are badly wounded. Consider being more careful (-1 Life, 1/3 Remaining)")
        lives -= 1
    elif lives == 1:
        print("You die. Game over.")
    
print("You see a door blocking your access to a cave")
for i in range(3):
    time.sleep(0.1)
    print(".")
print("You reach into your backpack and pull out a...")
while True: 
    equipment = (input("1: Key, 2: Sword, 3: Torch \n"))
    if equipment in ["1", "2", "3"]:
        break
    else:
        print("Invalid input.")
lives = 3
if equipment == "1":
    print("You unlock the door. Simple.")
if equipment == "2":
    print("You slash the door lock, then kick it down.")
if equipment == "3":
    print("You try to kick the door, burning yourself.")
    hearts()
print("You enter the cave. The way is dark.")
time.sleep(0.5)
if equipment == "3":
    print("Luckily, you have a torch.")
    print("You see a golden key on the ground. You pick it up.")
    superkey = 1
else:
    superkey = 0
    print("You stumble along the cave blindly.")
print("A creature drops from the ceiling, crashing down into the cave. It swings blindly")
for i in range(3):
    time.sleep(0.1)
    print(".")
while True:
    battle1 = (input("Do you: 1: Attack, 2: Run \n"))
    if battle1 in ["1", "2"]:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
if battle1 == "1":
    result = random.randint(1,4)
    if equipment == "2":
        print("Your sword glistens in the light. You aim for it's knee and strike.")
        result += 1
    if result >= 3:
        print("The creature bellows and falls silent")
        print("It drops a potion.")
        potion = 1
    elif result <= 2:
        print("The creature strikes. You fall back, injured")
        hearts()
else:
    print("You run away, dropping your equipment.")
    equipment = 0
for i in range(3):
    time.sleep(0.1)
    print(".")
print("After a while, you reach the end of the cave. Before you stands hundreds of doors.")
print("One of them has a gold key slot, and a note next to it.")
for i in range(3):
    time.sleep(0.1)
    print(".")
if superkey == 1:
    print("You use the golden key to unlock one of the slots. It clicks.")
    time.sleep(0.2)
    print("The door loosens. Solve the puzzle to open it.")
    time.sleep(0.2)
    print("What is tall when it's young, and short when it's old?")
    time.sleep(0.2)
    while True:
        answer = input("Answer: ")
        if answer.lower() == "candle":
            print("The door swings open.")
            break
        else:
            print("An invisible blade falls on you.")
            hearts()
            print("The door remains locked. Try again.")
elif equipment == "2":
    print("You use your sword to begin hacking down doors.")
    time.sleep(0.2)
    print("You sense something...")
    time.sleep(0.2)
    print("The door opens.")
    time.sleep(0.2)
    rage = 1
else:
    print("You start opening doors.")
    print("One of the doors has a monster behind it. It strikes you.")
    hearts()
    print("One of the door opens.")
time.sleep(0.4)
print("The throne room illumnates itself. You see piles of gold everywhere.")
for i in range(3):
    time.sleep(0.1)
    print(".")
print("A giant dragon sits on the throne, staring at you.")
time.sleep(0.4)
dragonhp = 3
if rage == 1:
    print("The dragon sees your sword, and is even angrier.")
    time.sleep(0.4)
    dragonhp = 5
while True:
    pattern = random.randint(1,3)
    luck = random.randint(1,3)
    if equipment == "2":
        luck += 1
    if dragonhp == 0:
        print("The dragon falls, dead.")
        time.sleep(0.4)
        print("You win.")
        exit()
    print("Dragon health is: " + str(dragonhp))
    if pattern == 1:
        print("The dragon charges a fireball.")
        time.sleep(0.4)
        while True:
            battle2 = (input("Do you: 1: Attack, 2: Dodge \n"))
            if battle2 in ["1", "2"]:
                break
            else:
                print("Use numbers.")
        if battle2 == "1" and luck == 1:
            print("You attack the dragon, parrying it's attack.")
            dragonhp -= 1
        if battle2 == "2":
            print("You dodge the attack, the dragon misses, giving you confidence")
            potion += 1
        else:
            print("You are hit.")
            hearts()
    if pattern == 2:
        print("The dragon starts flapping it's wings")
        time.sleep(0.4)
        while True:
            battle2 = (input("Do you: 1: Attack, 2: Dodge \n"))
            if battle2 in ["1", "2"]:
                break
            else:
                print("Use numbers.")
        if battle2 == "1":
            print("You attack the dragon, slashing it.")
            dragonhp -= 2
        if battle2 == "2" and luck == 1:
            print("The dragon soars through the air, missing you and hitting the wall")
            dragonhp -= 1
        else:
            print("The dragon soars past you, healing itself.")
            dragonhp += 1
    if pattern == 3:
        print("The dragon roars, shaking the room. It is preparing to charge.")
        time.sleep(0.4)
        while True:
            battle2 = (input("Do you: 1: Attack, 2: Dodge \n"))
            if battle2 in ["1", "2"]:
                break
            else:
                print("Use numbers.")
        if battle2 == "1" and luck == 1:
            print("You hit the dragon's head, forcing it back.")
            dragonhp -= 2
        if battle2 == "2":
            print("You dodge, barely.")
        else:
            print("The dragon charges, knocking you back.")
            hearts()
    


    try:
        equipment = int(input("1: Key, 2: Sword, 3: Torch \n"))
        break
    except ValueError:
        print("Use numbers.")
if equipment == 1:
    print("You unlock the door. Simple.")
