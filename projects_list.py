import random

beginner_projects_set = {'countdown timer':' while loops', 'password generator': 'for loops', 'random cooking decisions': 'random', 'tic-tac-toe': 'time,math, recursive decision making algorithm(minimax)', 'Snake!': 'Object Oriented Programming'}
high_beginner_projects_set = {'qr code encoder/decoder': 'python modules' , 'binary_search':'code interview ex implementation', 'minesweeper': 'recursion', 'sudoku': 'backtracking, recursion', 'photo manipulation': 'image filters in python', 'markov chain': 'AI', 'pong': 'GUI programming ', 'Connect Four': 'Higher end beginner, numpy, math, pygame, sys', 'Tetris': 'Higher end beginner', 'Web scraping': 'data collection from web pages', 'Bulk file renamer':'pipeline relevance?', 'weather program':'apis', 'discord bot':'discord API, replit IDE'}

#asking for input based on my requirements

class Main():
    ask = Ask()


class Current:

    def __init__ (self, beginner_project_input):
        self.current = {}
        self.beginner_proj = beginner_project_input()

    def Ask(self):
        set_input = input("Which set would you like to take from? B or H?")
        if set_input == "B":
            set_input_pop = input("Which entry would you like to pop? ")
            self.beginner_proj.pop()

    
    

def listing_beginner_projects():
    i=0
    print("Beginner Projects")
    for key,value in beginner_projects_set.items():
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

main = Main(beginner_projects_set, high_beginner_projects_set)