import random
import json

beginner_projects_set = {'countdown timer':' while loops', 'password generator': 'for loops', 'random cooking decisions': 'random', 'tic-tac-toe': 'time,math, recursive decision making algorithm(minimab_set)', 'Snake!': 'Object Oriented Programming'}

#intermediate_projects_set = {'qr code encoder/decoder': 'python modules' , 'binary_search':'code interview eb_set implementation', 'minesweeper': 'recursion', 'sudoku': 'backtracking, recursion', 'photo manipulation': 'image filters in python', 'markov chain': 'AI', 'pong': 'GUI programming ', 'Connect Four': 'Higher end beginner, numpy, math, pygame, sys', 'Tetris': 'Higher end beginner', 'Web scraping': 'data collection from web pages', 'Bulk file renamer':'pipeline relevance?', 'weather program':'apis', 'discord bot':'discord API, replit IDE'}

#i want to test myself on (value),return key
#hook json file onto class
#make sure oop principles are correct, right now the program is eating up all the input and not doing any logic
#understand how to apply oop not in a game sense (find examples)
# allow to put projects in completed category
    

class Main:
    
    def __init__(self,beginner_input):
        self.beginner_input = beginner
        # self.intermediate_projects_set = {'qr code encoder/decoder': 'python modules' , 'binary_search':'code interview eb_set implementation', 'minesweeper': 'recursion', 'sudoku': 'backtracking, recursion', 'photo manipulation': 'image filters in python', 'markov chain': 'AI', 'pong': 'GUI programming ', 'Connect Four': 'Higher end beginner, numpy, math, pygame, sys', 'Tetris': 'Higher end beginner', 'Web scraping': 'data collection from web pages', 'Bulk file renamer':'pipeline relevance?', 'weather program':'apis', 'discord bot':'discord API, replit IDE'}
        self.set_choice = ""
        self.choice = ""
        self.project_set = ""

        
    def update(self):

        set_choice = self.set_choice()
        choice = self.choice()

        if set_choice == "b":
            self.project_set = self.beginner_project_set
            print(self.project_set)
        elif set_choice == "i":
            self.project_set = self.beginner_project_set
            print(self.project_set)


        if choice == "add":
            self.add()
        elif choice == "remove":
            self.remove()
        else:
            self.set_choice()
            self.choice()
    

    def set_choice(self):
        b_i_set = str(input("Which set? beginner [b] or intermediate [i] ? "))
        return b_i_set


    def choice(self):
        add_remove_choice = str(input("Do you want to add [1] or remove [2]? "))
        return add_remove_choice

    def add(self):
        print("adding")
        dict_key_insert = str(input("Insert Key: "))
        dict_value_insert = str(input("Insert Value: "))
        self.project_set[dict_key_insert] = dict_value_insert
        print(self.project_set)


    
    def remove(self):
        print("removing")
        dict_set_key = str(input("What do you want to remove: "))
        del self.project_set[dict_set_key]
        print(self.project_set)


main = Main(beginner_projects_set)
main.update()

# set_choice = str(input("Which set? beginner [b] or intermediate [i] ? "))
# if set_choice == "b":
#     choice = str(input("Do you want to add [1] or remove [2]? "))
#     if choice == "1":
#         print("adding")
#         dict_key_insert = str(input("Insert Key: "))
#         dict_value_insert = str(input("Insert Value: "))
#         beginner_projects_set[dict_key_insert] = dict_value_insert
#         print(beginner_projects_set)

#     elif choice == "2":
#         print("removing")
#         b_set_key = str(input("What do you want to remove: "))
#         del beginner_projects_set[b_set_key]
#         print(beginner_projects_set)
#     else:
#         print("choice error")
# elif set_choice == "i":
#     choice = str(input("Do you want to add or remove? "))
#     if choice == "add":
#         print("adding")
#     elif choice == "remove":
#         print("removing")
#     else:
#         print("choice error")
# else:
#     print("error")






# def listing_beginner_projects(self):
#     i=0
#     print("Beginner Projects")
#     for key,value in self.beginner_projects_set.items():
#         print("\nBeginner Projects")
#         i +=1
#         print("Project {}: {}".format(i, key))
#         print("Tested topic: {}".format(value))
#     print("\n")

# # def listing_intermediate_projects():
#     j=0
#     print("Intermediate projects:")

#     for key,value in high_beginner_projects_set.items():
#         print("\n")
#         j +=1
#         print("Project {}: {}".format(j, key))
#         print("Tested topic: {}".format(value))
#     print("\n")

#listing_intermediate_projects()

# main = Choose()

# listing_beginner_projects()
# main.choose()


