import numpy as np
import matplotlib.pyplot as plt
import pygame
import pygame.locals
import time
import os , os.path

list =[f for f in os.listdir(/home/pi/Desktop/scanner) if (f[0:2:1] =="DB")]#.py .sh . .. & visitor.png
dep=time.time()
x,y=300,200
pygame.init()
screen=pygame.display.set_mode((x,y))
pygame.display.set_caption("Scanner")
pygame.font.init()
ft=pygame.font.SysFont("comicsansms",50)
screen.fill((255,255,255))
pygame.mixer.init()
im=plt.imread("visitor.png")
c=0

gamma=lambda x:0.2126*x[0] + 0.7152*x[1] + 0.0722*x[2]

def cmp(x,y,m):
    xg=np.full(x.shape[0:2],np.apply_along_axis(gamma, -1, x),float)
    yg=np.full(y.shape[0:2],np.apply_along_axis(gamma, -1, y),float)
    mar=no.full(x.shape[0:2],m,float)
    return np.array_equal(yg-xg,mar)


for i in list:
    ip=plt.imread(i)
    v=cmp(ip,im)
    if v:
        break
if v:
    imp=pygame.image.load(i).convert()
    screen.blit(imp,(0,0))
    we=pygame.mixer.Sound("welcome.wav")
    screen.blit(ft.render("WECLOME",True,(0,0,0)),(100,5))
    we.play()
    screen.update()
    time.sleep(1)
else:
    if imp in locals():
        screen.blit(imp,(0,0))
        wa=pygame.mixer.Sound("wanted.wav")
        screen.blit(ft.render("WANTED",True,(0,0,0)),(100,5))
        wa.play()
        screen.update()
        time.sleep(1)
    elif c<3:
        n=pygame.mixer.Sound("nope.wav")
        screen.blit(ft.render("GO AWAY",True,(0,0,0)),(50,50))
        n.play()
        screen.update()
        time.sleep(1)
        c+=1
    else:
        c=0
        f=pygame.mixer.Sound("")
        screen.blit(ft.render("FUCK OFF",True,(0,0,0)),(50,50))
        f.play()
        screen.update()
        time.sleep(1)
while True:
    if (time.time()-dep>=180):
        pygame.quit()
        break