import  pygame, math, random, os, sys
from pygame.image import load               ## import des modules de base nécessare au jeu

pygame.init()           ##lancement de pygame


sw=800                  ##définition des dimensions de base de l'écran
sh=600

sol_haut = 550

##import des images et fichiers nécessaires.
bg=pygame.image.load('blabla2.png')  
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/30),int(arrow.get_height()/30)))
arrow=pygame.transform.rotate(arrow, 90)
baguette_img=pygame.image.load('baguette.png')
baguette_img= pygame.transform.scale(baguette_img,(int(baguette_img.get_width()/12),int(baguette_img.get_height()/12)) )
wheel=pygame.image.load('Settings.png')
wheel_rect = wheel.get_rect(center = (50, 550))
coeur = pygame.image.load('coeur.jpg')
coeur = pygame.transform.scale(coeur,(int(arrow.get_width()/2),int(arrow.get_height()/2)) )
coeur_rect = coeur.get_rect(center = (20, 50))
sound = pygame.image.load('sound_on.png')
sound = pygame.transform.scale(sound, (int(sound.get_width()/10), int(sound.get_height()/10)))
sound_rect = sound.get_rect (center = (400, 170))
rat = pygame.image.load('rat.png')
rat = pygame.transform.scale(rat,(int(rat.get_width()/8),int(rat.get_height()/8)) )


mario_theme = pygame.mixer.Sound('mario_theme.wav') 
lose_music = pygame.mixer.Sound('mario_dies.wav')
success = pygame.mixer.Sound('success_music.wav')
V = mario_theme.set_volume(.5) 

mus_mess = pygame.font.Font('pol_jo.ttf', 20)
mus_mess_surf = mus_mess.render('Cliquer pour activer/desactiver le son', False, 'Red', 'Blue')
mus_mess_rect = mus_mess_surf.get_rect(center = (400, 80))

son_mess = pygame.font.Font('pol_jo.ttf', 25)
son_mess_surf = son_mess.render('Son active', False, 'Blue', 'Red')
son_mess_rect = son_mess_surf.get_rect(center = (400, 120))

soff_mess = pygame.font.Font('pol_jo.ttf', 25)
soff_mess_surf = soff_mess.render('Son desactive', False, 'Blue', 'Red')
soff_mess_rect = soff_mess_surf.get_rect(center = (400, 220)) 

on = pygame.font.Font('pol_jo.ttf', 30)
on_surf = on.render('ON', False, 'Yellow', 'Blue')
on_rect = on_surf.get_rect(center=(200, 170))

off = pygame.font.Font('pol_jo.ttf', 30)
off_surf = off.render('OFF', False, 'yellow', 'Blue')
off_rect = off_surf.get_rect(center=(600, 170))


bw=bg.get_width()                   ## obtention de la dimension de l'image de base.
bh=bg.get_height()
clock=pygame.time.Clock()           ## céation de la fonction de temps.
a=0                                 ## position de l'image de fond par rapport à l'écran.
b=-bh
pygame.display.set_caption('mariolowcoast')## nom de la fenêtre pygame ouverte
screen=pygame.display.set_mode((sw,sh))

##définition des classes régissant les objets du jeu 
class move_screen():
    def __init__(self,a):
        self.a=a
        self.va=0
        self.walll=True
        self.wallr=False
    def _velocityr(self):
        global mario
        if mario.x>=475 :
            if self.a>-11250:
                if self.va>=-5:
                    self.va-=1
                mario._brakex()
            if self.a<=-11250 and mario.x<=780:
                self.a=-11250
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

        self.mobc_img=rat
        self.mobc_img_rect=self.mobc_img.get_rect()
        self.mobc_img_rect.center=(self.x,self.y)
        self.mobc_img_rect.midbottom = (self.x,550)

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
        self.x += self.vx*0.5
        self.y +=self.vy*0.5
        self.lanceur_rect.center=(self.x,self.y)
    def _draw(self,screen):                          
        screen.blit(self.lanceur,self.lanceur_rect)
        

class bag():
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

def Screen(a,b):
    screen.blit(bg,(a,b))       ## création de la fenêtre et mise a jour
    pygame.display.update()
a=0
b=600-bh

def Begin():
        screen.blit(bg,(a,b))
        
        start = pygame.font.Font('pol_jo.ttf', 35)
        pygame.draw.rect(screen,'Blue',(310,330, 170, 50))
        start= start.render('Start',True,'Red','Blue')
        start_r = start.get_rect(center = (400,350))           
        screen.blit(start, start_r)

        score_text = pygame.font.Font('pol_jo.ttf', 25)
        score_surf = score_text.render(f'Best Score = {best_score}', False, 'Black')
        score_rect = score_surf.get_rect(center = (190, 60))
        screen.blit(score_surf, score_rect) 

def quitaccueil():
    global Playscreen
    global test_mario
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=310 and pygame.mouse.get_pos()[0]<=480) and(pygame.mouse.get_pos()[1]>=330 and pygame.mouse.get_pos()[1]<=350):
                        Playscreen = False
                        test_mario = True 

def gotooption():
    screen.blit(wheel, wheel_rect)
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=40 and pygame.mouse.get_pos()[0]<=40+wheel.get_width()) and(pygame.mouse.get_pos()[1]>=520 and pygame.mouse.get_pos()[1]<=520+wheel.get_width()):
                        Playscreen=False
                        option=True       

def Option():
    global music 
    screen.blit(bg,(a,b))
    screen.blit(sound, sound_rect)
    screen.blit(mus_mess_surf, mus_mess_rect)
    pygame.draw.rect(screen,'Blue',(150,150, 100, 50)) #on
    screen.blit(on_surf, on_rect)
    pygame.draw.rect(screen,'Blue',(550,150, 100, 50)) #off
    screen.blit(off_surf, off_rect)    
    if music:
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[0]>=555 and pygame.mouse.get_pos()[0]<=705) and(pygame.mouse.get_pos()[1]>=150 and pygame.mouse.get_pos()[1]<=200):
                screen.blit(soff_mess_surf, soff_mess_rect)
                music = False            
    if not music:
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[0]>=160 and pygame.mouse.get_pos()[0]<=310) and(pygame.mouse.get_pos()[1]>=150 and pygame.mouse.get_pos()[1]<=200):
                screen.blit(son_mess_surf, son_mess_rect) 
                music = True


def gotoaccueil():
    screen.blit(arrow,(35,480))
    global option, Playscreen
    if pygame.mouse.get_pressed()[0]:
                    if (pygame.mouse.get_pos()[0]>=60 and pygame.mouse.get_pos()[0]<=60+wheel.get_width()) and(pygame.mouse.get_pos()[1]>=490 and pygame.mouse.get_pos()[1]<=490+wheel.get_width()):
                       Playscreen=True
                       option=False   

def Title():
        title = pygame.font.Font('pol_jo.ttf', 55)
        texttitle = title.render('Maria',True,'Blue')
        textRecttitle = texttitle.get_rect()
        textRecttitle.center= (400,250)           
        screen.blit(texttitle, textRecttitle)

def Home():
    global game_over, count_rat, count_lanc, music_over, test_mario, object, mob, baguette, paing, score, mario, car, pain, pos, run, Playscreen, ground, option, t, life, music
    home = pygame.font.Font('pol_jo.ttf', 30)
    pygame.draw.rect(screen,'Blue',(420,480,120,50))
    texthome= home.render('Home',run,'Blue','Yellow')
    textRecthome = texthome.get_rect()
    textRecthome.center= (480,500)           
    screen.blit(texthome, textRecthome)
    if pygame.mouse.get_pressed()[0]: 
        if (pygame.mouse.get_pos()[0]>=420 and pygame.mouse.get_pos()[0]<=540) and (pygame.mouse.get_pos()[1]>=480 and pygame.mouse.get_pos()[1]<=530):
                            mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score, count_rat, count_lanc, music, music_over=start()
                            game_over = False 
                            Playscreen=True 
                            test_mario=False 
                            object=[mario,pain,car]
                            mob=[car,pain]
                            paing=[pain]
                            baguette=[] 

def Retry():
    global game_over, count_rat, count_lanc, music_over, object, mob, paing, baguette, test_mario, score, mario, car, pain, pos, run, Playscreen, ground, option, t, life, music  
    retry = pygame.font.Font('pol_jo.ttf', 30)
    pygame.draw.rect(screen,'Blue',(220,480,190,50))
    textretry= retry.render('Retry?',True,'Blue','Yellow')
    textRectretry = textretry.get_rect()
    textRectretry.center= (320,500)           
    screen.blit(textretry, textRectretry) 
    if pygame.mouse.get_pressed()[0]:
        if  ((pygame.mouse.get_pos()[0]>=220 and pygame.mouse.get_pos()[0]<=400) and (pygame.mouse.get_pos()[1]>=480 and pygame.mouse.get_pos()[1]<=530)):
            mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score, count_rat, count_lanc, music, music_over=start()
            Playscreen=False
            test_mario = True 
            object=[mario,pain,car]
            mob=[car,pain]
            paing=[pain]
            baguette=[]
        

def Vie():
    global life, game_over, test_mario   
    screen.blit(coeur, coeur_rect)
    vie_mess = pygame.font.Font('pol_jo.ttf', 25)
    vie_mess_surf = vie_mess.render(f' = {life}', run, 'Black')
    vie_mess_rect = vie_mess_surf.get_rect(center = (75, 50 ))
    screen.blit(vie_mess_surf, vie_mess_rect)

def Score():
    global score
    SCORE=pygame.font.Font('pol_jo.ttf',25)
    textScore=SCORE.render(f'Score = {score}',run,'Blue')
    textRectScore=textScore.get_rect(center = (400, 75))
    screen.blit(textScore,textRectScore)

def Score_go(): ##affichage score sur la page game over
    global score 
    SCORE=pygame.font.Font('pol_jo.ttf',25)
    textScore=SCORE.render(f'Score = {score}',run,(255,255,255))
    textRectScore=textScore.get_rect(center = (400, 75))
    screen.blit(textScore,textRectScore)

def game__over():
    global music, music_over 
    if music:
        mario_theme.stop()
        music_over = True
        lose_music.play()
    screen.fill('Blue')
    go_mess = pygame.font.Font('pol_jo.ttf', 50)
    go_mess_surf = go_mess.render('Game Over', False, 'Red')
    go_mess_rect = go_mess_surf.get_rect(center = (400, 300)) 
    screen.blit(go_mess_surf, go_mess_rect)   
    Retry()
    Home()
    Score_go()  
    
#def well_done(): ##problème au niveau de la position de Mario
#    global music, suc_mus
#    wd_mess = pygame.font.Font('pol_jo.ttf', 50)
#    wd_mess_surf = wd_mess.render('Well done ! \n You surpassed all the obstacles!', False, 'Red')
#    wd_mess_rect = wd_mess_surf.get_rect(center = (400, 200))
#    if mario.x == 500:
#        mario.vy = -5
#        screen.fill('Blue')
#        screen.blit(wd_mess_surf, wd_mess_rect)
#        if music:
#            music = False 
#            success.play()
#        Retry()
#        Home()
#        Score_go() 



## Initialisation des valeurs 
def start():
    return([maria(),mob_car(400,50),mob_pain(300,50),move_screen(0),True,False,True,False,False,False,0, 3, 0, 0, 0, True, False])
mario,car,pain,pos,run,test_mario,Playscreen,ground,option,game_over,t, life, score, count_rat, count_lanc, music, music_over=start()
best_score = 0

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
    if pos.a<=-11250:
            pos.a=-11250
            pos.va=0
def action():
        global pos, mario
        keys=pygame.key.get_pressed() ## c'est une fonction qui verifie si une clé est pressée, on puet, en appelant précisement un clé, la faire renvoyer un booléen
        if keys[pygame.K_RIGHT]  :##mouvmeent du personnage de gauche à droite.
            pos._velocityr() 
        elif keys[pygame.K_LEFT] :
            pos._velocityl()
        elif mario.y>=470:
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

# def collisions():
#     global mario,mob
#     for mechant in mob:
#         for perso in mechant():
#             perso_centre=perso.rect.centery
#             perso_top=mob.rect.top
#             mario_bottom=mario.bottom
#             if perso_top<mario_bottom<perso_centre and mario.y>=0:
#                 mario.y=-25
#                 perso.kill()


object=[mario,pain,car]
mob=[car,pain]
paing=[pain]
baguette=[]

best_score = 0

while  run:
    
    for event in pygame.event.get():   ## là étape TRES IMPORTANTE, il faut absolument définir cette action pour que la fenêtre se ferme.  
        if event.type==pygame.QUIT:
            exit()
    
    if Playscreen:
            if music:
                mario_theme.play()
            elif not music:
                mario_theme.stop()
            clock.tick(120)                     ## définition de l'écran d'accueil
            Begin()
            Title()
            gotooption()
            quitaccueil()                     
           
            pygame.display.flip()        ## raffraîchissement de l'image, cela mets à jours tout ce qui apparait à l'écran.
    
    if option and not Playscreen:
        Option()
        gotoaccueil()
        if music:
            screen.blit(son_mess_surf, son_mess_rect)
            mario_theme.play()
        else:
            screen.blit(soff_mess_surf, soff_mess_rect)
            mario_theme.stop()   
        pygame.display.flip()

    if test_mario:   ##lancement du jeu
        if music:
            mario_theme.play()
        elif not music:
            mario_theme.stop()
        init_mario() 
        Vie()
        Score()
        clock.tick(60)
        count_rat += 1
        count_lanc += 1
        score += 1  
        t+=1 
        pygame.display.flip() 
        wallgame()
        action()
        #well_done()
        #collisions()

        
        
        for o in object:   
            if  o.ground==False:      ##definition du sol et des fonctions nécessaires a la chute et au saut
                o._fall()
            if o.y<sol_haut:
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
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2 and mario.vy>0:
                mario.y=-25
                o.remove()
            if max(dx**2,dy**2)<=(mario.mario_img.get_width()/2)**2 and mario.vy==0:
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
            test_mario=False
            
    if game_over:
        game__over()
        pygame.display.flip()
        
    if score > best_score:
        best_score = score   



# def collisions(self):
#     collisions_mobs=pygame.sprite.spritecollide(self.mario.sprite,self.lanceur, False)
#     if collisions_mobs:
#         for mob in collisions_mobs:
#             mob_centre=mob.rect.centery
#             mob_top=mob.rect.top
#             mario_bottom=self.mario.sprite.rect.bottom
#             if mob_top<mario_bottom<mob_centre and self.mario.sprite.direction.y>=0:
#                 self.mario.sprite.direction.y=-25
#                 mob.kill()


    #test collision
    
