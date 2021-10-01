import json
from math import *
import sys
from os import write
from random import randint as rt
import pygame

pygame.init()

i = 0
user_text=''
# GAME DATA.
data = {
    "life": 150,
    "ammo": 10,
    'hunger': 100
}

# ACCOUNT DETAILS
account= {
    "Name": user_text
}

# LOADING THE DATA

try:
    with open("Game_Data.json") as game_data_file:
        data = json.load(game_data_file)
    if data["life"] <= 0:
        data["life"]=150
        data["hunger"] = 100
    elif data["ammo"]<=0:
        data["ammo"] = 100
    elif data["hunger"]<=0:
        data["hunger"] = 100
        data["life"] =150
except:
    print("Error")



# <---SCREEN--->
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Shooter')
pygame.display.set_icon(pygame.image.load('aggro.png'))
# <--_TIME-->
start_ticks=pygame.time.get_ticks()
cooldown = 2000 
# <---IMAGES-->
player = pygame.image.load('player.png')
Bullet_Player = pygame.image.load('001-bullet.png')
bullet_enemy = pygame.image.load('bullet (1).png')
Shield = pygame.image.load('002-shield.png')
game_over_screen = pygame.image.load('game_over_screen.png')
amo = pygame.image.load('bullet.png')
number_of_enemies = 5


clock = pygame.time.Clock()

# <---LEVEL-->
level = 1

# <---LEVEL 1 MAP--->

map1 = [
    [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1] 
]



# <----LEVEL 2 MAP---->

map2 = [
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0], 
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0],
    [2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0]     
]


current_map = map1


# Amo Stuff
amo_x = 200
amo_y = rt(50,500)
amo_activate = False

# Sheild stuff
Shield_x = 390
Shield_y = rt(60,500)
shield_strenght = 0    
shield_activate = False

# Enemy Stuff
Enemy_x = rt(1000,1010)
Enemy_y = rt(40,536)

Enemy_x_speed = -2
Enemy_y_speed = 0

# <---CONTROLS--->

# [PLAYERS]
Player_x= 40
Player_y= 268
Player_x_speed = 0
Player_y_speed = 0
lives = 5
timer = 0 
moving = False


# [BULLET][PLAYER]
Bullet_X_speed = 70
Bullet_X = Player_x
Bullet_Y = Player_y
bullet_state = "Ready"

bullet_damage = 1

# [BULLET][ENEMY]
bullet_state_enemy = "Ready"
LASER = pygame.transform.rotate(bullet_enemy, 90)
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



# [HEALTHBAR]
bar_width = 100
green_bar = pygame.Rect(890,40,200,20)
damage_speed = 0.01

# [MOUSE]
pygame.mouse.set_visible(False)
mouse = pygame.image.load("crosshair.png")

# [CRATE]

items = {
    0: "Food",
    1: "Ammo",
    2: "Health"
}


crate_x = rt(0,550)
crate_y = rt(0,536)

shield_on = False

# <---FUNCTIONS--->

def draw(name,x,y):
    screen.blit(name,(x,y))

def drawing_bg(map1):
    global tileX,tileY
    tileX = 0
    tileY = 0
    tile_dict = {0:pygame.image.load('concrete.png'),1: pygame.image.load("tile.png"),2:pygame.image.load('line.png')}
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

    
def end_game():
    global screen_speed,OVER_Y,GAME_OVER_SCREEN

    draw(game_over_screen,0,0)


def show_lives():
    global damage_speed
    pygame.draw.rect(screen,(40,40,40),[20,10,150,20])
    pygame.draw.rect(screen,(240,60,69),[20,10,data["life"],20]) 
    pygame.draw.rect(screen,(40,40,40),[20,10,150,20],3)
    draw(pygame.image.load('001-heart.png'),0,3)
    
    if data["life"] <=0:
        damage_speed = 0

def show_ammo():
    global data
    pygame.draw.rect(screen,(40,40,40),[890,45,100,20])
    pygame.draw.rect(screen,(226,193,5),[890,45,data["ammo"],20]) 
    pygame.draw.rect(screen,(40,40,40),[890,45,100,20],3)
    draw(pygame.image.load('bullet.png'),865,36)

def show_hunger_level():
    global data
    pygame.draw.rect(screen,(40,40,40),[890,10,100,20])
    pygame.draw.rect(screen,(215,127,74),[890,10,data["hunger"],20]) 
    pygame.draw.rect(screen,(40,40,40),[890,10,100,20],3)
    draw(pygame.image.load('meat.png'),868,3)
    

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
    

def enemy_firing():
    global score,bullet_state_enemy,data,number_of_enemies, shield_activate, shield_strenght
    for i in range(number_of_enemies):

        if check_collision(Bullet_X,Bullet_Y,ENEMY_X[i],ENEMY_Y[i]) :  
            ENEMY_Y[i] = 2000
            score+=1
        

   


        fire_bullet_enemy(LASER_X[i],LASER_Y[i])     
        
        LASER_X[i]-=40
        
        if LASER_X[i]<=0 or checkCollisions1(LASER_X[i],LASER_Y[i]):
            bullet_state_enemy = "Ready"
            LASER_X[i]=ENEMY_X[i]
            LASER_Y[i]=ENEMY_Y[i]
            fire_bullet_enemy(LASER_X[i],LASER_Y[i])
        
        if check_collision(Player_x,Player_y,LASER_X[i],LASER_Y[i]):
            if shield_activate:
                shield_strenght = shield_strenght + 1
                if shield_strenght >= 6:
                    shield_activate = False
            
            if not shield_activate:
             damage_speed = 0.5
             data["life"]-=damage_speed
            

        draw(ENEMY[i],ENEMY_X[i],ENEMY_Y[i])

def moving_enemy():
    global ENEMY_STATE
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

# Check for Collisions
def checkCollisions1(x_pos, y_pos):
    global data,damage_speed
    if x_pos <= 160  and x_pos >= 40 and y_pos >= 390:
        return True
    if x_pos <= 160 and x_pos >= 40 and y_pos <= 238:
        return True
    if x_pos >= 210 and x_pos <= 360 and y_pos >= 98 and y_pos <= 399:
        return True
    if Player_x >= 510 and Player_x<=550:
        data["life"]-=0.02
        
    return (x_pos >= 936) or (x_pos < 0) or (y_pos < 0) or ( y_pos >= 536)

def shield_collision(Shield_x, Shield_y, Player_x, Player_y,shield_activate):
    if shield_activate:
        return False
    if check_collision(Shield_x, Shield_y, Player_x, Player_y):
        return True
    else:
        return False

def write(n,x,y):
    stuff = font.render(n,True,(255,255,255))
    draw(stuff,x,y)

def let_player_proceed():
    map1[6][14]=1 
    map1[7][14]=1

def draw_player(name,center):
    screen.blit(name, center)

def click():
    global mouse_click
    if mouse_click == True:
        return True
    else:
        return False


def options():
    global mouse_click,screen
    full_screen_on = False
    running1 = True
    while running1:
        mouse_x,mouse_y = pygame.mouse.get_pos()
        draw(pygame.image.load('bg_2.png'),0,0)
        back_button = pygame.Rect(0,550,200,50)
        fullescreen_button = pygame.Rect(400,275,200,50)
        draw(pygame.image.load('back_button.png'),0,550)
        draw(pygame.image.load('off.png'),400,275)
        if back_button.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('back_button2.png'),0,550)
            if click():
                running1 = False
        if fullescreen_button.collidepoint((mouse_x,mouse_y)):
            if click():
                full_screen_on = True
                if full_screen_on == True:
                    screen = pygame.display.set_mode((screen.get_width(),screen.get_height()),pygame.FULLSCREEN)
                    draw(pygame.image.load('on.png'),400,275)
   
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:

                sys.exit()
 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False
        
        if full_screen_on == True:
            draw(pygame.image.load('on.png'),400,275)
        else:
            draw(pygame.image.load('off.png'),400,275)
 
                    
                   
        pygame.display.update()



def account(user_text):
    global mouse_click,running

    running1 = True
    font = pygame.font.Font(None,32)
    text_box = pygame.Rect(500,284,220,32)
    mouse_x,mouse_y = pygame.mouse.get_pos()
    while running1:
        mouse_click = False
        draw(pygame.image.load('Account_id.png'),250,150)
      
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            if ev.type == pygame.KEYDOWN:
       
                if ev.key == pygame.K_BACKSPACE:
                    user_text=user_text[0:-1]
                else:
                    user_text += ev.unicode
      
            
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False
   
            if click():
                running1 = False
                




        user_name = font.render(user_text,True,(40,40,40))

        screen.blit(user_name,(500,290))
        pygame.display.update()
  

def show_menu():
    global running,mouse_click,user_text,account
    pygame.mouse.set_visible(True)
    running1 = True
    button_1 = pygame.Rect(400,275,200,50)
    button_2 = pygame.Rect(400,395,200,50)
    button_3 = pygame.Rect(400,335,200,50)
    button_stats = pygame.Rect(890,55,100,100)
    button_account = pygame.Rect(0,500,100,100)
    while running1:
        draw(pygame.image.load('bg_1.png'),0,0)
        draw(pygame.image.load('start button.png'),400,275)
        draw(pygame.image.load('exit_button.png'),400,395)
        draw(pygame.image.load('Options.png'),400,335)
        draw(pygame.image.load('account.png'),0,500)
        draw(pygame.image.load('stats.png'),890,55)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if button_1.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('start button-2.png'),400,275)
            if click():
                running = True
                running1 = False
                mouse_click = False
                
    
        if button_2.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('exit.png'),400,395)
            if click():

                sys.exit()

        if button_3.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('Options2.png'),400,335)
            if click():
       
        
                options()

        if button_account.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('account_2.png'),0,500)
            if click():
       
        
                account(user_text)
        
        if button_stats.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('stats_2.png'),890,55)


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
   
                running1 = False

                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False

        
        
        pygame.display.update()
            
    


# monitor_size = [pygame.display.Info().current.w,pygame.display.Info().current.h]

mouse_click = False
full_screen_on = False
running = False

show_menu()
while running:
   
    mouse_x,mouse_y = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    stuff = rt(0,2)
    

  
    # DRAWING TILE MAP
    drawing_bg(map1)
    seconds = int((pygame.time.get_ticks()-start_ticks)/1000) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Game_Data.json','w') as game_data_file:
                json.dump(data,game_data_file)

            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                

                running = False
                sys.exit()


            if event.key == pygame.K_w:
                Player_y_speed=-10
                moving = True
            if event.key == pygame.K_a:
                Player_x_speed =-10
                moving = True

            if event.key == pygame.K_s:
                Player_y_speed = 10
                moving = True
            if event.key == pygame.K_d:
                Player_x_speed = 10
                moving = True
            if event.key == pygame.K_UP:
                Player_y_speed = -10
                moving = True
            if event.key == pygame.K_DOWN:
                Player_y_speed = 10
                moving = True
            if event.key == pygame.K_LEFT:
                Player_x_speed = -10
                moving = True
            if event.key == pygame.K_RIGHT:
                Player_x_speed = 10
                moving = True
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready" :
                    Bullet_X = Player_x
                    Bullet_Y = Player_y
                    fire_bullet_P1(Bullet_X,Bullet_Y)
                        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN:
                Player_x_speed = 0
                Player_y_speed = 0
                moving = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bullet_state == "Ready" :
                Bullet_X = Player_x
                Bullet_Y = Player_y
                fire_bullet_P1(Bullet_X,Bullet_Y) 



    Player_x+=Player_x_speed
    Player_y+=Player_y_speed


    if checkCollisions1(Player_x, Player_y):
            Player_y -= Player_y_speed
            Player_x -= Player_x_speed
            Player_x_speed = 0
            Player_y_speed = 0

    if bullet_state == "Fire":
        fire_bullet_P1(Bullet_X,Bullet_Y)
        Bullet_X+=Bullet_X_speed
        data["ammo"] -=bullet_damage
        bullet_FLIP = False

    if checkCollisions1(Bullet_X,Bullet_Y):
        bullet_state = "Ready"
        Bullet_X = Player_x
    if Bullet_X>=1000:
        bullet_state = "Ready"
        Bullet_X = Player_x
    
    if check_collision(Player_x,Player_y,crate_x,crate_y):
        crate_x = rt(0,550)
        crate_y = rt(0,536)
        if items[stuff] == "Health":
            shield_on = False
            data["life"]+=20
            write("+20",300,10)

            
        elif items[stuff] == "Ammo":
            shield_on = False
            data["ammo"]+=20
            if bullet_state == "Ready":
                bullet_state = "Fire"
    
            print("You have recieved +2 bullets")

        elif items[stuff] == "Food":
            data["hunger"]+=10
            data["life"]+=5
            print("+10 hunger")
            
    



    if Player_y>=536:
        Player_y = 536
    if Player_y <0:
        Player_y = 0
    if Player_x>=936:
        Player_x = 936
    if Player_x <=30:
        Player_x = 30
    

    # if shield_activate:
    #     shield_activate_writing = font.render(f"Shield is activated", 0,(0,0,0)) 
    #     draw(shield_activate_writing,40,40)
        
    
    # if shield_collision(Shield_x, Shield_y, Player_x, Player_y,shield_activate):
    #     shield_activate = True
        
    
    if moving == True and seconds%7 ==0 :
        data['hunger']-=0.05
    elif moving == False:
        data["hunger"]+=0
    

   
   
    # Moving enemies to a forward position
    moving_enemy()
    #firing of enemy bullets
    enemy_firing()

    show_lives()
    show_ammo()
    show_hunger_level()
    if not amo_activate:
        draw(amo,amo_x,amo_y)
    if not shield_activate: 
        draw(Shield,Shield_x,Shield_y)
    draw(player, Player_x, Player_y)
    draw(mouse,mouse_x,mouse_y)
   

    if data["life"]<=0:
        end_game()
    elif data["ammo"]<=0:
        bullet_state = "Ready"
        data["ammo"] = 0
        
    if data["hunger"] <=0:
        end_game()
    if data["life"]>=150:
        data["life"] =150
    if data["ammo"]>=100:
        data["ammo"]=100
    if data["hunger"]>=100:
        data["hunger"]=100
 
    pygame.display.update()
    clock.tick(60)
