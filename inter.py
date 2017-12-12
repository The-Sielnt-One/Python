from tkinter import *
import pygame
import pygame.locals
import time
from motor import marche,frust

root=Tk()
x,y=root.winfo_screenwidth(),root.winfo_screenheight()
root.destroy()
pygame.init()
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Welcome")

v=True
BAc=(95,158,160)
BBc=(30,144,255)
BRc=(0,191,255)
Bamphic=(100,149,237)
Bexitc=(230,0,0)
bx,by=x/4,y/5.5

pygame.mixer.init()
hello=pygame.mixer.Sound("BB8-Hello.wav")
hello.play()
time.sleep(2.5)
text=['Bloc A','Bloc B','Bloc R','Amphi','exit']
pygame.font.init()

def Dtxt(ch,x,y):
    screen.blit(ft.render(ch,True,(0,0,0)),(x,y))
    pygame.display.update()

def Butt(elt,t):
    return pygame.draw.rect(screen,elt,t)

def cal():
    r=pygame.mixer.Sound('BB8 Loading Data.wav')
    r.play()
    time.sleep(5)
    r=pygame.mixer.Sound('BB8 Follow me!.wav')
    r.play()
    time.sleep(3)
    
def fr():
    r=pygame.mixer.Sound('BB8 Frustration.wav')
    r.play()
    frust()
    time.sleep(3)
 
def main():
    screen.fill((255,255,255))
    im=pygame.image.load("enisologo.png").convert()
    screen.blit(im,(0,50))
    ft=pygame.font.SysFont("comicsansms",int(by*2/3))
    BA=Butt(BAc,(x-bx,0,bx,by))
    BB=Butt(BBc,(x-bx,by+2,bx,by))
    BR=Butt(BRc,(x-bx,2*(by+2),bx,by))
    Bamphi=Butt(Bamphic,(x-bx,3*(by+2),bx,by))
    Bexit=Butt(Bexitc,(x-bx,4*(by+2),bx,by))
    pygame.display.flip()
    for i in range(5):
        Dtxt(text[i],x-bx*5/6,10*i*by/10)
    dep=time.time()
    while v:
        for i in pygame.event.get():
            if (i.type==pygame.MOUSEBUTTONDOWN):
                mouse=pygame.mouse.get_pos()
                if BA.collidepoint(mouse):
                    cal():
                    marche('A')
                if BB.collidepoint(mouse):
                    cal()
                    marche('B')
                if BR.collidepoint(mouse):
                    cal()
                    marche('R')
                if Bamphi.collidepoint(mouse):
                    cal()
                    marche('amphi')
                if (Bexit.collidepoint(mouse))or(i.type==pygame.QUIT):
                    v=False
            if (time.time()-dep>=20):
                v=False
    pygame.quit()
