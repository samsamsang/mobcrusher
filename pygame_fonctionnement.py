#https://www.youtube.com/watch?v=AY9MnQ4x3zk, très bien expliqué et very complet!!
# parties pas regardées : 1h23-1h29 (coloriage de rectangles et autres figures)
# j'ai regardé jusque 2h23

import pygame
from sys import exit

#score 
def display_score(): #score dépendant du temps en vie 
    current_time = int(pygame.time.get_ticks()/1000) - start_time #temps donné en ms
    score_surf_b = test_font.render(f'Score: {current time}', False, (64, 64, 64)) #création d'une surface avec un texte
    score_rect_b = score_surf.get_rect(center = (400, 50)) #rectangulation de la surface 
    screen.blit(score_surf_b, score_rect_b)
    return current_time #current_time accessible à n'importe quel moment


#1_création d'une fenêtre
pygame.init() #obligatoire
screen = pygame.display.set_mode((width = 800,height = 400))#création display surface = ce que le joueur va voir
pygame.display.set_caption('Mario') # insertion d'un titre
clock = pygame.time.Clock() #C MAJUSCULE ESSENTIEL __ controle temps et fréquence d'images
#test_font()
game_active = True 
start_time = 0 
score = 0

#2_affichage de surfaces
# deux types de surface: display surface (fenetre, unique) et regular surface (image singulière, doit être intégrée sur la fenetre pour etre visible) 
#surface colorée
test_surface = pygame.Surface((w,h)) #S MAJUSCULE __ insertion surface plane de couleur
test_surface.fill('Red') #colorer la surface

#importer une image
test_surface_bis=pygame.image.load('nom_image.png + chemin d_accès si le dossier n_est pas importé')
ground_surface = pygame.image.load('ground.png')

#surface avec texte pour insérer un texte
test_font = pygame.font.Font('font type', police)#choix d'une police + taille, fichier ttf spécifie une police
text_surface = test_font.render('text', AA = booléen, color) # AA ==> anticrénelage

score_surf = test_font.render('My game', False, 'black')
score_rect = score_surf.get_rect(center = (400, 50))


#convertir les formats d'image plus utilisables par pygame => jeu + rapide
ground_surface = pygame.image.load('ground.png').convert_alpha()

#animation
snail_surface = pygame.image.load('mechant.png')
##snail_x_pos = 600 #position par défaut du snail
snail_rect = snail_surface.get_rect(bottomright, (600, 300))

#rectangles => positionnement précis des surfaces, collisions basiques 
#rectangle permet de positionner précisément une image par exemple bine sur le sol 
player_surf = pygame.image.load('player.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (x,y)) #rectangle dessiné autour de la surface. topleft, bottomright, center, midleft, midbottom, etc...  y = coordonnée du sol pour que le perso soit sur le sol
player_gravity = 0 #valeur par défaut

#surface d'introduction
player_stand = pygame.image.load('nom_image.png').convert_alpha()
player_stand= pygame.transform.rotozoom (image modifiée = player_stand, angle de rotation = 0, taille multipliée par = 2) #création d'une surface
player_stand_rect = player_stand.get_rect(center = (80, 300)) 

#création nouvelle variable avec le nom du jeu 
game_name = test_font.render(nom_jeu = 'PixelRunner', False, (111, 196, 230)) #surface de texte avec le nom du jeu
game_name_rect = game_name.getèrect(center = (400, 130))


#création nouvelle variable texte avec instruction du jeu 
game_message = test_font.render('Press space to run', False, (111, 196, 230))
game_message_rect = game_message.get_rect(center = (400, 330)) #y identique à celui de score_message



# faire en sorte que la fenêtre reste ouverte jusqu'à ce qu'on la ferme manuellement
while True: 
    for event in pygame.event.get(): #obtention des évènements de la file d'attente
        if event.type == pygame.QUIT # revient à fermer la fenêtre 
            pygame.quit() #opposé de pygame.init()
            exit() #permet d'annuler la boucle tant que et donc d'éviter des erreurs dûes à des collisions de méthodes init vs quit
    if game_active:
        #utilisation souris 
        if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
    
        #utilisation du clavier ou l.92-95
        if event.type == pygame.KEYDOWN: #bouton pressé, KEYUP ==> bouton relaché
            if event.type == pygame.K_SPACE and player_rect.bottom >= 300: #ne faire sauter le player que s'il touche le sol
                player_gravity = -20 #saut 


        # ATTENTION ORDRE DANS LEQUEL LES IMAGES SONT APPELEES
        screen.blit(test_surface, (0,0)) #intégration de la surface dans la fenêtre, origine du repère en haut à gauche, point placé aux coordonnées données = point haut gauche de notre surface 
        screen.blit(ground_surface, (0,300))
        pygame.draw.rect(surface = screen, couleur = 'Pink', rectangle colorié = score_rect, distance au centre pas colorié, largeur de la bordure) #faire un fond sur le rcetangle de texte
        screen.blit(score_surf, score_rect)
        score = display_score()


        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        
        snail_x_pos += 1 #permettre au snail de bouger en modifiant sa position. vers la droite: +z, vers la gauche : -z
        if snail_x_pos < -100;
            snail_x_pos = 800
        screen.blit(snail_surface, (snail_x_pos, 250)) #position de$u snail dépend d'une variable
        #ou
        #screen.blit(snail_surface, snail_rect) # position du snail dépendant du rectangle, plus concis que version avec snail_x_pos 
        


        #player_rect += 1 #le perso se dpélace vers la droite
        #screen.blit(player_surf, (80, 200))
        #ou
        player_gravity += 1
        player_rect.y += player_gravity #intégration dans la boucle permet de faire chuter le player de + en + vite 
        if player_rect.bottom >= 300: #300 = coordonnée du sol
            player_rect.bottom = 300 #le player ne peut pas aller en dessosu du sol
        screen.blit(player_surf, player_rect)


        #collision
        #player_rect.colliderect(snail_rect) #pas de collision: renvoie 0, collision: renvoie 1
        if snail_rect.colliderect(player_rect) : #sous-entendu if .. =1
            game_active = False #le jeu ne se ferme pas lors d'une collsion non désirée
    
    else:
        screen.fill((94, 129, 162 )) # intensité des trois couleur primaires 
        screen.blit(player_stand, player_stand_rect) #affichage player
        
        score_message = test_font.render(f'Your score: {score}', false, (111, 169, 196)) #création variable avec le score  
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect) #affichage nom de jeu
        
        # en fonction de si c'est une nouvelle partie ou bien une partie après un échec, on affiche les instructions ou le score
        if score == 0:
            screen.blit(game_message, game_message_rect) #affichage instructions de jeu
        else:
            screen.blit(score_message, score_message_rect)


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            game_active = True 
            snail_rect.left = -20 #permettre que le snail ne touche pas le player dès le retour sur le jeu, sinon échec immédiat 
            start_time = int(pygame.time.get_ticks()/1000) #réinitialisation du score lors d'une nouvelle tentative 
           
            



    #utilisation de la souris 
    mouse_pos = pygame.mouse.get_pos()
    player_rect.collidepoint((x,y)) #vérifier si le point de coord (x,y) est en contact avec le rectangle 
        pygame.mouse.get_pressed() #renvoie un booléen en fonction de si le coté droit/gauche et/ou le centre de la souris est pressé

    #utlisation du clavier
    keys = pygame.key.get_pressed() #renvoie 0 ou 1
    if keys[pygame.K_SPACE]:
        print('jump')

    pygame.display.update() #faire en sorte que le code run en permanence, draw all elts and update evrything
    clock.tick(60) #60 images/sec (FPS). fréquence maximale
    # pour un jeu + sophistiqué, important d'intégrer une fréquence minimale mais c'est + ardu








