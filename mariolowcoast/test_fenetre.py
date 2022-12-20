import pygame, re
sw=1550
sh=750
run=True
i=0
y=0
pygame.init()
screen=pygame.display.set_mode((sw,sh))
print(pygame.font.get_fonts())
while run:
    for event in pygame.event.get():     
        if event.type==pygame.QUIT:
            run=False
    k=0
    p=0
    for a in pygame.font.get_fonts():
        if k>=700:
            p+=4
            k==0
        else:
            k+=20
        
        
        title = pygame.font.SysFont(a, 12)
        texttitle = title.render('1',run,(255,255,255))
        textRecttitle = texttitle.get_rect()
        textRecttitle.center= (i+k,y+p)           
        screen.blit(texttitle, textRecttitle)
        pygame.display.flip()