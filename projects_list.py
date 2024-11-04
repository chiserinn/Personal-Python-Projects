import random
beginner_projects_set = {'countdown timer':' while loops', 'password generator': 'for loops', 'random cooking decisions': 'random', 'tic-tac-toe': 'time,math, recursive decision making algorithm(minimab_set)', 'Snake!': 'Object Oriented Programming'}

high_beginner_projects_set = {'qr code encoder/decoder': 'python modules' , 'binary_search':'code interview eb_set implementation', 'minesweeper': 'recursion', 'sudoku': 'backtracking, recursion', 'photo manipulation': 'image filters in python', 'markov chain': 'AI', 'pong': 'GUI programming ', 'Connect Four': 'Higher end beginner, numpy, math, pygame, sys', 'Tetris': 'Higher end beginner', 'Web scraping': 'data collection from web pages', 'Bulk file renamer':'pipeline relevance?', 'weather program':'apis', 'discord bot':'discord API, replit IDE'}

#i want to test myself on (value),return key
#make sure to remove duplicate code with oop practices
    
print (beginner_projects_set)
set_choice = str(input("Which set? beginner or intermediate? "))
if set_choice == "beginner":
    choice = str(input("Do you want to add or remove? "))
    if choice == "add":
        print("adding")
    elif choice == "remove":
        print("removing")

        #asking for key, removing from set
        b_set = str(input("What do you want to remove "))
        beginner_projects_set.pop(b_set)
        print(beginner_projects_set)#make sure it saves each time
    else:
        print("choice error")
elif set_choice == "intermediate":
    choice = str(input("Do you want to add or remove? "))
    if choice == "add":
        print("adding")
    elif choice == "remove":
        print("removing")
    else:
        print("choice error")

# class Choose:
    
#     def __init__(self):
        
#         self.project_set_choice = int(input("Which project set? Beginner (1) or Intermediate (2)"))

#     def choose(self):
#         if self.project_choice == 1: #beginner
#             action_choice = int(input("Would you like to add or remove a data entry? [1-add,2-remove]"))
#             if action_choice == 1:
#                 pass
#             elif action_choice == 2:
#                 b_pop = str(input("Type the key for the entry you'd like to remove. "))
#                 b_pop_lowered = b_pop.lower()
#                 print (b_pop_lowered)
#                 self.beginner_projects.pop(b_pop_lowered)
#         elif self.project_set_choice == 2:
#             pass
    


# def listing_beginner_projects(self):
#     i=0
#     print("Beginner Projects")
#     for key,value in self.beginner_projects_set.items():
#         print("\nBeginner Projects")
#         i +=1
#         print("Project {}: {}".format(i, key))
#         print("Tested topic: {}".format(value))
#     print("\n")

# def listing_intermediate_projects():
    j=0
    print("Intermediate projects:")

    for key,value in high_beginner_projects_set.items():
        print("\n")
        j +=1
        print("Project {}: {}".format(j, key))
        print("Tested topic: {}".format(value))
    print("\n")

#listing_intermediate_projects()

# main = Choose()

# listing_beginner_projects()
# main.choose()


