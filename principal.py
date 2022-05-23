# aqui vamo colocar a principal do game
import pygame
pygame.init()


WIDTH = 1200
HEIGHT =700 


WIDTH_RUA_A=  280
WIDTH_RUA_B = WIDTH-280
window = pygame.display.set_mode((WIDTH, HEIGHT))

import assets as ast
import classes as cs  


pygame.display.set_caption('blimbots')









all_sprites = pygame.sprite.Group()
all_carros = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_carros'] = all_carros

# Criando o jogador
player = cs.Jogador(ast.carros['jogador'])
all_sprites.add(player)


tipo_do_carro = cs.aleatorio()
carros = cs.Carros(ast.carros['policia'])
all_carros.add(carros)


















clock = pygame.time.Clock()
FPS = 30


game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 1
            if event.key == pygame.K_RIGHT:
                player.speedx += 1
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 1
            if event.key == pygame.K_RIGHT:
                player.speedx -= 1
        if event.type == pygame.QUIT:
            game = False

    all_sprites.update()

    
    window.fill((0, 0, 0))  
    window.blit( ast.fundos['cidade'] , (0, 0))
    
    all_sprites.draw(window)

    pygame.display.update()











pygame.quit() 