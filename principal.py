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



state = ast.inicio


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
FPS = 60

pista = 0
pisca = 0

game = True

# ===== Loop principal =====
while game:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # tela de inicio 
        
        if state == ast.inicio:
            window.fill((0, 0, 0))
            window.blit(ast.fundos['inicio'], (0, 0))
            # Verifica se o usuario passou o mouse por cima do botao
            print(mouse)
            if mouse[0]<= 100 and mouse[1]<= 100:
                window.blit(ast.cor_pb['cidade'], (100, 100))

                if event.type == pygame.MOUSEBUTTONDOWN:
                   
                    mapa = 'cidade'
                    state = ast.antes_de_start 
            if mouse[0]<= 300 and mouse[1]<= 100:
                window.blit(ast.cor_pb['bambus'], (300,100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mapa = 'bambus'
                    state = ast.antes_de_start
            if mouse[0]<= 500 and mouse[1]<= 100:
                window.blit(ast.cor_pb['praia'], (500, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mapa = 'praia'
                    state = ast.antes_de_start
            if event.type == pygame.QUIT:
                game = False

            pygame.display.update()
    


        elif state == ast.antes_de_start :
            # rodando o jogo 
            if event.type == pygame.KEYUP:
                if event.type == pygame.QUIT:
                    game = False
                #gera fundo 
                window.fill((0, 0, 0))  
                window.blit(ast.fundos[mapa], (0, 0))

                #     Precione enter/ return para iniciar o jogo
                # define cor do start  
                if mapa == 'cidade':
                    cor_start = (255, 0, 0)
                if mapa == 'bambus':
                    cor_start = (0,255,0)
                if mapa == 'praia':
                    cor_start = (255,255,0)


                text_surface = ast.score_font.render("Press enter to START", True, cor_start)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH / 2, HEIGHT/2)
                window.blit(text_surface, text_rect)
                pygame.display.update()
                state = ast.jogando
            
              
                
            
            
 
        elif state == ast.jogando :     
            distancia = 0
            vida = 3
            correndo = True
            while correndo :
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # Dependendo da tecla, altera a velocidade.
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx -= 1
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx += 1
                    # Verifica se soltou alguma tecla.
                    if event.type == pygame.KEYUP:
                        # Dependendo da tecla, altera a velocidade.
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx += 1
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx -= 1
                    if event.type == pygame.QUIT:
                        game = False
                        correndo = False
                        break
                
                all_sprites.update()
                #  verifica colições 
                hits = pygame.sprite.spritecollide(player, all_carros, True)
                if len(hits) > 0:
                    c = cs.Carros(lista_posicoes)
                    all_sprites.add(c)
                    all_carros.add(c)
                    distancia = 0 
                    vida -= 2
                    if vida == 0:
                        correndo = False
                        state = ast.morto
                        mapa = 'gameover'
                        break

                     

                if distancia % 1000 == 0:
                    vida += 1 
                    if vida >= 7:
                        vida -= 1

                #  movimentp pista 
                pista = pista % HEIGHT
                window.fill((0, 0, 0))  
                window.blit(ast.fundos[mapa], (0, pista))
                window.blit(ast.fundos[mapa], (0, (pista - HEIGHT)))

                # vida 
                for i in range(0, vida):
                    text_surface = ast.score_font.render(chr(9829) * vida, True, (255, 0, 0))
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (10, HEIGHT - 10)
                    window.blit(text_surface, text_rect)
                

                pista+=1
                all_sprites.draw(window)


                # score aparece na tela 
                distancia += 1
                text_surface = ast.score_font.render("{} metros".format(distancia), True, cor_start)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH / 2,  10)
                window.blit(text_surface, text_rect)
                # salvando maior score
                dmax = 0
                if distancia > dmax:
                    dmax = distancia 



                pygame.display.update()

            
    
        elif state ==ast.morto:
            # depois que morre o player 
        

            if event.type == pygame.QUIT:
                game = False


            window.fill((0, 0, 0))  
            window.blit(ast.fundos[mapa], (0, 0))



            text_surface = ast.score_font.render("{} metros,  foi sua distancia maxima".format(dmax), True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  10)
            window.blit(text_surface, text_rect)
            pygame.display.update()











pygame.quit() 