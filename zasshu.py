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
    try:
        equipment = int(input("1: Key, 2: Sword, 3: Torch \n"))
        break
    except ValueError:
        print("Use numbers.")
if equipment == 1:
    print("You unlock the door. Simple.")