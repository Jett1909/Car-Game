import pygame, time
pygame.init()
#for the Background colour
gray = (119,118,110)
#set the name of the Game
pygame.display.set_caption('Car Racing Game')
#Size of display screen
WIDTH = 800
HEIGHT = 600
#creating the game display
gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT))
#creates a clock to keep track of the time since the game was opened
clock = pygame.time.Clock()
carImg = pygame.image.load('cars.jpg')

def car(x, y):
    gamedisplay.blit(carImg, (x, y))

def game_loop():
    x = (WIDTH*0.35)
    y = (HEIGHT*0.6)
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
                x_change = -5
                print("left Key pressed")
            if event.key == pygame.K_RIGHT:
                x_change = 5
                print("right key pressed")
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0  
        x += x_change
        #creating a loop to give the game a gray background
        gamedisplay.fill(gray)
        car(x, y)
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
