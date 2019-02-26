from pathlib import Path
import pygame
import time
import random
pygame.init()

display_width = 1600
display_height = 900

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('RPG PyGame Luclys')
clock = pygame.time.Clock()

charImg_forward = pygame.image.load('image/Caracters/$PandaMaru_MV_witch_forward.png')#L45xH48
charImg_leftward = pygame.image.load('image/Caracters/$PandaMaru_MV_witch_leftward.png')#L45xH48
charImg_rightward = pygame.image.load('image/Caracters/$PandaMaru_MV_witch_rightward.png')#L45xH48
charImg_backward = pygame.image.load('image/Caracters/$PandaMaru_MV_witch_backward.png')#L45xH48


CharSpriteTileSet = pygame.image.load("image/Caracters/$PandaMaru_MV_witch.png")
CharSpriteTile = CharSpriteTileSet.subsurface((0,0,45,48))
CharSpriteTile



char_width = 45
char_height = 48
bgImg = pygame.image.load('image/Textures//fond_1_resized.png')#L41xH48
inventory_gui = pygame.image.load('image/Gui/Inventaire_gui.png')
gui_width = 1024
gui_height = 576

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

global facing
facing="undef"

def char(x,y,x_change,y_change):
    global facing
    if y_change > 0:
        facing ='south'
    elif y_change < 0:
        facing ='north'
    elif x_change > 0:
        facing ='east'
    elif x_change < 0:
        facing='west'
    if facing == "north" :
        gameDisplay.blit(charImg_backward,(x,y))
    elif facing == "east" :
        gameDisplay.blit(charImg_rightward,(x,y))
    elif facing == "west" :
        gameDisplay.blit(charImg_leftward,(x,y))
    elif facing == "south" :
        gameDisplay.blit(charImg_forward,(x,y))


  # git config --global user.email "spidloic@outlook.fr"
  # git config --global user.name "Luclys"


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit by User")
                quit()
            if event.type == pygame.KEYUP:
                intro = False

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("RPG PyGame Luclys", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        gameDisplay.blit(CharSpriteTile,(0,0))
        clock.tick(15)

def game_echap_menu():
    echap_menu = True
    print("Echap menu opened.")

    while echap_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Exit by User")
                quit()
            if event.type == pygame.KEYUP:
                if event.key ==  pygame.K_ESCAPE:
                    print("Echap menu closed.")
                    echap_menu = False

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Es-tu sûr de vouloir quitter ?", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(60)


def game_inventory():
    inventory = True
    print("Inventory opened.")

    while inventory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_echap_menu()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e or pygame.K_ESCAPE:
                    print("Inventory closed.")
                    inventory = False

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                print(mouse_x,mouse_y)

                #Clic sur jeter item
                if(1185 <= mouse_x and mouse_x <= 1302 and 623 <= mouse_y and mouse_y <= 730):
                    print("Clic sur la croix pour supprimer l'item")
                    #Action
                #Clic sur vendre l'item
                if(1042  <= mouse_x and mouse_x <= 1152  and 631  <= mouse_y and mouse_y <= 730):
                    print("Clic sur l'étoile pour vendre l'item")
                    #Action
                compteur = 0
                for iy in range(3):
                    for jx in range(4):
                        compteur += 1
                        if(355+140*jx  <= mouse_x and mouse_x <= 475+140*jx  and 300+133*iy  <= mouse_y and mouse_y <= 420+133*iy):
                            print("item n°",compteur)



        gameDisplay.blit(inventory_gui,(display_width/2-gui_width/2,display_height/2-gui_height/2))
        pygame.display.update()
        clock.tick(60)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    obstruction_left = False
    obstruction_up = False
    obstruction_right = False
    obstruction_down = False

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_echap_menu()
            if event.type == pygame.KEYDOWN:
                #Handle 4-way movement
                if event.key == pygame.K_LEFT or event.dict['unicode'] == 'q':
                    if not obstruction_left:
                        x_change = -5
                if event.key == pygame.K_RIGHT or event.dict['unicode'] == 'd':
                    if not obstruction_right:
                        x_change = 5
                if event.key == pygame.K_UP or event.dict['unicode'] == 'z':
                    if not obstruction_up:
                        y_change = -5
                if event.key == pygame.K_DOWN or event.dict['unicode'] == 's':
                    if not obstruction_down:
                        y_change = 5


            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_a,pygame.K_q,pygame.K_d):
                    x_change = 0
                if event.key in (pygame.K_UP,pygame.K_DOWN,pygame.K_w,pygame.K_z,pygame.K_s):
                    y_change = 0
                if event.key == pygame.K_e:
                    game_inventory()
                if event.key == pygame.K_ESCAPE:
                    game_echap_menu()

        x += x_change
        y += y_change

        gameDisplay.blit(bgImg,(0,0))
        char(x,y,x_change,y_change)

        #Handle the obstruction : wether or not the character can move that way
        if x >= display_width - char_width:
            x_change = 0
            obstruction_right = True
        else:
            obstruction_right = False
        if x <= 0:
            x_change = 0
            obstruction_left= True
        else:
            obstruction_left = False
        if y >= display_height - char_height:
            y_change = 0
            obstruction_down = True
        else:
            obstruction_down = False
        if y <= 0:
            y_change = 0
            obstruction_up = True
        else:
            obstruction_up = False


        #Sert à checker s'il y a une collision avec des coordonnées thingX, thingX
        # if y < thing_starty+thing_height:
        #     print('y crossover')
        #
        #     if thingX < x+char_width and thingX+thingW > x:
        #         print('x crossover')
        #         crash()

        pygame.display.update()
        clock.tick(60) #60fps

game_intro()
game_loop()
pygame.quit()
quit()
