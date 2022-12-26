import pygame
from sys import exit

#1_création d'une fenêtre
pygame.init() #obligatoire
screen = pygame.display.set_mode((width,height))#création display surface = ce que le joueur va voir
pygame.display.set_caption('Mario') # insertion d'un titre
clock = pygame.time.Clock() #C MAJUSCULE ESSENTIEL __ controle temps et fréquence d'images

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

#convertir les formats d'image plus utilisables par pygame => jeu + rapide
ground_surface = pygame.image.load('ground.png').convert_alpha()

#animation
snail_surface = pygame.image.load('mechant.png')
snail_x_pos = 600 #position par défaut du snail

#rectangles => positionnement précis des surfaces, collisions basiques 
#rectangle permet de positionner précisément une image par exemple bine sur le sol 
player_surf = pygame.image.load('player.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (x,y)) #rectangle dessiné autour de la surface. topleft, bottomright, center, midleft, midbottom, etc...  y = coordonnée du sol pour que le perso soit sur le sol



# faire en sorte que la fenêtre reste ouverte jusqu'à ce qu'on la ferme manuellement
while True: 
    for event in pyagame.event.get(): #obtention des évènements de la file d'attente
        if event.type == pygame.QUIT # revient à fermer la fenêtre 
            pygame.quit() #opposé de pygame.init()
            exit() #permet d'annuler la boucle tant que et donc d'éviter des erreurs dûes à des collisions de méthodes init vs quit
    
    # ATTENTION ORDRE DANS LEQUEL LES IMAGES SONT APPELEES
    screen.blit(test_surface, (0,0)) #intégration de la surface dans la fenêtre, origine du repère en haut à gauche, point placé aux coordonnées données = point haut gauche de notre surface 
    screen.blit(ground_surface, (0,0))
    screen.blit(text_surface, (300, 50))
    snail_x_pos += 1 #permettre au snail de bouger en modifiant sa position. vers la droite: +z, vers la gauche : -z
    if snail_x_pos < -100 ;
    snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250)) #position de$u snail dépend d'une variable
    player_rect += 1 #le perso se dpélace vers la droite
    screen.blit(player_surf, (80, 200))

    pygame.display.update() #faire en sorte que le code run en permanence, draw all elts and update evrything
    clock.tick(60) #60 images/sec (FPS). fréquence maximale
    # pour un jeu + sophistiqué, important d'intégrer une fréquence minimale mais c'est + ardu








