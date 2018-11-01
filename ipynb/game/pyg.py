import pygame
from pygame.locals import *
from sys import exit



pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Hello, World!")

pygame.display.set_icon(pygame.image.load("fugu.png").convert_alpha())
 
font = pygame.font.SysFont("arial", 16);
font_height = font.get_linesize()
event_text = []
 
while True:
 
    event = pygame.event.wait()
    event_text.append(str(event))
    #获得时间的名称
    event_text = event_text[-SCREEN_SIZE[1]//font_height:]
    #这个切片操作保证了event_text里面只保留一个屏幕的文字
 
    if event.type == QUIT:
        exit()
 
    screen.fill((0, 0, 0))
 
    y =0 
    #找一个合适的起笔位置，最下面开始但是要留一行的空
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0, 255, 0)), (0, y) )
        #以后会讲
        y+=font_height
        #把笔提一行
 
    pygame.display.update()