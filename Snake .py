
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


fruit_spawn = True

#default orientation

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
        self.position = self.generate_random_pos()
        
    
    def draw(self):
        #Display surface -> setting blank canvas only one
        #Surface -> many surfaces, output canvas
        #Rects -> manipulation of surface, positioning, collision detection, render(draw)
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y*cell_size,cell_size,cell_size)
        game_window.blit(food_surface, food_rect)
        #pygame.draw.rect(game_window, white, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        position = Vector2(x,y)
        return position
        
class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
    
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(game_window, blue, segment_rect, 0, 7)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0,self.body[0] + self.direction)

food = Food()
food_surface = pygame.image.load("ree-vector-red-apple-png_1020x.jpg")
snake = Snake()


SNAKE_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SNAKE_UPDATE, 200)

#game loop
while True:

    for event in pygame.event.get():
        if event.type  == SNAKE_UPDATE:
            snake.update()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and snake.direction != (0,1):
            snake.direction = Vector2(0, -1)
        if event.key == pygame.K_DOWN and snake.direction != (0,-1):
            snake.direction = Vector2(0, 1)
        if event.key == pygame.K_LEFT and snake.direction != (1,0):
            snake.direction = Vector2(-1, 0)
        if event.key == pygame.K_RIGHT and snake.direction != (-1,0):
            snake.direction = Vector2(1, 0)

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    


    game_window.fill(green)
    food.draw()
    snake.draw()

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
