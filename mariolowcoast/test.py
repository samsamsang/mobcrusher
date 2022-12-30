import  pygame, math, random, os 
from pygame.image import load               ## import des modules de base nécessare au jeu

pygame.init()           ##lancement de pygame


sw=800                  ##définition des dimensions de base de l'écran
sh=600

run=True                ## création des booléens nécessaires à ce jeu
test_mario=True
Playscreen=False
ground= False
t=0

bg=pygame.image.load('blabla.png')  ##import des images et fichiers nécessaires.
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/30),int(arrow.get_height()/30)))
arrow=pygame.transform.rotate(arrow, 90)
Baguette=pygame.image.load('baguette.png')
Baguette=pygame.transform.rotate(Baguette,90)
wheel=pygame.image.load('Settings.png')
bw=bg.get_width()                   ## obtention de la dimension de l'image de base.
bh=bg.get_height()
clock=pygame.time.Clock()           ## céation de la fonction de temps.
a=0                                 ## position de l'image de fond par rapport à l'écran.
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
        self.r=True
        self.jump=1
        self.sumersolt=1
        self.count=1
        self.ground=False
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.center=(self.x,self.y)
    def _velocityxr(self):      ##actions impliquant le petrsonnage
        if self.r==False:
            self.mario_img=pygame.transform.flip(self.mario_img, 1, 0)
            self.r=True
        if self.vx<=5:
            self.vx+=1
    def _velocityxl(self):
        if self.r==True:
            self.mario_img = pygame.transform.flip(self.mario_img, 1, 0)
            self.r=False
        if self.vx>=-5:
            self.vx-=1
    def _brakex(self):
        if self.vx!=0:
            self.vx=0
    def _jump(self):
        self.vy=0
        self.vy-=10
        
    def _ground(self):
        self.ground,self.vy,self.jump,self.sumersolt,self.count=[True,0,1,1,1]
        
        
    def _fall(self):
        self.vy+=0.3
        self.count+=1

    def _draw(self,screen):                             ##apparition de l'image à l'écran
        screen.blit(self.mario_img,self.mario_img_rect)




    def _moveForward(self):         ##actualisation automatique de la postion du personnage en fonction de la vitesse
        self.x += self.vx*0.5
        self.y +=self.vy*0.5
        self.mario_img_rect.center=(self.x,self.y)
class mob_car():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.count=1
        self.ground=False
        self.wallr=False
        self.walll=False
        self.r=True
        self.mobc_img=pygame.image.load('maryo.png')
        self.mobc_img_rect=self.mobc_img.get_rect()
        self.mobc_img_rect.center=(self.x,self.y)
    def _fall(self):
        if self.ground==False:
            self.vy+=0.2
            
    def _ground(self):
        self.ground=True
        if self.vy>0:
            self.vy=0
    def _brakey(self):
        if self.ground==True:
            if self.vy>0:
                self.vy=0
    def _follow(self,t):
        if self.x-mario.x<-5:
            if self.r==False:
                self.mobc_img=pygame.transform.flip(self.mobc_img,1,0)
                self.r=True
            if self.vx<3:
                self.vx+=1
        if self.x-mario.x>5:
            if self.r==True:
                self.mobc_img=pygame.transform.flip(self.mobc_img,1,0)
                self.r=False
            if self.vx>-3:
                self.vx-=1
        if (self.x-mario.x)**2<=25:
            self.vx=0
    def _walk(self,t):
        
        if t%100==0:
            self.mobc_img=pygame.transform.flip(self.mobc_img,1,0)
            self.vx=-self.vx
            self.r= not self.r
    def _brakex(self):
        if self.wallr and self.vx>0:
            self.vx=0
        if self.walll and self.vx<0:
            self.vx=0
    def _moveForward(self):       
        self.x += self.vx*0.5
        self.y +=self.vy*0.5
        self.mobc_img_rect.center=(self.x,self.y)
    def _draw(self,screen):                             
        screen.blit(self.mobc_img,self.mobc_img_rect)
class mob_pain():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.count=1
        self.ground=False
        self.wallr=False
        self.walll=False
        self.r=True
        self.mobp_img=pygame.image.load('maryo.png')
        self.mobp_img_rect=self.mobp_img.get_rect()
        self.mobp_img_rect.center=(self.x,self.y)
    def _fall(self):
        if self.ground==False:
            self.vy+=0.2
    def _ground(self):
        self.ground=True
        if self.vy>0:
            self.vy=0
    def _brakey(self):
        if self.ground==True:
            if self.vy>0:
                self.vy=0
    def _follow(self,t):
        self.count+=1
        self.vx=0
        if self.x-mario.x<0:
            if self.r==False:
                self.mobp_img=pygame.transform.flip(self.mobp_img,1,0)
                self.r=True
        if t%150==0:
            self.vy-=10
        if self.x-mario.x>5:
            if self.r==True:
                self.mobp_img=pygame.transform.flip(self.mobp_img,1,0)
                self.r=False
        
    def _walk(self,t):
        self.count=1
        if self.ground:
            if self.r:
                self.vx=5
            else:
                self.vx=-5
            if t%100==0:
                self.mobp_img=pygame.transform.flip(self.mobp_img,1,0)
                self.vx=-self.vx
                self.r= not self.r
    def _brakex(self):
        if self.wallr and self.vx>0:
            self.vx=0
        if self.walll and self.vx<0:
            self.vx=0
    def _moveForward(self):       
        self.x += self.vx*0.5
        self.y +=self.vy*0.5
        self.mobp_img_rect.center=(self.x,self.y)
    def _draw(self,screen):                             
        screen.blit(self.mobp_img,self.mobp_img_rect)
class bag():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        v=7
        self.paing_img=arrow
        self.paing_img_rect=self.paing_img.get_rect()
        self.paing_img_rect.center=(self.x,self.y)
        if self.x-mario.x<0:
            self.vx=v
        else:
            self.vx=-v
    def _moveForward(self):
        self.x+=self.vx
        self.paing_img_rect.center=(self.x,self.y)
    def _draw(self,screen):
        screen.blit(self.paing_img,self.paing_img_rect)
    





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
car=mob_car(100,50)
pain=mob_pain(200,50)
object=[mario,car,pain]
mob=[pain,car]
paing=[pain]
baguette=[]
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
        car._moveForward()
        pain._moveForward()
        pain._draw(screen)
        for o in baguette:
            o._moveForward()
            o._draw(screen)
        t+=1
        
        car._draw(screen)
        pygame.display.flip()
        keys=pygame.key.get_pressed() ## c'est une fonction qui verifie si une clé est pressée, on puet, en appelant précisement un clé, la faire renvoyer un booléen
        if keys[pygame.K_RIGHT] and a>= 800-bw:##mouvmeent du personnage de gauche à droite.
            
            mario._velocityxr()
            pygame.display.update()
        elif keys[pygame.K_LEFT] and a<= 5:
            
            mario._velocityxl()
    
    
        else:
            mario._brakex()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] : ## mise en place du saut
            if mario.ground==True and mario.jump>0:
                mario.y-=10
                mario._jump()
                mario.jump-=1
            elif mario.ground==False and mario.sumersolt>0 and mario.count>30:
                mario._jump()
                mario.sumersolt-=1
        for o in object:   
            if  o.ground==False:      ##definition du sol et des fonctions nécessaires a la chute et au saut
                o._fall()
            if o.y<470:
                o.ground= False
            else:
            
                o._ground()
        for i,o in enumerate(mob) :
            if (o.x-mario.x)**2<=20000:
                o._follow(t)
            else:
                o._walk(t)
        for o in paing:
            if o.count%60==0:
                baguette.append(bag(o.x,o.y))

 

        
