import sys, pygame
pygame.init()

size = width, height = 1200, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("fireball.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed) #orgine du repère défini en bas à droite de l'image 
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black) #écran noir lorsqu'on veut faire disparaitre la balle 
    screen.blit(ball, ballrect) #blit => block transfer, copier le contenu d'une surface à une autre, coin haut gauche placé à la localisation donnée 
    pygame.display.flip()

    ##centrer une image 
    ##pic_center = ((SCREEN_WIDTH-pic.get_width())/2,(SCREEN_HEIGHT-pic.get_height())/2) 
    ##pygame.display.flip()
