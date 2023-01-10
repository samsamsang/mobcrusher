import  pygame, random ## import des modules de base nécessare au jeu

pygame.init()           ##lancement de pygame


sw=800                  ##définition des dimensions de base de l'écran
sh=600
sol_haut = 550          ##définition de la hauteur du sol 
lv=1                    ##niveau par défaut
S=[50, 75, 100]         ##valeurs de l'indentation du score en fonction du niveau 
parachute = [360, 410, 460] ##hauteur à laquelle apparaissent les mobs en fonction du niveau 

#import des fichiers nécessaires 
bg=pygame.image.load('map.png')  ##import des images 
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/30),int(arrow.get_height()/30)))
arrow=pygame.transform.rotate(arrow, 90)
baguette_img=pygame.image.load('baguette.png')
baguette_img= pygame.transform.scale(baguette_img,(int(baguette_img.get_width()/12),int(baguette_img.get_height()/12)) )
wheel=pygame.image.load('Settings.png')
wheel_rect = wheel.get_rect(center = (50, 575))
coeur = pygame.image.load('coeur.png')
coeur = pygame.transform.scale(coeur,(int(arrow.get_width()/2),int(arrow.get_height()/2)) )
coeur_rect = coeur.get_rect(center = (20, 50))
sound = pygame.image.load('sound_on.png')
sound = pygame.transform.scale(sound, (int(sound.get_width()/10), int(sound.get_height()/10)))
sound_rect = sound.get_rect (center = (400, 170))
rat = pygame.image.load('rat.png')
rat = pygame.transform.scale(rat,(int(rat.get_width()/8),int(rat.get_height()/8))) 
maison = pygame.image.load('maison.png')
maison = pygame.transform.scale(maison, (int(maison.get_width()/5),int(maison.get_height()/5)))
maison_rect = maison.get_rect(center =(40, 100))
#import des fichiers sonores 
mario_theme = pygame.mixer.Sound('mario_theme.wav') 
lose_music = pygame.mixer.Sound('mario_dies.wav')
success = pygame.mixer.Sound('mario_dies.wav')
V = mario_theme.set_volume(.5) 
#création des zones de texte 
musbison_mess = pygame.font.Font('pol_jo.ttf', 16)
musbison_mess_surf = musbison_mess.render('La musique vous insupporte ?  (comprehensible) Desactivez-la !', False, 'Black')
musbison_mess_rect = musbison_mess_surf.get_rect(center = (400, 300))

musbisoff_mess = pygame.font.Font('pol_jo.ttf', 16)
musbisoff_mess_surf = musbisoff_mess.render('La musique vous manque ? (moins comprehensible) Activez-la !', False, 'Black')
musbisoff_mess_rect = musbisoff_mess_surf.get_rect(center = (400, 300))

mus_mess = pygame.font.Font('pol_jo.ttf', 20)
mus_mess_surf = mus_mess.render('Cliquer pour activer/desactiver le son', False, 'Black')
mus_mess_rect = mus_mess_surf.get_rect(center = (400, 80))

son_mess = pygame.font.Font('pol_jo.ttf', 25)
son_mess_surf = son_mess.render('Son active', False, 'Blue')
son_mess_rect = son_mess_surf.get_rect(center = (400, 120))

soff_mess = pygame.font.Font('pol_jo.ttf', 25)
soff_mess_surf = soff_mess.render('Son desactive', False, 'Blue')
soff_mess_rect = soff_mess_surf.get_rect(center = (400, 220)) 

on = pygame.font.Font('pol_jo.ttf', 30) #ensuite fct def level, clic reprendre condition fonction quiaccueil av 
on_surf = on.render('ON', False, 'Black', 'Blue') 
on_rect = on_surf.get_rect(center=(200, 170))

off = pygame.font.Font('pol_jo.ttf', 30)
off_surf = off.render('OFF', False, 'Black', 'Blue')
off_rect = off_surf.get_rect(center=(600, 170))

level1 = pygame.font.Font('pol_jo.ttf', 25)
level1_surf = level1.render('1', False, 'Black', 'Blue') 
level1_rect = level1_surf.get_rect(center=(225, 515))
level2 = pygame.font.Font('pol_jo.ttf', 25)
level2_surf = level2.render('2', False, 'Black', 'Blue') 
level2_rect = level2_surf.get_rect(center=(425, 515))
level3 = pygame.font.Font('pol_jo.ttf', 25)
level3_surf = level3.render('3', False, 'Black', 'Blue') 
level3_rect = level3_surf.get_rect(center=(625, 515))
#booléen
music = True 

bw=bg.get_width()                   ## obtention de la dimension de l'image de base
bh=bg.get_height()
clock=pygame.time.Clock()           ## céation de la fonction de temps
frm=0.5        
a=0                                 ##position du fond d'écran 
b=600-bh

pygame.display.set_caption('MarioLowCost')## nom de la fenêtre pygame ouverte
screen=pygame.display.set_mode((sw,sh))

##définition des classes régissant les objets du jeu 
class move_screen(): #déplacement de la map 
    global mario, frm, mob
    def __init__(self,a):
        self.a,self.va,self.vaf,self.walll,self.wallr=[a,0,0,True,False]
        self.va=0
        self.walll=True
        self.wallr=False
    def _velocityr(self):
        
        if mario.x>=475 :
            if self.a>-11250:
                if self.va>=-5:
                    self.va-=1
                mario._brakex()
                self.vaf,mario.vxf=[-mario.vxf,0]
            if self.a<=-11250 and mario.x<=780:
                self.a=-11250
                mario._velocityxr()
        elif   not mario.wallr :
            self.va=0
            self.vaf=0
            mario._velocityxr()
    def _velocityl(self):
        if mario.x<=100 :
            if self.a<0:
                if self.va<=5:
                   self.va+=1
                mario._brakex()
                self.vaf,mario.vxf=[-mario.vxf,0]
            if self.a>=0 and mario.x>=0:
                self.a=0    
                mario._velocityxl()
        elif  not mario.walll :
            self.va=0
            self.vaf=0
            mario._velocityxl()   
    def _brake(self):
        self.va=0
        self.vaf=0
    def _moveForward(self):
        if self.vaf!=0:
            self.a+=self.vaf*frm
        else:
            self.a+=self.va*frm
    def _movemob(self):
        for o in mob:
            if self.vaf!=0:
                o.x+=self.vaf*frm
            else:
                o.x+=self.va*frm

class maria():               ## création du personnage
    def __init__(self):         ## paramètres de base du personnage (image, position)
        self.x,self.y,self.vx,self.vy,self.vxf,self.r,self.jump,self.sumersolt,self.count,self.ground,self.wallr,self.walll=[150,50,0,0,0,True,1,1,1,False,False,False]
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.center=(self.x,self.y)
    def _velocityxr(self):      ##actions impliquant le personnage (variation de la vitesse)
        if self.r==False:
            self.mario_img,self.r=[pygame.transform.flip(self.mario_img, 1, 0),True]
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
    def _ground(self):  ##definition du sol et des fonctions nécessaires a la chute et au saut 
        self.ground,self.vy,self.vxf,self.jump,self.sumersolt,self.count=[True,0,0,1,1,1]
    def _jump(self): 
        self.vy=0
        self.vy-=10 
    def _fall(self): 
        self.vy+=0.3
        self.count+=1
    def _draw(self,screen):                             ##apparition de l'image à l'écran
        screen.blit(self.mario_img,self.mario_img_rect)
    def _moveForward(self):
        if self.vxf!=0:         ##actualisation automatique de la postion du personnage en fonction de la vitesse
            self.x +=self.vxf*frm
        else:
            self.x+=self.vx*frm
        self.y +=self.vy*frm
        self.mario_img_rect.center=(self.x,self.y)

class mob_rat(): ##définition des rats 
    def __init__(self,x,y): ##cracatéristiques des rats (image, position)
        self.x,self.y,self.vx,self.vy,self.count,self.ground,self.wallr,self.walll,self.r=[x,y,0,0,1,False,False,False,True]
        self.mobc_img=rat
        self.mobc_img_rect=self.mobc_img.get_rect()
        self.mobc_img_rect.center=(self.x,self.y)
        self.mobc_img_rect.midbottom = (self.x,sol_haut)
    def _fall(self): ##définition des actions du rat 
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
    def _follow(self,t): #à la poursuite de Maria
        if self.x-mario.x<-1:
            if self.r==False:
                self.mobc_img=pygame.transform.flip(self.mobc_img,1,0)
                self.r=True
            if self.vx<1:
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
        global frm    
        self.x += self.vx*frm
        self.y +=self.vy*frm
        self.mobc_img_rect.center=(self.x,self.y)                                   
    def _draw(self,screen):                             
        screen.blit(self.mobc_img,self.mobc_img_rect)

class mob_pain(): ##définition des lanceurs de baguettes
    def __init__(self,x,y):
        self.x,self.y,self.vx,self.vy,self.count,self.ground,self.wallr,self.walll,self.r=[x,y,0,0,1,False,False,False,True]
        self.lanceur=pygame.image.load('lanceurdebaguette.png')
        self.lanceur=pygame.transform.flip(self.lanceur,1,0)
        self.lanceur=pygame.transform.scale(self.lanceur,(int(self.lanceur.get_width()/13),int(self.lanceur.get_height()/13)) )
        self.lanceur_rect=self.lanceur.get_rect()
        self.lanceur_rect.center=(self.x,self.y)
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
                self.lanceur=pygame.transform.flip(self.lanceur,1,0)
                self.r=True
        if t%150==0:
            self.vy-=10
        if self.x-mario.x>5:
            if self.r==True:
                self.lanceur=pygame.transform.flip(self.lanceur,1,0)
                self.r=False    
    def _walk(self,t):
        self.count=1
        if self.ground:
            if self.r:
                self.vx=5
            else:
                self.vx=-5
            if t%100==0:
                self.lanceur=pygame.transform.flip(self.lanceur,1,0)
                self.vx=-self.vx
                self.r= not self.r
    def _brakex(self):
        if self.wallr and self.vx>0:
            self.vx=0
        if self.walll and self.vx<0:
            self.vx=0
    def _moveForward(self):       
        global frm     
        self.x += self.vx*frm
        self.y +=self.vy*frm
        self.lanceur_rect.center=(self.x,self.y)
    def _draw(self,screen):                          
        screen.blit(self.lanceur,self.lanceur_rect)
        
class bag(): ##définition des baguettes, équivalentes aux boules de feu 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        v=7
        self.paing_img=baguette_img
        self.paing_img_rect=baguette_img.get_rect() 
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

##définition des fonctions régissant ce qui apparaît à l'écran 
def Screen(a,b): ## création de la fenêtre et mise a jour
    screen.blit(bg,(a,b)) 
    pygame.display.update()      

def Begin(): ##définition écran accueil 
        screen.blit(bg,(a,b)) #fond d'écran

        start = pygame.font.Font('pol_jo.ttf', 35) #design bouton start 
        pygame.draw.rect(screen,'Blue',(310,330, 170, 50))
        start= start.render('Start',True,'Red','Blue')
        start_r = start.get_rect(center = (400,350))           
        screen.blit(start, start_r)

        score_text = pygame.font.Font('pol_jo.ttf', 25) #affichage du meilleur score 
        score_surf = score_text.render(f'Best Score = {best_score}', False, 'Black')
        score_rect = score_surf.get_rect(center = (190, 60))
        screen.blit(score_surf, score_rect) 

        choix_niv_text = pygame.font.Font('pol_jo.ttf', 25) ##choix du niveau
        choix_niv_surf = choix_niv_text.render("choisir le niveau", False, 'Black')
        choix_niv_rect = choix_niv_surf.get_rect(center = (400, 440))
        screen.blit(choix_niv_surf, choix_niv_rect)

def Title(): #titre du jeu 
        title = pygame.font.Font('pol_jo.ttf', 55)
        texttitle = title.render('Mob Crusher',True,'Blue')
        textRecttitle = texttitle.get_rect()
        textRecttitle.center= (400,250)           
        screen.blit(texttitle, textRecttitle)

def choix_level(): ##définition des boutons pour le choix du niveau 
    global lv
    pygame.draw.rect(screen,'Blue',(200,490, 50, 50))
    screen.blit(level1_surf, level1_rect)
    pygame.draw.rect(screen,'Blue',(400,490, 50, 50))
    screen.blit(level2_surf, level2_rect)
    pygame.draw.rect(screen,'Blue',(600,490, 50, 50))
    screen.blit(level3_surf, level3_rect)
    if (pygame.mouse.get_pressed()[0]):
        if (pygame.mouse.get_pos()[0]>=150 and pygame.mouse.get_pos()[0]<=250) and(pygame.mouse.get_pos()[1]>=440 and pygame.mouse.get_pos()[1]<=540):
                lv=1
        if (pygame.mouse.get_pos()[0]>=350 and pygame.mouse.get_pos()[0]<=450) and(pygame.mouse.get_pos()[1]>=440 and pygame.mouse.get_pos()[1]<=540):
                lv=2
        if (pygame.mouse.get_pos()[0]>=550 and pygame.mouse.get_pos()[0]<=650) and(pygame.mouse.get_pos()[1]>=440 and pygame.mouse.get_pos()[1]<=540):
                lv=3

def affiche_level(): ##affichage du niveau 
    level= pygame.font.Font('pol_jo.ttf', 25)
    level_surf = level.render(f"level = {lv}", False, 'Black')
    level_rect=level_surf.get_rect(center = (650, 60))
    screen.blit(level_surf, level_rect)

def gotooption(): ##passage aux options 
    screen.blit(wheel, wheel_rect)
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=50-wheel.get_width() and pygame.mouse.get_pos()[0]<=50+wheel.get_width()) and(pygame.mouse.get_pos()[1]>=575-wheel.get_height() and pygame.mouse.get_pos()[1]<=575+wheel.get_height()):
                        Playscreen=False
                        option=True       
                        
def Option(): ##définition du menu des options (son et niveaux)
    global music 
    screen.blit(bg,(a,b))
    screen.blit(sound, sound_rect)
    screen.blit(mus_mess_surf, mus_mess_rect)
    pygame.draw.rect(screen,'Blue',(150,150, 100, 50)) 
    screen.blit(on_surf, on_rect)
    pygame.draw.rect(screen,'Blue',(550,150, 100, 50)) 
    screen.blit(off_surf, off_rect)    
    if music: ##désactiver la musique
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[0]>=555 and pygame.mouse.get_pos()[0]<=705) and(pygame.mouse.get_pos()[1]>=150 and pygame.mouse.get_pos()[1]<=200):
                screen.blit(soff_mess_surf, soff_mess_rect)
                screen.blit(musbisoff_mess_surf, musbisoff_mess_rect)
                music = False            
    if not music: ##réactiver la musique 
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[0]>=160 and pygame.mouse.get_pos()[0]<=310) and(pygame.mouse.get_pos()[1]>=150 and pygame.mouse.get_pos()[1]<=200):
                screen.blit(son_mess_surf, son_mess_rect) 
                screen.blit(musbison_mess_surf, musbison_mess_rect)
                music = True 

def gotoaccueil(): #retour à l'écran d'accueil 
    screen.blit(arrow,(35,480))
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=60-arrow.get_width() and pygame.mouse.get_pos()[0]<=60+arrow.get_width()) and(pygame.mouse.get_pos()[1]>=490-arrow.get_height() and pygame.mouse.get_pos()[1]<=490+arrow.get_height()):
                       Playscreen=True
                       option=False  

def quitaccueil(): ##passage au jeu
    global Playscreen
    global test_mario
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=310 and pygame.mouse.get_pos()[0]<=480) and(pygame.mouse.get_pos()[1]>=300 and pygame.mouse.get_pos()[1]<=400):
                        Playscreen = False
                        test_mario = True 

def Vie(): #mise en place de l'affichage des vies 
    global life, game_over, test_mario   
    screen.blit(coeur, coeur_rect)
    vie_mess = pygame.font.Font('pol_jo.ttf', 25)
    vie_mess_surf = vie_mess.render(f' = {life}', run, 'Black')
    vie_mess_rect = vie_mess_surf.get_rect(center = (75, 50))
    screen.blit(vie_mess_surf, vie_mess_rect)

def back_to_home(): #retour à l'écran d'accueil 
    global game_over, test_mario, object, mob, baguette, paing, score, mario, car, pain, pos, run, Playscreen, ground, option, t, life           
    screen.blit(maison, maison_rect)
    if pygame.mouse.get_pressed()[0]: 
        if (pygame.mouse.get_pos()[0]>=40-maison.get_width() and pygame.mouse.get_pos()[0]<=40+maison.get_width()) and(pygame.mouse.get_pos()[1]>=100-maison.get_height() and pygame.mouse.get_pos()[1]<=100+maison.get_height()):
                            mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score=start()
                            test_mario=False
                            Playscreen=True

def Score(): #affichage du score en direct 
    global score 
    SCORE=pygame.font.Font('pol_jo.ttf',25)
    textScore=SCORE.render(f'Score = {score}',run,'Blue')
    textRectScore=textScore.get_rect(center = (400, 75))
    screen.blit(textScore,textRectScore)

def game__over(): ##définition de la page game over
    global music, music_over
    screen.fill('Blue')
    go_mess = pygame.font.Font('pol_jo.ttf', 50)
    go_mess_surf = go_mess.render('Game Over', False, 'Red')
    go_mess_rect = go_mess_surf.get_rect(center = (400, 300)) 
    screen.blit(go_mess_surf, go_mess_rect)   
    Retry()
    Home()
    Score_go()                           

def Home():#retour à l'accueil 
    global game_over, test_mario, object, mob, baguette, paing, score, mario, car, pain, pos, run, Playscreen, ground, option, t, life
    home = pygame.font.Font('pol_jo.ttf', 30)
    pygame.draw.rect(screen,'Blue',(420,480,120,50))
    texthome= home.render('Home',run,'Blue','Yellow')
    textRecthome = texthome.get_rect()
    textRecthome.center= (480,500)           
    screen.blit(texthome, textRecthome)
    if pygame.mouse.get_pressed()[0]: 
        if (pygame.mouse.get_pos()[0]>=420 and pygame.mouse.get_pos()[0]<=540) and (pygame.mouse.get_pos()[1]>=480 and pygame.mouse.get_pos()[1]<=530):
                            mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score=start()
                            game_over = False 
                            reset_list()

def Retry(): #nouvel essai 
    global game_over, object,mob,paing,baguette,test_mario, score, mario, car, pain, pos, run, Playscreen, ground, option, t, life  
    retry = pygame.font.Font('pol_jo.ttf', 30)
    pygame.draw.rect(screen,'Blue',(220,480,190,50))
    textretry= retry.render('Retry?',True,'Blue','Yellow')
    textRectretry = textretry.get_rect()
    textRectretry.center= (320,500)           
    screen.blit(textretry, textRectretry) 
    if pygame.mouse.get_pressed()[0]: 
        if  ((pygame.mouse.get_pos()[0]>=220 and pygame.mouse.get_pos()[0]<=400) and (pygame.mouse.get_pos()[1]>=480 and pygame.mouse.get_pos()[1]<=530)):
            mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score=start()
            Playscreen = False 
            test_mario = True 
            reset_list()

def Score_go(): ##affichage du score
    global score 
    SCORE=pygame.font.Font('pol_jo.ttf',25)
    textScore=SCORE.render(f'Score = {score}',run,(255,255,255))
    textRectScore=textScore.get_rect(center = (400, 75))
    screen.blit(textScore,textRectScore)

def reset_list(): #définition d'une liste regroupant les différentes listes utilisées pour appler les objets (figures)
    global  mob, paing, baguette
    mob,paing,baguette=[[car,pain],[pain],[]] 

## Initialisation des valeurs 
def start():
    return([maria(),mob_rat(400,50),mob_pain(300,50),move_screen(0),True,False,True,False,False,False,0, 3, 0])

def init_mario():
        pos._moveForward()     
        pos._movemob()
        screen.blit(bg,(pos.a,b))
        mario._moveForward()
        for o in mob:
            o._moveForward()
            o._draw(screen)
        
        mario._draw(screen)
        
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
    if pos.a<=-11250:
            pos.a=-11250
            pos.va=0
def action():
        global pos, mario
        keys=pygame.key.get_pressed() ## c'est une fonction qui verifie si une clé est pressée, on peut, en appelant précisement une clé, la faire renvoyer un booléen
        if keys[pygame.K_RIGHT] or mario.vxf >0  :##mouvmeent du personnage de gauche à droite.
            pos._velocityr()
        elif keys[pygame.K_LEFT] or mario.vxf <0 :
            pos._velocityl()            
        elif mario.y>=sol_haut:
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
def gener_mob(t,lv): #apparition des mobs de manière aléatoire sur la map, aux alentours du personnage 
    if (t*lv)%400==100:
        mob.append(mob_rat(random.randrange(int(mario.x-300), int(mario.x+300)), parachute[lv-1]))
    if (t*lv)%1300==1000:
        mob.append(mob_pain(random.randrange(int(mario.x-300), int(mario.x+300)),parachute[lv-1]))
        paing.append(mob[-1])

mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score=start()
reset_list()

best_score = 0 

##lancement du jeu 
while  run:
    for event in pygame.event.get():   ## là étape TRES IMPORTANTE, il faut absolument définir cette action pour que la fenêtre se ferme.  
        if event.type==pygame.QUIT:
            exit()
    
    if Playscreen: ## définition de l'écran d'accueil
            if music:
                mario_theme.play()
            elif not music:
                mario_theme.stop()
            clock.tick(120)                     
            Begin()
            Title()
            gotooption()
            quitaccueil()   
            choix_level()
            affiche_level()                   
            pygame.display.flip()        ## raffraîchissement de l'image, cela met à jours tout ce qui apparait à l'écran.
    
    if option and not Playscreen: ##définition de la page des options 
        Option()
        gotoaccueil()
        if music:
            screen.blit(son_mess_surf, son_mess_rect)
            screen.blit(musbison_mess_surf, musbison_mess_rect)
            mario_theme.play()
        else:
            screen.blit(soff_mess_surf, soff_mess_rect)
            screen.blit(musbisoff_mess_surf, musbisoff_mess_rect) 
            mario_theme.stop()   
        pygame.display.flip()

    if test_mario:   ##lancement du jeu
        if music:
            mario_theme.play()
        elif not music:
            mario_theme.stop() 
        init_mario() 
        affiche_level() 
        Vie()
        Score()
        back_to_home()
        gener_mob(t,lv)
        clock.tick(120) 
        t+=1
        if t%10==0:
            score+=1
        pygame.display.flip() 
        wallgame()
        action() 
        
        if not mario.ground: #collisions
            mario._fall()
        if mario.y<sol_haut:
            mario.ground=False
        else:
            mario._ground()
        
        for o in mob:   
            if   not o.ground:      
                o._fall()
            if o.y<sol_haut:
                o.ground= False
            else:
                o._ground()
            dx=o.x-mario.x 
            dy=o.y-mario.y
            if dx**2<=20000:
                o._follow(t)   
            else:
                o._walk(t)
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2 and mario.vy>0:
                mario.y-=25
                mario.vy=-5
                mob.remove(o)
                score += S[lv -1]

                pygame.display.flip()

            elif max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2 :
                mario.y-=10
                mario.vy=-5
                if o.r==True:
                    mario.x+=10
                    mario.vxf=5
                else:
                    mario.x-=10
                    mario.vxf=-5
                life -= 1
                                    
        for o in paing:
            if o.count%60==0:
                baguette.append(bag(o.x,o.y))
        for o in baguette:
            dx=o.x-mario.x
            dy=o.y-mario.y
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2  :
                life -= 1
                baguette.remove(o)

        if life <= 0:
            game_over = True
            if music:
                mario_theme.stop()
                music_over = True 
                lose_music.play()
            test_mario=False

    if game_over:
        game__over()
        pygame.display.flip()

    if score > best_score:
        best_score = score    
