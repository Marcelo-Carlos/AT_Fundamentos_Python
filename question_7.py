#Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo 
# de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.
import pygame
from random import randint
from pygame.locals import *

pygame.init()
screen_width, screen_heigth = 800, 600
screen = pygame.display.set_mode((screen_width, screen_heigth))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
YELLOW = (255, 255, 0)
screen.fill(BLACK)
     
def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)
        
def draw_rect_yellow():
    cor = YELLOW
    square_width, square_height = 50, 50
    x, y = randint(0, screen_heigth - square_height), randint(0, screen_width - square_width) 
    pygame.draw.rect(screen, cor, (x,y,square_width, square_height)) 
    
terminou = False
while not terminou:
    pygame.display.update()
    write_text("Question 7 - AT")  
    
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            terminou = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw_rect_yellow()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                draw_rect_yellow()
    
pygame.display.quit()
pygame.quit()