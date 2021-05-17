import pygame, time, os
pygame.init()
#MOST IMPORTANT MUSIC
pygame.mixer.music.load('MARIOCART.mp3')
pygame.mixer.music.play(0)
#for the Background colour
gray = (119,118,110)
#set the name of the Game
pygame.display.set_caption('Car Racing Game')
#Size of display screen
WIDTH = 800
HEIGHT = 600
#more variables
CARSPEED = 5
#creating the game display
gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT))
#creates a clock to keep track of the time since the game was opened
clock = pygame.time.Clock()
carImg = pygame.image.load('RedCar.png')
carImg = pygame.transform.scale(carImg, (95, 189))
carImg = pygame.transform.flip(carImg, False, True)
backGroundPic = pygame.image.load("Grass.jpg")
backGroundPic = pygame.transform.scale(backGroundPic, (136, 273))
Road = pygame.image.load("Road.jpg")
Road = pygame.transform.scale(Road, (600, 900))
Car_Width = 100
def background():
    gamedisplay.blit(backGroundPic, (0, 0))
    gamedisplay.blit(backGroundPic, (0, 200))
    gamedisplay.blit(backGroundPic, (0, 400))
    gamedisplay.blit(backGroundPic, (700, 0))
    gamedisplay.blit(backGroundPic, (700, 200))
    gamedisplay.blit(backGroundPic, (700, 400))
    gamedisplay.blit(Road, (100, -100))
def car(x, y):
    gamedisplay.blit(carImg, (x, y))

def game_loop():
    x = (WIDTH*0.4)
    y = (HEIGHT*0.7)
    x_change = 0
    #call global Variable
    global gray

    #Crating a loop to check if the X(quit) is pressed
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                x_change = -CARSPEED
                print("left Key pressed")
            if event.key == pygame.K_RIGHT:
                x_change = CARSPEED
                print("right key pressed")
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0  
        x += x_change
        #creating a loop to give the game a gray background
        gamedisplay.fill(gray)
        background()
        car(x, y)
        if x > 690-Car_Width or x<110:
            bumped = True
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
