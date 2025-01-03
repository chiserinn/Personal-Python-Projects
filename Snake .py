
import pygame,time,random,sys
from pygame.math import Vector2


#libraries
snake_speed = 15


black = pygame.Color(0,0,0)
blue = pygame.Color(0,0,255)
white = pygame.Color(255,255,255)
red = pygame.Color(0,255,0)
green = pygame.Color(100,255,0)

cell_size = 28
number_of_cells = 23
offset = 70

#initialisation
pygame.init()

#initialise game window
pygame.display.set_caption('Snake!')
game_window = pygame.display.set_mode((2*offset + cell_size*number_of_cells, 2*offset + cell_size*number_of_cells))

#fps
fps = pygame.time.Clock()

#snake
snake_position = [100,50]

snake_body = [ [100,50], [90,50], [80,50], [70,50]]


fruit_spawn = True


#score
score = 0


#display
title_font = pygame.font.Font(None,60)
score_font = pygame.font.Font(None,60)

   
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
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)
        
    
    def draw(self):
        #Display surface -> setting blank canvas only one
        #Surface -> many surfaces, output canvas
        #Rects -> manipulation of surface, positioning, collision detection, render(draw)
        food_rect = pygame.Rect(offset + self.position.x * cell_size, offset + self.position.y*cell_size,cell_size,cell_size)
        game_window.blit(food_surface, food_rect)
        #pygame.draw.rect(game_window, white, food_rect)
    
    def generate_random_cell(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x,y)

    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()

        while position in snake_body:
            position = self.generate_random_cell()
            
        return position
        
class Snake:
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False
    
    def draw(self):
        for segment in self.body:
            segment_rect = (offset + segment.x * cell_size, offset + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(game_window, blue, segment_rect, 0, 7)

    def update(self):
        self.body.insert(0,self.body[0] + self.direction)

        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)       

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):

        if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

    def check_collision_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score +=1
        
    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()
    
    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0

    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()

food_surface = pygame.image.load("ree-vector-red-apple-png_1020x.jpg")
game = Game()

SNAKE_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SNAKE_UPDATE, 200)

#game loop
while True:

    for event in pygame.event.get():
        if event.type  == SNAKE_UPDATE:
            game.update()
    
    if event.type == pygame.KEYDOWN:
        if game.state == "STOPPED":
            game.state = "RUNNING"

        if event.key == pygame.K_UP and game.snake.direction != (0,1):
            game.snake.direction = Vector2(0, -1)
        if event.key == pygame.K_DOWN and game.snake.direction != (0,-1):
            game.snake.direction = Vector2(0, 1)
        if event.key == pygame.K_LEFT and game.snake.direction != (1,0):
            game.snake.direction = Vector2(-1, 0)
        if event.key == pygame.K_RIGHT and game.snake.direction != (-1,0):
            game.snake.direction = Vector2(1, 0)
        
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    


    game_window.fill(green)
    pygame.draw.rect(game_window, black, (offset-5, offset-5, cell_size * number_of_cells +10,cell_size * number_of_cells +10), 5)
    game.draw()
    title_surface = title_font.render("Retro Snake", True, black)
    score_surface = score_font.render(str(game.score), True, black)
    game_window.blit(title_surface, (offset - 5, 20))
    game_window.blit(score_surface, (offset-5, offset +cell_size*number_of_cells +10))
    pygame.display.update()
    fps.tick(60)
        

#snake steps
#food class
#snake class



