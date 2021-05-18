import pygame, time
pygame.init()
#MOST IMPORTANT MUSIC
pygame.mixer.music.load('MARIOCART.mp3') #loads the musci file 
pygame.mixer.music.play(0) #plays the music
#set the name of the Game
pygame.display.set_caption('Car Racing Game')
#Size of display screen
WIDTH = 800
HEIGHT = 600
#more variables
CARSPEED = 5
#colours
black = (0, 0, 0)
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
Car_Width = 271

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ( (WIDTH/2), (HEIGHT/2) )
    gamedisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash():
    message_display("YOU CRASHED")

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

    #Crating a loop to check if the X(quit) is pressed and checking if left or right arrow is pressed
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
        background()
        car(x, y)
        #creates the boarder for the road
        if x > 564 or x<150:
            crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
