#Buggy version, but has more stuff
import pygame, time, random
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
#images :)
carImg = pygame.image.load('RedCar.png')
carImg = pygame.transform.scale(carImg, (95, 189))
carImg = pygame.transform.flip(carImg, False, True) #flips the car image (it started facing the worng way)
backGroundPic = pygame.image.load("Grass.jpg")
backGroundPic = pygame.transform.scale(backGroundPic, (136, 273)) #size change
Road = pygame.image.load("Road.jpg")
Road = pygame.transform.scale(Road, (600, 900)) #size change
Car_Width = 271
obs = 0

def obstacle(obs_start_x, obs_start_y):
    if obs == 0:
        obs_pic = pygame.image.load("BlackCar.png")
        obs_pic = pygame.transform.scale(obs_pic, (100, 200))
    gamedisplay.blit(obs_pic, (obs_start_x, obs_start_y))


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
    obstacle_speed = 9
    y_change = 0
    obs_start_x = random.randrange(200, (WIDTH - 200) )
    obs_start_y = -750
    obs_width = 95 
    obs_height = 195 
    #Crating a loop to check if the X(quit) is pressed and checking if left or right arrow is pressed
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        background()
        obs_start_y -= (obstacle_speed/4)
        obstacle(obs_start_x, obs_start_y)
        obs_start_y += obstacle_speed
        car(x, y)
        #creates the boarder for the road
        if x > 574 or x<140:
            crash()
        if obs_start_y > HEIGHT:
            obs_start_y = 0 - obs_height
            obs_start_x = random.randrange(170, (WIDTH - 170))
            obs = random.randrange(0, 3)

        if y < obs_start_y + obs_height:
            if x > obs_start_x and x < obs_start_x + obs_width or x + Car_Width < obs_start_x + obs_width:
                crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
