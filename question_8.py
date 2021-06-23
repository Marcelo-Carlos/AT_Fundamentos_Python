#Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre 
# ele na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo 
# em uma posição aleatória na tela. Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser
# eliminados
import pygame
from pygame.locals import *
from random import randint

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, BLUE = (255, 0, 0), (0, 0, 255)
YELLOW = (255,255,0)
screen.fill(BLACK)
x, y = screen_width/2, 80
square_width, square_height = 50, 50

class Quadradinho():
    def __init__(self):
        self.largura, self.altura = 30, 30
        self.x = randint(0, screen_width-self.largura)
        self.y = randint(0, screen_height-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (randint(20, 255), randint(20, 255), randint(20, 255))

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)



def draw_blue_circle(x,y):    
    pygame.draw.circle(screen, BLUE, (x, y), 50)
    
def addText():
    font = pygame.font.Font(None, 24)    
    screen.blit(font.render('Clique!', True, BLACK), (x-25, y-5))
    
def draw_rect_yellow():
    square_width, square_height = 50, 50
    a, b = randint(0, screen_height - square_height), randint(0, screen_width - square_width) 
    pygame.draw.rect(screen, YELLOW, (a,b,square_width, square_height))
    
   
        
def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)
    
terminou = False
while not terminou:  
    write_text("Question 8 - AT") 
    pygame.display.update()    
    draw_blue_circle(x, y)
    addText() 
    
    teste = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
                                
            if pos[0] >= 350 and pos[0] <= 450 and pos[1] >= 30 and pos[1] <= 130:            
                draw_rect_yellow()                
                """ for q in areas:
                    if q.area.collidelist(pos):
                        areas.remove(q) """
                
                   
                          
pygame.display.quit()
pygame.quit()