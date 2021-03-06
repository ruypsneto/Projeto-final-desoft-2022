# vamos colocar aqui as funcoes para o jogo
import pygame
import assets as ast 
import random



WIDTH = 1200
HEIGHT = 700 


WIDTH_RUA_A=  280
WIDTH_RUA_B = WIDTH-280


#  gera qual carro sera escolhido para o inimigo
def aleatorio():
    posiveis= ['policia', 'caminhaozinho', 'verde', 'amarelo']
    a= random.choice(posiveis)
    return a 



    



#  classe do jogador
class Jogador(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self, img):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        self.image = img

        # Mantem dentro da tela
        if self.rect.right > WIDTH_RUA_B:
            self.rect.right = WIDTH_RUA_B
        if self.rect.left < WIDTH_RUA_A:
            self.rect.left = WIDTH_RUA_A

#  classe dos inimigos 
class Carros(pygame.sprite.Sprite):
    def __init__(self, lista):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = ast.carros[aleatorio()]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH_RUA_A, (WIDTH_RUA_B-130))
        lista.append(self.rect.x)
        self.rect.y = -600
        self.speedy = random.randint(1,2)

    def update(self, distancia):
        # Atualização da posição da nave
        self.rect.y += self.speedy
  

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT+400:
            self.image = ast.carros[aleatorio()]


            a = random.randint(WIDTH_RUA_A, self.rect.x)
            b =  random.randint(self.rect.x, (WIDTH_RUA_B-130)) 
            self.rect.x = random.choice([a, b])
            self.rect.y = 0
            self.speedy = random.randint(1,2)
            if distancia >= 1000:
                self.speedy = random.randint(2,3)

        


