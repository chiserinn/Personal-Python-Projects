import random
import json

beginner_projects_set = {'countdown timer':' while loops', 'password generator': 'for loops', 'random cooking decisions': 'random', 'tic-tac-toe': 'time,math, recursive decision making algorithm(minimab_set)', 'Snake!': 'Object Oriented Programming'}

#hook json class to save info and end the project for now
#for the next version of this project, I want to condense the logic into classes and create more succint code

print(beginner_projects_set)

set_choice = str(input("Which set? beginner [b] or intermediate [i] ? "))
if set_choice == "b":
    choice = str(input("Do you want to add [1] or remove [2]? "))
    if choice == "1":
        print("adding")
        dict_key_insert = str(input("Insert Key: "))
        dict_value_insert = str(input("Insert Value: "))
        beginner_projects_set[dict_key_insert] = dict_value_insert
        print(beginner_projects_set)

    elif choice == "2":
        print("removing")
        b_set_key = str(input("What do you want to remove: "))
        del beginner_projects_set[b_set_key]
        print(beginner_projects_set)
    else:
        print("choice error")
elif set_choice == "i":
    choice = str(input("Do you want to add or remove? "))
    if choice == "add":
        print("adding")
    elif choice == "remove":
        print("removing")
    else:
        print("choice error")
else:
    print("error")




