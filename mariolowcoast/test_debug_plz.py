import  pygame, math, random, os, sys
from pygame.image import load               ## import des modules de base nécessare au jeu

pygame.init()           ##lancement de pygame


sw=800                  ##définition des dimensions de base de l'écran
sh=600



bg=pygame.image.load('blabla.png')  ##import des images et fichiers nécessaires.
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/30),int(arrow.get_height()/30)))
arrow=pygame.transform.rotate(arrow, 90)
baguette=pygame.image.load('starbg.png')
baguette=pygame.transform.rotate(baguette,90)
wheel=pygame.image.load('Settings.png')
mario_theme = pygame.mixer.Sound('mario_theme.wav') 
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
class move_screen():
    def __init__(self,a):
        self.a=a
        self.va=0
        self.walll=True
        self.wallr=False
    def _velocityr(self):
        global mario
        if mario.x>=475 :
            if self.a>-11700:
                if self.va>=-5:
                    self.va-=1
                mario._brakex()
            if self.a<=-11700 and mario.x<=780:
                self.a=-11700
                mario._velocityxr()
        elif   not mario.wallr :
            self.va=0
            
            mario._velocityxr()
    def _velocityl(self):
        global mario
        if mario.x<=100 :
            if self.a<0:
                if self.va<=5:
                   self.va+=1
                mario._brakex()
            
            if self.a>=0 and mario.x>=0:
                self.a=0    
                mario._velocityxl()
        elif  not mario.walll :
            self.va=0
            mario._velocityxl()
            
        
        
        

        


            
            
        
            

    def _brake(self):
        self.va=0
    def _moveForward(self):
        
        self.a+=self.va*0.5
    def _movemob(self):
        global pain, car
        pain.x+=self.va*0.5
        car.x+=self.va*0.5

class maria():                  ## création du personnage
    def __init__(self):         ## paramètres de base du personnage (position, image, vitesse)
        self.x,self.y,self.vx,self.vy,self.r,self.jump,self.sumersolt,self.count,self.ground,self.wallr,self.walll=[150,50,0,0,True,1,1,1,False,False,False]
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
        self.x,self.y,self.vx,self.vy,self.count,self.ground,self.wallr,self.walll,self.r=[x,y,0,0,1,False,False,False,True]

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
        if self.r:
            self.vx=3
        else:
            self.vx=-3
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
        self.x,self.y,self.vx,self.vy,self.count,self.ground,self.wallr,self.walll,self.r=[x,y,0,0,1,False,False,False,True]
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
        g_mess = pygame.font.Font(None, 60)
        g_mess_surf = g_mess.render('Appuyer sur espace pour commencer', False, 'Black')
        g_mess_rect = g_mess_surf.get_rect(center = (400, 500)) 
        screen.blit(g_mess_surf, g_mess_rect)
        #begin = pygame.font.SysFont('franklingothicmedium', 35)
        #textbegin= begin.render('Start',True,(255,255,255),(170,170,170))
        #textRectbegin = textbegin.get_rect(center = (400,350))           
        #screen.blit(textbegin, textRectbegin)
        wheel_rect = wheel.get_rect(center = (50, 550))
        screen.blit(wheel,wheel_rect)
def quitaccueil():
    global Playscreen
    global test_mario
    

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        Playscreen=False
        test_mario=True

def gotooption():
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=40 and pygame.mouse.get_pos()[0]<=40+wheel.get_width()) and(pygame.mouse.get_pos()[1]>=520 and pygame.mouse.get_pos()[1]<=520+wheel.get_width()):
                        Playscreen=False
                        option=True       

def setting():
    screen.blit(bg,(a,b))
    sound_on = pygame.image.load('starbg.png')
    sound_on_rect = sound_on.get_rect (center = (400, 300))

    #sound_off = pygame.image.load('son_off.png')
    #sound_off_rect = sound_off.get_rect (center = (400, 300))
    
    #if event.type == pygame.KEYDOWN:
     #   if event.key == pygame.K_SPACE:
      #      screen.fill('Yellow')
       #     screen.blit(sound_on, sound_on_rect)
        #    pygame.display.flip()
            #if event.type == pygame.KEYDOWN:
             #   if event.key == pygame.K_SPACE:
             #       pygame.mixer.Sound.stop(mario_theme)
              #      screen.blit(sound_off, sound_off_rect)
               #     pygame.display.flip()


def gotoacceuil():
    screen.blit(arrow,(35,480))
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=60 and pygame.mouse.get_pos()[0]<=60+wheel.get_width()) and(pygame.mouse.get_pos()[1]>=490 and pygame.mouse.get_pos()[1]<=490+wheel.get_width()):
                       Playscreen=True
                       option=False   

def Title():
        title = pygame.font.SysFont('franklingothicmedium', 55)
        texttitle = title.render('Maria',True,(255,255,255))
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

def game__over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound('mario_dies.wav')
    music.play()
    #topscore.top_score(SCORE)
    screen.fill('Blue')
    go_mess = pygame.font.Font(None, 60)
    go_mess_surf = go_mess.render('Game Over', False, 'Red')
    go_mess_rect = go_mess_surf.get_rect(center = (400, 300)) 
    screen.blit(go_mess_surf, go_mess_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    test_mario = True 
                #music.stop()
        pygame.display.update()
def start():
    return([maria(),mob_car(400,50),mob_pain(300,50),move_screen(0),True,False,True,False,False,False,0])
mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t=start()
def init_mario():
        pos._moveForward()     
        screen.blit(bg,(pos.a,b))
         
      
        mario._moveForward()
        car._moveForward()
        pain._moveForward()
        pos._movemob()
        mario._draw(screen)
        pain._draw(screen)
        car._draw(screen)
        for o in baguette:
            o._moveForward()
            o._draw(screen)
def wallgame():
    global pos, mario
    if mario.x<=0:
            mario.walll=True
            mario.x=0
    else:
            mario.walll=False
    if mario.x>=780:
            mario.wallr=True
            mario.x=780
    else:
            mario.wallr=False
    if pos.a>=0:
            pos.a=0
            pos.va=0
    if pos.a<=-11700:
            pos.a=-11700
            pos.va=0
def action():
        global pos, mario
        keys=pygame.key.get_pressed() ## c'est une fonction qui verifie si une clé est pressée, on puet, en appelant précisement un clé, la faire renvoyer un booléen
        if keys[pygame.K_RIGHT]  :##mouvmeent du personnage de gauche à droite.
            pos._velocityr() 
        elif keys[pygame.K_LEFT] :
            pos._velocityl()
        else:
            pos._brake()
            mario._brakex()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP] : ## mise en place du saut
            if mario.ground==True and mario.jump>0:
                mario.y-=10
                mario._jump()
                mario.jump-=1
            elif mario.ground==False and mario.sumersolt>0 and mario.count>30:
                mario._jump()
                mario.sumersolt-=1

object=[mario,pain,car]
mob=[car,pain]
paing=[pain]
baguette=[]


while  run:
    
    for event in pygame.event.get():   ## là étape TRES IMPORTANTE, il faut absolument définir cette action pour que la fenêtre se ferme.  
        if event.type==pygame.QUIT:
            exit()
            #run = False
    
    if Playscreen:
            clock.tick(120)                     ## définition de l'écran d'accueil
            Begin()
            Title()
            gotooption()
            quitaccueil()
           
           
            pygame.display.flip()        ## raffraichissement de l'image, cela mets à jours tout ce qui apparait à l'écran.
    if option and not Playscreen:
        setting()
        gotoacceuil()
        pygame.display.flip()
    if test_mario:   ##lancement du jeu
        init_mario()
        clock.tick(120)  
        t+=1 
        pygame.display.flip() 
        wallgame()
        action()
        
        for o in object:   
            if  o.ground==False:      ##definition du sol et des fonctions nécessaires a la chute et au saut
                o._fall()
            if o.y<470:
                o.ground= False
            else:
            
                o._ground()
        for i,o in enumerate(mob) :
            dx=o.x-mario.x
            dy=o.y-mario.y
            if dx**2<=20000:
                o._follow(t)
                
            else:
                o._walk(t)
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2:
                game_over=True
                test_mario=False
            

        for o in paing:
            if o.count%60==0:
                baguette.append(bag(o.x,o.y))
        for o in baguette:
            dx=o.x-mario.x
            dy=o.y-mario.y
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2:
                game_over=True
                test_mario=False

    if game_over:
        game__over()
