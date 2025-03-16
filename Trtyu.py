import pygame as pg
import time
import random
W,H=1000,800
WIN=pg.display.set_mode((1000,800))
BG = pg.image.load("Tetris background.jpg")
run=True
fun=False
v=10
u=800
p=random.randint(1,4)
f=60
clock= pg.time.Clock()
k=[]
t= "dhakj"
r="hsgac"
o=0

base_=pg.Rect(0,790,1000,1)



def square():
    global player,slayer
    player=pg.Rect(200,500,20,40)
    slayer=pg.Rect(220,500,20,40)
    #pg.draw.rect(WIN,"red",player)
    #pg.draw.rect(WIN,"red",slayer)
def L():
    global player,slayer
    player=pg.Rect(200,550,20,40)
    slayer=pg.Rect(200,580,40,20)
def reverse_L():
    global player,slayer
    player=pg.Rect(200,620,20,40)
    slayer=pg.Rect(180,650,40,20)
    
def squigally():
    global player,slayer
    player=pg.Rect(200,720,20,40)
    slayer=pg.Rect(220,700,20,40)
    #pg.draw.rect(WIN,"red",player)
    #pg.draw.rect(WIN,"red",slayer)
def reverse_squigally():
    global player,slayer
    player=pg.Rect(250,700,20,40)
    slayer=pg.Rect(270,720,20,40)
if p==1:
    
    L()
elif p==2:
    
    reverse_L()
elif p==3:
    
    squigally()
elif p==4:
    
    reverse_squigally()
    



while run:
    WIN.blit(BG,(0,0))
    
    #if k!=[]:
        #WIN.blit(BG,(0,0))
        
    for m in k:
            
        o+=1
        pg.draw.rect(WIN,"blue",m)
        
        
        
    clock.tick(60)
    pg.draw.rect(WIN,"black",base_)
    
    pg.draw.rect(WIN,"blue",player)
    pg.draw.rect(WIN,"blue",slayer)
    pg.display.update()
    key=pg.key.get_pressed()

    if key[pg.K_LEFT] and player.x - v >=0:
        f=60
        player.x -= v
        slayer.x -= v
        
        if e.type==key[pg.K_LEFT]:
            u=10
        else:
            u=800
    if key[pg.K_RIGHT] and slayer.x - v <= W -40:
        f=60
        player.x += v
        slayer.x += v
        if e.type==key[pg.K_RIGHT]:
            u=10
        else:
            u=800
    if key[pg.K_UP] and slayer.y - v >=0:
        f=60
        player.y -= v
        slayer.y -= v
        if e.type==key[pg.K_UP]:
            u=10
        else:
            u=800
    if key[pg.K_DOWN] and player.y - v + 20 <= H -40:
        f=60
        player.y += v
        slayer.y += v
        if e.type==key[pg.K_DOWN]:
            u=10
        else:
            u=800

    
    if player.colliderect(base_) or slayer.colliderect(base_)== True:
        t=player
        r=slayer
        if k.count(t)<1:
            k.append(t)
        if k.count(r)<1:
            k.append(r)
        p=random.randint(1,4)
        if p==1:
    
            L()
        if p==2:
           reverse_L()
        if p==3:
    
           squigally()
        if p==4:
    
           reverse_squigally()
            
        
        
        

    for e in pg.event.get():
        if e.type == pg.QUIT:
            run= False
            print(player)
            print(slayer)
            
            break
    
    

print(t)
print(r)
print(o)
pg.quit()
    



