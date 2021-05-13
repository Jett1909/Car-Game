import pygame, time
pygame.init()
gray = (119,118,110)
pygame.display.set_caption('Car Racing Game')
WIDTH = 700
HEIGHT = 900
gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
carImg = pygame.image.load('cars.jpg')

def car(x, y):
    gamedisplay.blit(carImg, (x, y))

def game_loop():
    x = (WIDTH*0.35)
    y = (HEIGHT*0.70)
    x_change = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0  
        
        x += x_change
        gamedisplay.fill(gray)
        car(x, y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
