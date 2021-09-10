import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1000,600))
def draw(name,x,y):
    global screen
    screen.blit(name,(x,y))
running1 = True
running = False
mouse_click = False
def click():
    global mouse_click
    if mouse_click == True:
        return True
    else:
        return False

def start_game():
    global running,running1,mouse_click
    running = True
    running1 = False
    mouse_click = False

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
    global mouse_click,running,mouse_x,mouse_y
   
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

def show_menu(user_text):
    global running,mouse_click
    pygame.mouse.set_visible(True)
    running1 = True
    
    button_1 = pygame.Rect(400,275,200,50)
    button_2 = pygame.Rect(400,395,200,50)
    button_3 = pygame.Rect(400,335,200,50)
    button_account = pygame.Rect(0,500,100,100)
    while running1:
        draw(pygame.image.load('bg_1.png'),0,0)
        draw(pygame.image.load('start button.png'),400,275)
        draw(pygame.image.load('exit_button.png'),400,395)
        draw(pygame.image.load('Options.png'),400,335)
        draw(pygame.image.load('account.png'),0,500)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if button_1.collidepoint((mouse_x,mouse_y)):
            draw(pygame.image.load('start button-2.png'),400,275)
            if click():
                start_game()

                
    
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


        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
   
                running1 = False

                sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            else:
                mouse_click = False


        
        pygame.display.update()
if running == True:
    running = True