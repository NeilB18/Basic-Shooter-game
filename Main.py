import pygame
from pygame import *
pygame.init()

# <---SCREEN--->
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Shooter')

# <--_TIME-->
start_ticks=pygame.time.get_ticks()

# <---IMAGES-->
player = pygame.image.load('target-shooter.png')

clock = pygame.time.Clock()

# <---MAP--->

map = [
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0] 
]


# <---CONTROLS--->

# [PLAYERS]
Player_x= 0
Player_y= 268

Player_x_speed = 0
Player_y_speed = 0
lives = 5
timer = 0 

# [FONTS]
font = pygame.font.Font('freesansbold.ttf',22)

# <---FUNCTIONS--->

def draw(name,x,y):
    screen.blit(name,(x,y))


def show_time():
    global seconds
    seconds = int((pygame.time.get_ticks()-start_ticks)/1000)    
    timer_label = font.render(f"Time: {seconds}", True ,(0,0,0))
    draw(timer_label,890,10)

#Draw Text
lives_label = font.render(f"Lives: {str(lives)}",1,(0,0,0))



running = True
while running:

    tileX = 0
    tileY = 0
    tile_dict = {0:pygame.image.load('concrete.png'),1: pygame.image.load("tile.png"),2:pygame.image.load('line.png')}

    #Draw Text
    lives_label = font.render(f"Lives: {str(lives)}",True,(0,0,0))
    
    # drawing image
    for row in map:
        for x in row:
            if x == 0:
                draw(tile_dict[0],tileX,tileY)
                tileX += 40
            if x == 1:
                draw(tile_dict[1],tileX,tileY)
                tileX += 40
            if x == 2:
                draw(tile_dict[2],tileX,tileY)
                tileX += 40
        tileX = 0
        tileY += 40            




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False


            if event.key == pygame.K_w:
                Player_y_speed=-15
            if event.key == pygame.K_a:
                Player_x_speed =-15
            if event.key == pygame.K_s:
                Player_y_speed = 15
            if event.key == pygame.K_d:
                Player_x_speed = 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                Player_x_speed = 0
                Player_y_speed = 0

    Player_y+=Player_y_speed
    Player_x+=Player_x_speed
    

    if Player_y>=536:
        Player_y = 536
    if Player_y <0:
        Player_y = 0
    if Player_x>=936:
        Player_x = 936
    if Player_x <=0:
        Player_x = 0
    
    show_time()
    draw(lives_label,890,40)
    draw(player, Player_x, Player_y)
    pygame.display.update()
    clock.tick(60)

   