import pygame as pg
from sys import exit
import random,time
pg.display.init()
pg.display.set_caption("this is first game in Ali's World")
pg.init()
Screen = pg.display.set_mode((800,400),pg.RESIZABLE)
Clock = pg.time.Clock()
# carrector = pg.Surface((75,50))
# carrector.fill('red')
caracter = pg.image.load("carector.png").convert_alpha()
BG = pg.image.load("milky-way-2695569_1280.jpg").convert()
Block = pg.image.load("block.png").convert()
Font = pg.font.Font(None,30)
font_surface = Font.render("Welcoe To Mamad Game",False,"green") 
Block_y = 200
Block_x = 730
caracter_rect = caracter.get_rect(midbottom = (13,200))


# Time = time.time()
# real_time = 0
# time_surface = Font.render(f"{real_time}",False, "white")

while True :

    Screen.blit(BG,(0,0))
    Screen.blit(caracter,(10,200))
    Screen.blit(font_surface,(0,0))
    if Block_x > 70:
        Screen.blit(Block,(Block_x,Block_y ))
        Block_x -=5
    else : 
        Block_x = 720


    for event in pg.event.get():
        if event.type == pg.QUIT:
                pg.quit()
                exit()
    
    Clock.tick(60)
    pg.display.update()
