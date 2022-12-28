
import  pygame, math, random, os 
from pygame.image import load               ## import des modules de base nécessare au jeu

pygame.init()           ##lancement de pygame


sw=800                  ##définition des dimensions de base de l'écran
sh=600

run=True                ## création des booléens nécessaires à ce jeu
test_mario=True
Playscreen=False
ground= False
jump=2
sumersolt=2
count=1
bg=pygame.image.load('blabla.png')  ##import des images et fichiers nécessaires.
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/20),int(arrow.get_height()/20)))
arrow=pygame.transform.rotate(arrow, 90)
wheel=pygame.image.load('Settings.png')
bw=bg.get_width()                   ## obtention de la dimension de l'image de base.
bh=bg.get_height()
clock=pygame.time.Clock()           ## céation de la fonction de temps.
a=0                                 ## position du coin de l'image de fond par rapport à l'écran.
b=-bh
pygame.display.set_caption('mariolowcoast')## nom de la fenêtre pygame ouverte
screen=pygame.display.set_mode((sw,sh))
def Screen(a,b):
    screen.blit(bg,(a,b))       ## création de la fenêtre et mise a jour
    pygame.display.update()
a=0
b=600-bh
class maria():                  ## création du personnage
    def __init__(self):         ## paramètres de base du personnage (position, image, vitesse)
        self.x=50
        self.y=50
        self.vx=0
        self.vy=0
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.center=(self.x,self.y)
    def _velocityxr(self):      ##actions impliquant le petrsonnage
        if self.vx<=10:
            self.vx+=1
    def _velocityxl(self):
        if self.vx>=-10:
            self.vx-=1
    def _brakex(self):
        if self.vx!=0:
            self.vx=0
    def _jump(self):
        self.vy=0
        self.vy-=10
        
        
        
    def _fall(self):
        self.vy+=0.2

    def _draw(self,screen):                             ##apparition de l'image à l'écran
        screen.blit(self.mario_img,self.mario_img_rect)




    def _moveForward(self):         ##actualisation automatique de la postion du personnage en fonction de la vitesse
        self.x += self.vx*0.5
        self.y +=self.vy*0.5
        self.mario_img_rect.center=(self.x,self.y)

def Begin():
        screen.blit(bg,(a,b))
        begin = pygame.font.SysFont('franklingothicmedium', 35)
        pygame.draw.rect(screen,(170,170,170),(320,380,170,50))
        textbegin= begin.render('Start',run,(255,255,255),(170,170,170))
        textRectbegin = textbegin.get_rect()
        textRectbegin.center= (400,400)           
        screen.blit(textbegin, textRectbegin)
def gotooption():
    screen.blit(wheel,(50,500))
def gotoacceuil():
    screen.blit(arrow,(35,480))
def Title():
        title = pygame.font.SysFont('franklingothicmedium', 55)
        texttitle = title.render('Maria',run,(255,255,255))
        textRecttitle = texttitle.get_rect()
        textRecttitle.center= (400,250)           
        screen.blit(texttitle, textRecttitle)
def Home():
        
        home = pygame.font.SysFont('franklingothicmedium', 35)
        pygame.draw.rect(screen,(170,170,170),(400,480,170,50))
        texthome= home.render('Home',run,(255,255,255),(170,170,170))
        textRecthome = texthome.get_rect()
        textRecthome.center= (480,500)           
        screen.blit(texthome, textRecthome)
mario=maria()
while  run:
    
    for event in pygame.event.get():   ## là étape TRES IMPORTANTE, il faut absolument définir cette action pour que la fenêtre se ferme.  
        if event.type==pygame.QUIT:
            run=False
    if Playscreen:                      ## définition de l'écran d'accueil
           Begin()
           Title()
           gotooption()
           
           pygame.display.flip()        ## raffraichissement de l'image, cela mets à jours tout ce qui apparait à l'écran.
    elif test_mario:        ##lancement du jeu
        screen.blit(bg,(a,b))
        clock.tick(120)     ##definition de la fréquence de rafraichissement
        mario._moveForward()##mise à jour de la position du personnage principal
        mario._draw(screen)## on dessine mario dans la fenêtre
        pygame.display.flip()
        keys=pygame.key.get_pressed() ## c'est une fonction qui verifie si une clé est pressée, on puet, en appelant précisement un clé, la faire renvoyer un booléen
        if keys[pygame.K_RIGHT] and a>= 800-bw:##mouvmeent du personnage de gauche à droite.
            
            mario._velocityxr()
            pygame.display.update()
        elif keys[pygame.K_LEFT] and a<= 5:
            
            mario._velocityxl()
    
    
        else:
            mario._brakex()
        if keys[pygame.K_SPACE] : ## mise en place du saut
            if ground==True and jump>0:
                mario.y-=10
                mario._jump()
                jump-=1
            elif ground==False and sumersolt>0 and count>30:
                mario._jump()
                sumersolt-=1
            
        if  ground==False:      ##definition du sol et des fonctions nécessaires a la chute et au saut
            mario._fall()
            count+=1
        if mario.y<470:
            ground= False
        else:
            ground= True
            mario.vy=0
            jump=1
            sumersolt=1
            count=1


            
    
            
        
