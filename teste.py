import pygame
from random import randint

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
BRANCO, PRETO = (255, 255, 255), (0, 0, 0)
a, b = largura_tela/2, 80
square_width, square_height = 50, 50
screen_width, screen_height = 800, 600

RED, BLUE = (255, 0, 0), (0, 0, 255)
YELLOW = (255,255,0)
terminou = False

tela.fill(PRETO)


class Quadradinho():
    def __init__(self):
        self.largura, self.altura = 50, 50
        self.x = randint(0, largura_tela-self.largura)
        self.y = randint(0, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = YELLOW

    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
    
    def draw_blue_circle(x,y):    
        pygame.draw.circle(tela, BLUE, (a, b), 50)
    
    def addText():
        font = pygame.font.Font(None, 24)    
        tela.blit(font.render('Clique!', True, PRETO), (a-25, b-5))


def write_text(text):
    font = pygame.font.Font(None, 24)
    text = font.render(text, 1, BRANCO)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)









terminou = False
while not terminou:
    write_text("Question 8 - AT") 
    pygame.display.update()
    Quadradinho.draw_blue_circle(a, b)
    Quadradinho.addText()
    


    lista_quadrinhos = []
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:            
            pos = pygame.mouse.get_pos()
                       
            q = Quadradinho()
            q.desenha(tela)
            lista_quadrinhos.append(q)
                
            for q in lista_quadrinhos:
                if q.area.collidepoint(pos): 
                    print(q.area.collidepoint(pos))                   
                    lista_quadrinhos.remove(q)
                    
      


pygame.display.quit()
pygame.quit()
