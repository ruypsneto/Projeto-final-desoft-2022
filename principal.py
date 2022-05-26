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

lista_posicoes = []
for i in range(3):
    carros = cs.Carros(lista_posicoes)
    all_sprites.add(carros)
    all_carros.add(carros)


# Criando o jogador
player = cs.Jogador(ast.carros['jogador'])
all_sprites.add(player)




















clock = pygame.time.Clock()
FPS = 30

pista = 0

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
    hits = pygame.sprite.spritecollide(player, all_carros, True)
    if len(hits) > 0:
        game = False


    pista = pista % HEIGHT
    window.fill((0, 0, 0))  
    window.blit(ast.fundos['bambus'], (0, pista))
    window.blit(ast.fundos['bambus'], (0, (pista - HEIGHT)))
    

    pista+=1
    all_sprites.draw(window)


    pygame.display.update()











pygame.quit() 