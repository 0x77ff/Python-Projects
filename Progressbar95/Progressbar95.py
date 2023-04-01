import pygame
from pygame import mixer
import random#import libraries
mixer.init()
pygame.init()
pygame.font.init()#activate libraries
background_colour = (77, 81, 87)
# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((750, 750))
# Set the caption of the screen
pygame.display.set_caption('Progressbar95')
# Fill the background colour to the screen
screen.fill(background_colour)
color = (255,0,0)
#text
my_font = pygame.font.SysFont('Comic Sans MS', 16)
#variables
amt=0
oldamt=0
x = 250
y = 250
oldx=0
oldy=0
width = 250
height = 40
x, y = pygame.mouse.get_pos()#x and y pos of mouse to move player
offset=250
offset2=10
widthoffset=20#offsets for bar
DrawNew = False#used to activate drawblue() function

def drawblue():#function to create new blue segment
    global xx
    global rect2
    global yy
    global oldyy
    global speed
    global offset
    speed=random.randint(1,10)
    yy=0
    xx = random.randint(0,500)
    oldyy=0
    rect2 = pygame.draw.rect(screen, (5, 103, 250), (xx,yy, 10, 20))
    
    DrawNew=False

mixer.music.load('E:/Pythonprojects/Projects/Progressbar95/95.mp3')
mixer.music.play(100)#plays music
drawblue()#make a blue when a game starts
running = True
while running:
    pygame.time.wait(10)#fps
    rect5=pygame.draw.rect(screen, (71,123,134), (x+offset2,y+6, width-widthoffset, height-12))#blank part of bar
    rect4=pygame.draw.rect(screen, (5, 103, 250), (x+10,y+6, width-offset, height-12))#blue part of bar
    rect3=pygame.draw.rect(screen, (5, 103, 250), (0,740, 750, 10))#bar at the bottom
    pygame.mouse.set_visible(False)#turn off mouse visible
    oldx,oldy=x,y#saves x,y
    rect1 = pygame.draw.rect(screen, (137, 153, 176), (x,y, width, height),10,5)#player
    text_surface = my_font.render(str(amt)+'%', False, (0, 0, 0))#set up text
    screen.blit(text_surface, (x+115,y+10))  #This takes: window/surface, color, rect 
    pygame.display.update()#updates game display
    pygame.draw.rect(screen, (77,81,87), (oldx,oldy, width, height))#coveres old rect left by player
    x, y = pygame.mouse.get_pos()#set x,y to mouse position
    
    oldamt=amt
    if pygame.Rect.colliderect(rect5, rect2) == True:#if player and blue collide +5 and make new blue
        pygame.draw.rect(screen, (background_colour), (xx,yy, 10, 20))
        rect4 = pygame.draw.rect(screen, (5, 103, 250), (x+10,y+6, width-247.6, height-12))
        amt=amt+5
        offset=offset-11.6#update bar visuals
        offset2=offset2+11.6#update bar visuals
        widthoffset=widthoffset+11.6#update bar visuals
        DrawNew=True
        drawblue()
    else:
        DrawNew=False
    if DrawNew==False:#if they havent collided, move the blue
        oldyy=yy-19+(speed)
        yy+=speed  
        rect2 = pygame.draw.rect(screen, (5, 103, 250), (xx,yy, 10, 20))
        pygame.draw.rect(screen, (background_colour), (xx,oldyy, 10, 20)) 
    if pygame.Rect.colliderect(rect3, rect2) == True:#if blue goes offscreen(Touches bar at bottom) make new blue
        pygame.draw.rect(screen, (background_colour), (xx,yy, 10, 20))
        DrawNew=True
        drawblue()
    if pygame.Rect.colliderect(rect4, rect2) == True :#if Blue touches blue part of bar, make new blue and destroy old blue
       pygame.draw.rect(screen, (background_colour), (xx,yy, 10, 20))
       DrawNew=True
       drawblue()    
    if amt==100:#if bar full, end game
        running=False
                   
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            running = False
pygame.quit()#a=end the game once running=False



                    
