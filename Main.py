from math import *
from random import randint as rt

import pygame
from pygame import *

pygame.init()


i = 0

# <---SCREEN--->
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Shooter')

# <--_TIME-->
start_ticks=pygame.time.get_ticks()
cooldown = 2000 
# <---IMAGES-->
player = pygame.image.load('player.png')
Bullet_Player = pygame.image.load('001-bullet.png')
bullet_enemy = pygame.image.load('laser.png')
GAME_OVER_SCREEN = pygame.image.load('game_over_screen.png')
number_of_enemies = 3


clock = pygame.time.Clock()

# <---LEVEL-->
level = 1

# <---LEVEL 1 MAP--->

map1 = [
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



# <----LEVEL 2 MAP---->

map2 = [
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0]     
]


current_map = map1

# Enemy Stuff
Enemy_x = rt(1000,1010)
Enemy_y = rt(40,536)

Enemy_x_speed = -2
Enemy_y_speed = 0

# <---CONTROLS--->

# [PLAYERS]
Player_x= 0
Player_y= 268
Player_x_speed = 0
Player_y_speed = 0
lives = 5
timer = 0 

# [BULLET][PLAYER]
Bullet_X_speed = 70
Bullet_X = Player_x
Bullet_Y = Player_y
bullet_state = "Ready"

# [BULLET][ENEMY]
bullet_state_enemy = "Ready"
LASER = pygame.transform.rotate(bullet_enemy, 270)
LASER_LIST = []
LASER_X = []
LASER_Y = []
LASER_SPEED = []
# [ENEMIES]
ENEMY = []
ENEMY_X = []
ENEMY_Y = []
ENEMY_SPEED = []

ENEMY_STATE = "MOVING"

ENEMY_STOP_POS_X = rt(800,900)
ENEMY_STOP_POS_Y = rt(0,536)

last = pygame.time.get_ticks()

for x in range(number_of_enemies):
    ENEMY.append(pygame.image.load("shooter.png"))
    ENEMY_X.append(Enemy_x)
    ENEMY_Y.append(Enemy_y)
    ENEMY_SPEED.append(-5)
    LASER_LIST.append(LASER)
    LASER_X.append(Enemy_x)
    LASER_Y.append(Enemy_y)
    LASER_SPEED.append(-70)







# [SCORE]
score = 0

# [FONTS]
font = pygame.font.Font('freesansbold.ttf',22)

# [GAME OVER SCREEN]
OVER_X = 0
OVER_Y = 0
screen_speed =0


# <---FUNCTIONS--->
def draw(name,x,y):
    screen.blit(name,(x,y))


def show_time():
    seconds = int((pygame.time.get_ticks()-start_ticks)/1000)    
    timer_label = font.render(f"Time: {seconds}", True ,(0,0,0))
    draw(timer_label,890,10)

def check_collision(x1,y1,x2,y2):
    d = sqrt((pow(x2-x1 ,2))+(pow(y2-y1,2)))
    if d < 37:
        return True
    else: 
        return False

def fire_bullet_P1(x,y):
    global bullet_state
    bullet_state = "Fire"    
    draw(Bullet_Player,x+16,y+10)

def fire_bullet_enemy(x,y):
    global bullet_state_enemy
    bullet_state_enemy = "Fire"    
    draw(LASER_LIST[i],x+16,y+10)   

def find_prime():
    num = rt(-10,10)
    for x in range(2,10):
        if num%x==0:
            return False
    else:
        return True

#Draw Text
lives_label = font.render(f"Lives: {str(lives)}",True,(236,47,50))

# Check for Collisions
def checkCollisions1(x_pos, y_pos):
    global lives
    if x_pos <= 160  and x_pos >= 40 and y_pos >= 378:
        return True
    if x_pos <= 160 and x_pos >= 40 and y_pos <= 238:
        return True
    if x_pos >= 210 and x_pos <= 360 and y_pos >= 98 and y_pos <= 399:
        return True
    if Player_x >= 510:
        lives-=0.01
        
    return (x_pos >= 936) or (x_pos < 0) or (y_pos < 0) or ( y_pos >= 536)
    

running = True
while running:
    


   
    pygame.display.flip()
    tileX = 0
    tileY = 0
    tile_dict = {0:pygame.image.load('concrete.png'),1: pygame.image.load("tile.png"),2:pygame.image.load('line.png')}

    #Draw Text
    lives_label = font.render(f"Lives: {str(int(lives))}",True,(236,47,50))
    
    def drawCords(x_pos, y_pos):
        string_x_pos = str(x_pos)
        string_y_pos = str(y_pos)
        cords = font.render(f"{x_pos, y_pos}",1,(0,0,0))
        draw(cords,890,70)
    
    
    #drawing image
    for row in map1:
        for x in row:
            if x == 0:
                draw(tile_dict[0],tileX, tileY)
                tileX += 40
            if x == 1:
                draw(tile_dict[1],tileX,tileY)
                tileX += 40
            if x == 2:
                draw(tile_dict[2],tileX,tileY)
                tileX += 40

        tileX = 0
        tileY += 40 

    # Draw map2
    #for row in map2:
    #    for x in row:
    #        if x==0:
    #            draw(tile_dict[0],tileX, tileY)
    #            tileX += 40
    #        if x == 1:
    #            draw(tile_dict[1],tileX,tileY)
    #            tileX += 40
    #        if x==2:
    #            draw(tile_dct[2],tileX,tileY)
    #            tileX += 40
    #    tileX = 0
    #    tileY += 40
    if lives == 0:
        draw(GAME_OVER_SCREEN,OVER_X,OVER_Y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False


            if event.key == pygame.K_w:
                Player_y_speed=-10
                
            if event.key == pygame.K_a:
                Player_x_speed =-10


            if event.key == pygame.K_s:
                Player_y_speed = 10
                
            if event.key == pygame.K_d:
                Player_x_speed = 10

            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready" :
                    Bullet_X = Player_x
                    Bullet_Y = Player_y
                    fire_bullet_P1(Bullet_X,Bullet_Y)            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                Player_x_speed = 0
                Player_y_speed = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bullet_state == "Ready" :
                Bullet_X = Player_x
                Bullet_Y = Player_y
                fire_bullet_P1(Bullet_X,Bullet_Y) 

 

    # if x_pos <= 160  asnd x_pos >= 40 and y_pos >= 378:
    #     return True
    # if x_pos <= 160 and x_pos >= 40 and y_pos <= 238:
    #     return True
    # if x_pos >= 210 and x_pos <= 360 and y_pos >= 98 and y_pos <= 399:
    #     return True
    # if x_pos >= 510:
    #     return True

    
    
    if checkCollisions1(Player_x, Player_y):
            Player_y -= Player_y_speed
            Player_x -= Player_x_speed
            Player_x_speed = 0
            Player_y_speed = 0

    
    Player_x+=Player_x_speed
    Player_y+=Player_y_speed

    drawCords(Player_x, Player_y)



    if bullet_state == "Fire":
        fire_bullet_P1(Bullet_X,Bullet_Y)
        Bullet_X+=Bullet_X_speed
        bullet_FLIP = False

    if checkCollisions1(Bullet_X,Bullet_Y):
        bullet_state = "Ready"
        Bullet_X = Player_x
    if Bullet_X>=1000:
        bullet_state = "Ready"
        Bullet_X = Player_x
    
    if Player_y>=536:
        Player_y = 536
    if Player_y <0:
        Player_y = 0
    if Player_x>=936:
        Player_x = 936
    if Player_x <=0:
        Player_x = 0
    
    # Moving enemies to a forward position
    if ENEMY_STATE != "STOP":
        for i in range(number_of_enemies):
            LASER_X[i] = ENEMY_X[i]
            LASER_Y[i] = ENEMY_Y[i]
            ENEMY_X[i]+=ENEMY_SPEED[i]
        
            if ENEMY_X[i]<=600:
                ENEMY_X[i] = rt(1000,1010)
                ENEMY_Y[i] = rt(40,536)
            
            if ENEMY_X[i] == ENEMY_STOP_POS_X :
                ENEMY_STATE = "STOP"
        
           
                ENEMY_X[i] = ENEMY_STOP_POS_X

            draw(ENEMY[i],ENEMY_X[i],ENEMY_Y[i])
    #firing of enemy bullets
    for i in range(number_of_enemies):

        if check_collision(Bullet_X,Bullet_Y,ENEMY_X[i],ENEMY_Y[i]) :  
            ENEMY_Y[i] = 2000
            level+=1
        now = pygame.time.get_ticks()
        cooldown=10#rt(500,1000)
        if now - last >= cooldown:
            last = now  

        fire_bullet_enemy(LASER_X[i],LASER_Y[i])      
        LASER_X[i]-=30
         
        if LASER_X[i]<=0:
            bullet_state_enemy = "Ready"
            LASER_X[i]=ENEMY_X[i]
            LASER_Y[i]=ENEMY_Y[i]
            fire_bullet_enemy(LASER_X[i],LASER_Y[i])
        draw(ENEMY[i],ENEMY_X[i],ENEMY_Y[i])


    show_time()
    
    draw(lives_label,890,40)
    draw(player, Player_x, Player_y)
    
    pygame.display.update()
    clock.tick(60)
