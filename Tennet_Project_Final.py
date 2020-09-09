import time
import random
game_table = [["    "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","10"],
[" 1  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 2  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 3  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 4  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 5  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 6  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 7  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 8  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 9  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
["10  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],]
game_table1 = [["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"],
["___","___", "___", "___","___", "___", "___","___", "___", "___","___","___"]]

print("""~~~~~~~~~~~~~~~~~~~ Welcome to the Battleship Game ~~~~~~~~~~~~~~~~~~
The 5 ships are: Carrier (occupies 5 spaces), Battleship (4), Destroyer (3), 
                 Submarine (3), and Patrol (2)
                 
You have to sink all ships in 15 tries.
""")
def ships_placement(args):
    y=x=int(args[1])+3
    w = random.randint(1, 2)
    control_list=[]
    if w == 1:
        count = 1
        while count < x:
            a = random.randint(1, 10)
            if args=="*5C":
                b=random.randint(1, 5)
            else:
                b = random.randint(1, 6)
            control_list.append(a)
            control_list.append(b)
            for i in range(1, y):
                if game_table1[a-1][b-1] == "___" and game_table1[a][b-1] == "___" and game_table1[a+1][b-1] == "___":
                    b+=1
                    count += 1
                else:
                    count=1
                    control_list=[]
                    break
        a = control_list[0]
        b = control_list[1]
        for i in range(1, y-2):
            ships_index.append(a)
            ships_index.append(b)
            game_table1[a][b] = args
            b += 1
    else:
        count = 1
        while count < x:
            if args=="*5C":
                a=random.randint(1,5)
            else:
                a = random.randint(1, 6)
            b = random.randint(1, 10)
            control_list.append(a)
            control_list.append(b)
            for i in range(1, y):
                if game_table1[a-1][b-1] == "___" and game_table1[a-1][b]== "___" and game_table1[a-1][b+1]== "___" :
                    a+=1
                    count += 1
                else:
                    control_list=[]
                    count=1
                    break
        a = control_list[0]
        b = control_list[1]
        for i in range(1, y-2):
            ships_index.append(a)
            ships_index.append(b)
            game_table1[a][b] = args
            a += 1
    return game_table1

ships_index=[]
ships_placement("*5C")
ships_placement("*4B")
ships_placement("*3D")
ships_placement("*3S")
ships_placement("*2P")

def winning_criteria(args):
    count=0
    for i in args:
        for k in i:
            if k[0]=="*":
                count+=1
    return count

count = winning_criteria(game_table1)

def print_gtable(args):
    for i in args:
        print("\t".expandtabs(30),*i,end="\n"*2)
print_gtable(game_table)
#print_gtable(game_table1)

def last_gametable(args):
    v = 0
    h = 1
    for i in range(args):
        v_index = ships_index[v]
        h_index = ships_index[h]
        game_table[v_index][h_index] = ' ⛴'
        v += 2
        h += 2
    return print_gtable(game_table)

number_of_tries=0
count1=0
control_carrier=0
control_battleship=0
control_destroyer=0
control_submarine=0
control_patrol=0

while number_of_tries<15:
    if count==count1:
        print("Congratulations, You win!!!\nYou destroyed all ships")
        print_gtable(game_table)
        break
    try:
        while True:
            entry=input("\nPlease enter numbers from 1 to 10 first number for vertical, the second for horizontal with a SPACE: ")
            entry = entry.split()
            x=int(entry[0])
            y=int(entry[1])
            if x>10 or x<1 or y>10 or y<1 :
                print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
                continue
            break
    except (IndexError, ValueError):
        print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
        continue
    if game_table[x][y]!="___":
        print("\nPlease be careful!!!\nYou have hit this target before.\nPlease check the coordinates of the target!!!")
        number_of_tries += 1
        print("Remaining try/tries :", 15 - number_of_tries)
        print_gtable(game_table)
        time.sleep(5)
    elif game_table1[x][y][0]=="*":
        print("\n***Congratulations***, You hit the ship!!!\n")
        game_table[x][y]=' ⛴'
        count1+=1
        print_gtable(game_table)
        if game_table1[x][y] == "*5C":
            control_carrier += 1
            if control_carrier == 5:
                print("***Congratulations***, You have sunk my Carrier\n")
        elif game_table1[x][y] == "*4B":
            control_battleship += 1
            if control_battleship == 4:
                print("***Congratulations***, You have sunk my Battleship\n")
        elif game_table1[x][y] == "*3D":
            control_destroyer += 1
            if control_destroyer == 3:
                print("***Congratulations***, You have sunk my Destroyer\n")
        elif game_table1[x][y] == "*3S":
            control_submarine += 1
            if control_submarine == 3:
                print("***Congratulations***, You have sunk my Submarine\n")
        elif game_table1[x][y] == "*2P":
            control_patrol += 1
            if control_patrol == 2:
                print("***Congratulations***, You have sunk my Patrol\n")
    elif game_table[x][y]=="___":
        print("\nSorry, you missed the target!!!")
        game_table[x][y]="X".center(3)
        number_of_tries+=1
        print("Remaining try/tries :", 15 - number_of_tries)
        print_gtable(game_table)
        time.sleep(5)
if number_of_tries==15:
    print("You have used 15 tries and You could not destroy all ships!!!\nYOU LOST!!!\nThis is the gametable where all the ships are placed!!!\n")
    last_gametable(17)