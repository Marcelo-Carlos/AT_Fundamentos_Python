#Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, 
# ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, 
# o retângulo que participou da colisão deve desaparecer.
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
x, y = screen_width/2, screen_height/2

class Teclas:
    def __init__(self, w, a, s, d):
        self.w = w
        self.a = a
        self.s = s
        self.d = d
        
        

teclas = Teclas(False, False, False, False)


def draw_blue_circle(x,y):
    cor = YELLOW    
    pygame.draw.circle(screen, YELLOW, (x, y), 50)
    
def addText():
    font = pygame.font.Font(None, 24)    
    screen.blit(font.render('Clique!', True, BLACK), (x-25, y-5))
    
def draw_rect_yellow():
    cor = YELLOW
    square_width, square_height = 50, 50
    x, y = randint(0, screen_heigth - square_height), randint(0, screen_width - square_width) 
    pygame.draw.rect(screen, cor, (x,y,square_width, square_height))
        
def move_element(teclas, x,y):
    if teclas.w and y > 0:
        y -= 2    
    elif teclas.w and y == 0:
        y = screen_width 
    elif teclas.a and y < screen_height:
        y += 2
    elif teclas.a and y == screen_height:
        y = 0
        
    elif teclas.s and x > 0:
        x -= 2
    elif teclas.s and x == 0:
        x -= 2
    elif teclas.s and x < 0:
        x = screen_width
        
    elif teclas.d and x < screen_width:
        x += 2
    elif teclas.d and x == screen_width:
        x += 2
    elif teclas.d and x > screen_width:
        x = 0
    return x,y    

def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, WHITE)
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)


terminou = False
while not terminou:
    screen.fill(BLACK)    
    write_text("Question 8 - AT")    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        #Enquanto estiver pressionado     
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                teclas.w = True
            elif event.key == K_a:
                teclas.a = True
            if event.key == K_s:
                teclas.s = True
            if event.key == K_d:
                teclas.d = True
        #Momento que parar a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                teclas.w = False
            elif event.key == pygame.K_a:
                teclas.a = False
            elif event.key == pygame.K_s:
                teclas.s = False
            elif event.key == pygame.K_d:
                teclas.d = False        
                            
    x, y = move_element(teclas, x, y)
    draw_blue_circle(x, y)
    addText()   
    pygame.display.update() 
             
pygame.display.quit()
pygame.quit()