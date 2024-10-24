
import pygame,time,random,sys
from pygame.math import Vector2


#libraries
snake_speed = 15


black = pygame.Color(0,0,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
red = pygame.Color(0,255,0)
green = pygame.Color(100,255,0)

cell_size = 30
number_of_cells = 25

#initialisation
pygame.init()

#initialise game window
pygame.display.set_caption('Snake!')
game_window = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

#fps
fps = pygame.time.Clock()

#snake
snake_position = [100,50]

snake_body = [ [100,50], [90,50], [80,50], [70,50]]

#fruit
fruit_position = [random.randrange(1, (cell_size*number_of_cells//10)) * 10, random.randrange(1,(cell_size*number_of_cells)//10)*10]

fruit_spawn = True

#default orientation
direction = 'RIGHT'
change_to = direction

#score
score = 0

#display
def show_score(choice,color,font,size):
    #set font
    score_font = pygame.font.SysFont(font,size)
    #creating text surface
    score_surface = score_font.render('Score: ' + str(score), True, color)
    #continuously update text surface
    score_rect = score_surface.get_rect()
    #display
    game_window.blit(score_surface, score_rect)

#game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()

    #set position 
    game_over_rect.midtop = (cell_size*number_of_cells/2, cell_size*number_of_cells/4)

    game_window.blit(game_over_surface, game_over_rect)
    #screen.blit(set surface, update method)

    time.sleep(2)
    pygame.quit()
    quit()

class Food:
    def __init__(self):
        self.position = Vector2(5,6)
        
    
    def draw(self):
        #Display surface -> setting blank canvas only one
        #Surface -> many surfaces, output canvas
        #Rects -> manipulation of surface, positioning, collision detection, render(draw)
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(game_window, white, food_rect)
        
food = Food()

#game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'UPDOWN'   
            if event.key == pygame.LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #keys
    if change_to == 'UP' and direction !='DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction !='UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction !='RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction !='LEFT':
        direction = 'RIGHT'    

    
    game_window.fill(green)
    food.draw()

    pygame.display.update()
    fps.tick(60)
        

#snake steps
#food class
#snake class




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
