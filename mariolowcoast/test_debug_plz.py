
import  pygame, math, random, os 
from pygame.image import load

pygame.init()


sw=800
sh=600

run=True
test_mario=True
Playscreen=False
ground= True

bg=pygame.image.load('blabla.png')
bg=pygame.transform.scale(bg, (int(bg.get_width()/4),int(bg.get_height()/4)))
arrow=pygame.image.load('arrow.png')
arrow=pygame.transform.scale(arrow, (int(arrow.get_width()/20),int(arrow.get_height()/20)))
arrow=pygame.transform.rotate(arrow, 90)
wheel=pygame.image.load('Settings.png')
bw=bg.get_width()
bh=bg.get_height()
clock=pygame.time.Clock()
a=0
b=-bh
pygame.display.set_caption('mariolowcoast')
screen=pygame.display.set_mode((sw,sh))
def Screen(a,b):
    screen.blit(bg,(a,b))
    pygame.display.update()
a=0
b=600-bh
class maria():
    def __init__(self):
        self.x=50
        self.y=50
        self.vx=0
        self.vy=0
        self.mario_img = pygame.image.load('maryo.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.center=(self.x,self.y)
    def _velocityxr(self):
        if self.vx<=10:
            self.vx+=1
    def _velocityxl(self):
        if self.vx>=-10:
            self.vx-=1
    def _brakex(self):
        if self.vx!=0:
            self.vx=0
    def _jump(self):
        self.vy=10
        while not ground:
            self.vy-=0.2
        self.vy=0
    def _fall(self):
        self.vy+=0.2
    def _draw(self,screen):
        screen.blit(self.mario_img,self.mario_img_rect)




    def _moveForward(self):
        self.x += self.vx*0.25
        self.y +=self.vy*0.25

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
    
    for event in pygame.event.get():     
        if event.type==pygame.QUIT:
            run=False
    if Playscreen:
           Begin()
           Title()
           gotooption()
           
           pygame.display.flip()
    elif test_mario:
        screen.blit(bg,(a,b))
        
        mario._moveForward()
        mario._draw(screen)
        pygame.display.flip()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and a>= 800-bw:
            
            mario.x+=50
            pygame.display.update()
        elif keys[pygame.K_LEFT] and a<= 5:
            
            mario.y+=50
    
        else:
            mario._brakex()
        if  ground==False:
            mario._fall()
        if mario.y<1500:
            ground= False
        else:
            ground= True


            
    
            
        
