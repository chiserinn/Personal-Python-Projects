
import pygame
import time
import random

#libraries
snake_speed = 15

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
red = pygame.Color(0,255,0)
green = pygame.Color(0,255,0)

#initialisation
pygame.init()

#initialise game window
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

#fps
fps = pygame.time.Clock()









###########################################################################################################################

#Object Oriented Programming Notes

## Object

#class Dog: (CLASS)
#   name = "Erin" (IDENTITY - unique key)
#   type = "poodle" (STATE - attributes, variables)
#   def bite(): (BEHAVIOUR - method)
    # pass

# obj = Dog() (OBJECT)

# def __init__ (self,name):
#    self.name = name
# creates an instance method(called everytime Dog() is called) -> to initialise the object(self) and argument(name) to take the attribute (name)

## Inheritance

# class Dog():
# class Poodle(Dog):
# class Baby_Poodle (Poodle):
# each subsequent class takes the methods and attributes

##Polymorphism 

#class Dog():
# def fight():
#   print ("Ruff")
#class Poodle(Dog):
# def fight():
#   print ("RRRUFF")
# each subsequent class can override existing methods

## Encapsulation

#class Dog():
# def __init__() -> "____" Privated, cannot access/change variables, will raise attribute error when accessed(printed)

###########################################################################################################################
