import random
import time
import sys

# Developed By: Leo Power
# https://powerthecoder.xyz

main_list= []
list_am = input("Enter amount of players: ")
for i in range(int(list_am)):
    name = input("Enter Player Name: ")
    main_list.append(name)

x = 0
while x != 1:
    print()
    amount_per_team = input("Player Per Team: ")
    if(amount_per_team == 0):
        print("Developed By: Leo Power")
        print("https://powerthecoder.xyz")
    elif(amount_per_team < 0):
        print("Shuting Down...")
        time.sleep(1)
        sys.exit()
    else:
        arg = "run"
        if(arg.lower() == "run"):
            print()
            print("Team 1: ")
            print()
            z = 0
            list1 = []
            list2 = []
            while z != int(amount_per_team):
                new_pick = random.choice(main_list)
                if not new_pick in list1:
                    print(f"{new_pick}")
                    list1.append(new_pick)
                    z += 1
                else:
                    pass
            print()
            print("Team 2:")
            print()
            v = 0
            while v != int(amount_per_team):
                new_pick = random.choice(main_list)
                if not new_pick in list2:
                    if not new_pick in list1:
                        print(f"{new_pick}")
                        list2.append(new_pick)
                        v += 1
                    else:
                        pass
                else:
                    pass
            pass