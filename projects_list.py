import random
from beginner_projects import beginner_projects_set

high_beginner_projects_set = {'qr code encoder/decoder': 'python modules' , 'binary_search':'code interview ex implementation', 'minesweeper': 'recursion', 'sudoku': 'backtracking, recursion', 'photo manipulation': 'image filters in python', 'markov chain': 'AI', 'pong': 'GUI programming ', 'Connect Four': 'Higher end beginner, numpy, math, pygame, sys', 'Tetris': 'Higher end beginner', 'Web scraping': 'data collection from web pages', 'Bulk file renamer':'pipeline relevance?', 'weather program':'apis', 'discord bot':'discord API, replit IDE'}

#asking for wanted tested topic ( value), given key
#asking for key, removing from set

beginner_projects = beginner_projects_set()
    

class Choose:
    
    def __init__(self):
        self.beginnerproj = beginner_projects()
        self.project_set_choice = int(input("Which project set? Beginner (1) or Intermediate (2)"))

    def choose(self):
        if self.project_choice == 1: #beginner
            action_choice = int(input("Would you like to add or remove a data entry? [1-add,2-remove]"))
            if action_choice == 1:
                pass
            elif action_choice == 2:
                b_pop = str(input("Type the key for the entry you'd like to remove. "))
                b_pop_lowered = b_pop.lower()
                print (b_pop_lowered)
                self.beginner_projects.pop(b_pop_lowered)
        elif self.project_set_choice == 2:
            pass
    


def listing_beginner_projects(self):
    i=0
    print("Beginner Projects")
    for key,value in self.beginner_projects_set.items():
        print("\nBeginner Projects")
        i +=1
        print("Project {}: {}".format(i, key))
        print("Tested topic: {}".format(value))
    print("\n")

def listing_intermediate_projects():
    j=0
    print("Intermediate projects:")

    for key,value in high_beginner_projects_set.items():
        print("\n")
        j +=1
        print("Project {}: {}".format(j, key))
        print("Tested topic: {}".format(value))
    print("\n")

#listing_intermediate_projects()

listing_beginner_projects()
main.choose()


