from itertools import combinations
from random import choice
from time import sleep
import os
import pickle


players = []
termine = "y"
number_of_players = 0

while termine == "y":

    name = input("Enter the name of the player : ").title()
    if name in players:
        print("Name already in the list")
    else:
        players.append(name)
    termine = input("Add a player(y/n): ")


match = combinations(players, 2)

matchs = []

a = []
for i in list(match):
    a.append(i)

partie = 1
print("""---------------------------------------------------------------------""")
print(f" We have {len(players)} players")

print("""---------------------------------------------------------------------""")
print("")
print("The computer is ready to draw...")
print("")

sleep(5)

while a is not True:
    if len(a) == 1:
        b = a[0]
        print(f"Match {partie} : {b[0]} vs {b[1]}")
        matchs.append(f"Match {partie} : {b[0]} vs {b[1]}")
        break
    else:
        b = choice(a)
        print(f"Match {partie} : {b[0]} vs {b[1]}")
        print("")
        a.remove(b)
        matchs.append(f"Match {partie} : {b[0]} vs {b[1]}")
        partie += 1
        sleep(2)
print("")
print("""---------------------------------------------------------------------""")
print("Thank you!")
print("")

print(players)

with open("players", "wb") as open_file:
    my_pickler = pickle.Pickler(open_file)
    my_pickler.dump(players)

with open("matchs", "wb") as open_file:
    my_pickler = pickle.Pickler(open_file)
    my_pickler.dump(matchs)


os.system("pause")