# aqui vamo colocar a principal do game
import pygame
# inicia o pygame
pygame.init()

#  definindo tamanho de tela 
WIDTH = 1200
HEIGHT =700 


WIDTH_RUA_A=  280
WIDTH_RUA_B = WIDTH-280
window = pygame.display.set_mode((WIDTH, HEIGHT))
#  imports aqui pois não estavam funcionando no topo 
import assets as ast 
import classes as cs  


pygame.display.set_caption('blimbots')


#  inicia o mixer
pygame.mixer.init()




state = ast.inicio

#  criando os sprites 
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
img_player = ast.carros['jogador']
all_player = pygame.sprite.Group()
all_player.add(player)
# all_sprites.add(player)









#  definindo velocidade dos fremes 
clock = pygame.time.Clock()
FPS = 30

pista = 0
pisca = 0
d_record = 0
game = True

# ===== Loop principal =====
while game:
    # pega possição do mouse
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # tela de inicio e onde se define o mapa jogado 
        
        if state == ast.inicio:
            #  fundos adicionados na tela 
            window.fill((0, 0, 0))
            window.blit(ast.fundos['inicio'], (0, 0))
            window.blit(ast.cor_pb['cidade_pb'], (200, 340))
            window.blit(ast.cor_pb['bambus_pb'], (500, 340))
            window.blit(ast.cor_pb['praia_pb'], (850, 340))


            if event.type == pygame.QUIT:
                game = False


            #  ira definir o mapa jogado
            # Verifica se o usuario passou o mouse por cima do botao
            if  mouse[0]>= 200 and mouse[1]>= 400 and mouse[1]<= 400+ ast.HEIGHT_INICIO and mouse[0]<= 200 + ast.WIDTH_INICIO :
                window.blit(ast.cor_pb['cidade'], (200, 340))
                window.blit(ast.sapo, (1000,90))

                # verifica se o usuario clicou no dentro da area definida
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.set_volume(ast.musicas['select'], 0.1)
                    ast.musicas['select'].play()
                   
                    mapa = 'cidade'
                    
                    state = ast.antes_de_start 
                    window.blit(ast.fundos[mapa], (0, 0))
                    
                    
            # Verifica se o usuario passou o mouse por cima do botao
            elif   mouse[0]>= 500 and mouse[1]>= 390 and mouse[1]<= 390+ ast.HEIGHT_INICIO and mouse[0]<= 500 + ast.WIDTH_INICIO :
                window.blit(ast.cor_pb['bambus'], (500,340))

                # verifica se o usuario clicou no dentro da area definida
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.set_volume(ast.musicas['select'], 0.1)
                    ast.musicas['select'].play()
                    mapa = 'bambus'
                    state = ast.antes_de_start
                    window.blit(ast.fundos[mapa], (0, 0))
                   
            # Verifica se o usuario passou o mouse por cima do botao
            elif  mouse[0]>= 850 and mouse[1]>= 400 and mouse[1]<= 400+ ast.HEIGHT_INICIO and mouse[0]<= 850 + ast.WIDTH_INICIO :

                window.blit(ast.cor_pb['praia'], (850, 340))

                # verifica se o usuario clicou no dentro da area definida
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.set_volume(ast.musicas['select'], 0.1)
                    ast.musicas['select'].play()
                    mapa = 'praia'
                    state = ast.antes_de_start
                    window.blit(ast.fundos[mapa], (0, 0))
                    
            
            





            pygame.display.update()



        #antes de rodar o jogor é necessario precionar enter para o jogador não ser pego de surpressa
        elif state == ast.antes_de_start :
            
            if event.type == pygame.QUIT:
                game = False

            cor_start= (200,100,200)
            window.fill((0, 0, 0))  
            window.blit(ast.fundos[mapa], (0, 0))
            text_surface = ast.score_font.render("Press enter to START", True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2, HEIGHT/2)
            window.blit(text_surface, text_rect)
        
            if event.type == pygame.KEYDOWN:
        
                
                if event.key == pygame.K_RETURN:

                    #     Precione enter/ return para iniciar o jogo
                    # define cor do start  
                    # define musica jogada 
                    if mapa == 'cidade':
                        cor_start = (255, 0, 0)
                        pygame.mixer.music.load('musicas/tokyo.wav')
                        
                    if mapa == 'bambus':
                        cor_start = (0,255,0)
                        pygame.mixer.music.load('musicas/bambus.wav')
                        
                    if mapa == 'praia':
                        cor_start = (255,255,0)
                        pygame.mixer.music.load('musicas/bandoleros.wav')

                    state = ast.jogando
            
            pygame.display.update()
        
              
                
            
        
    
        elif state == ast.jogando :     
            distancia = 0
            bateu = 0
            dmax = 0
            vida = 7    
            contador_batidas = 0
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(loops=-1)
            #  corrida inicia 
            while state == ast.jogando :

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
                        state = ast.state

                #  atualiza os sprites 
                all_player.update(img_player)
                all_sprites.update(distancia)


                #  verifica colições 
                hits = pygame.sprite.spritecollide(player, all_carros, True)
                if len(hits) > 0:
                   
                    if vida > 0:
                        c = cs.Carros(lista_posicoes)
                        all_sprites.add(c)
                        all_carros.add(c)
                        #  verifica a se o jogador ainda esta na ação de batida(rodou)
                        if bateu == 0:
                            pygame.mixer.Sound.set_volume(ast.musicas['crash'], 0.1)
                            pygame.mixer.Sound.set_volume(ast.musicas['ratinho'], 0.1)
                            ast.musicas['crash'].play()
                            ast.musicas['ratinho'].play()
                            rodou_texto = 0
                            distancia = distancia/2 
                            bateu = 1
                            vida -= 1
                           

                            
                    #  verifica se o player ainda tem vidas  
                    if vida <= 0:
                        player.speedx = 0
                        state = ast.morto
                        if len(all_carros)<4:
                            c = cs.Carros(lista_posicoes)
                            all_sprites.add(c)
                            all_carros.add(c)

                #  rotção do carro 
                if bateu >= 1:
                    bateu += 1
                    rodou_texto +=1
                    if 720/8 == bateu:
                        img_player = pygame.transform.rotate(img_player, 90)
                        contador_batidas +=1 

                    if bateu >= 720/8:
                        bateu = 1 
                    if contador_batidas == 8:
                        contador_batidas = 0
                        bateu = 0 


                #  aumenta a vida a cada distancia
                if distancia % 1000 == 0:
                    vida += 1 
                    if vida >= 7:
                        vida -= 1

                #  movimento pista 
                pista = pista % HEIGHT
                window.fill((0, 0, 0))  
                window.blit(ast.fundos[mapa], (0, pista))
                window.blit(ast.fundos[mapa], (0, (pista - HEIGHT)))
                pista+=1

                # faz com que apareça a quantidade vidas que o player tem na tela 
                for i in range(0, vida):
                    text_surface = ast.score_font.render(chr(9829) * vida, True, (255, 0, 0))
                    text_rect = text_surface.get_rect()
                    text_rect.bottomleft = (10, HEIGHT - 10)
                    window.blit(text_surface, text_rect)
                

                #    desenha sprites na tela
                all_sprites.draw(window)
                all_player.draw(window)

                # texto de quando bate ('RODOU')

                if bateu >= 1:
                    text_surface = ast.score_font.render("RODOU", True, cor_start)
                    text_rect = text_surface.get_rect()
                    text_surface = pygame.transform.scale(text_surface,(600, 100))
                    text_rect.midtop = ((WIDTH / 4)+ 80,  100)
                    window.blit(text_surface, text_rect)



                # score aparece na tela 
                distancia += 1
                text_surface = ast.score_font.render("{:.2f} metros".format(distancia/100), True, cor_start)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH / 2,  10)
                window.blit(text_surface, text_rect)

                # salvando maior score
                if distancia > dmax:
                    dmax = distancia 
                if distancia >= 150*100:
                    state = ast.vencedor



                pygame.display.update()

            
        
        # depois que morre o player
        if state ==ast.morto:
            mouse = pygame.mouse.get_pos()
           
            
            
            
    
            if event.type == pygame.QUIT:
                game = False

            #  mapa aparece na tela 
            window.fill((0, 0, 0)) 
            window.blit(ast.fundos['gameover'], (0,0)) 
           
            #    texto de distancia maxima atingida
            text_surface = ast.score_font.render("{:.2f} metros, foi sua distancia maxima".format(dmax/100), True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  10)
            window.blit(text_surface, text_rect)
          
            # texto de 'quer continuar'
            text_surface = ast.score_font.render("Quer continuar?", True, cor_start)
            text_rect = text_surface.get_rect()
            text_surface = pygame.transform.scale(text_surface,(600, 100))
            text_rect.midtop = ((WIDTH / 3)+ 100,  150)
            window.blit(text_surface, text_rect)


            # verifica se o mouse do player esta dentro da area definida
            if  mouse[0]>= 300 and mouse[1]>= 360 and mouse[0]<= 500 and mouse[1]<= 470 :
                cor = (30,30, 30)
                vertices = [(300, 360),(500, 360),(500, 470),(300, 470)]
                pygame.draw.polygon(window, cor, vertices)


                # verifica se clicou dentro da area definida
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # reinicia sprites 
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
                    img_player = ast.carros['jogador']
                    all_player = pygame.sprite.Group()
                    all_player.add(player)

                    state = ast.antes_de_start

            
            # verifica se o mouse do player esta dentro da area definida
            if  mouse[0]>= (300+(WIDTH / 3)) and mouse[1]>= 360 and mouse[1]<= 470 and mouse[0]<= 500+(WIDTH / 3) :
                cor = (30,30, 30)
                vertices = [(300+(WIDTH / 3), 360),(500+(WIDTH / 3), 360),(500+(WIDTH / 3), 470),(300+(WIDTH / 3), 470)]
                pygame.draw.polygon(window, cor, vertices)


                # verifica se clicou dentro da area definida
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # pausa a musica
                    pygame.mixer.music.pause()
                     # reinicia sprites 
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
                    img_player = ast.carros['jogador']
                    all_player = pygame.sprite.Group()
                    all_player.add(player)

                    state = ast.inicio






            #  texto para respostas do jogador (sim/não)
            text_surface = ast.score_font.render("YES", True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 3,  400)
            window.blit(text_surface, text_rect)

            text_surface = ast.score_font.render("NO", True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = ((WIDTH / 3)* 2, 400)
            window.blit(text_surface, text_rect)



            pygame.display.update()
        

        elif state == ast.vencedor:
            if event.type == pygame.QUIT:
                game = False

            #  mapa aparece na tela 
            window.fill((0, 0, 0)) 
            window.blit(ast.fundos['gameover'], (0,0)) 
           
            #    texto de distancia maxima atingida
            text_surface = ast.score_font.render("Você venceu!!!", True, cor_start)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  10)
            window.blit(text_surface, text_rect)
          
            # texto de 'quer continuar'
            text_surface = ast.score_font.render("Agora vc faz parte da famila", True, cor_start)
            text_rect = text_surface.get_rect()
            text_surface = pygame.transform.scale(text_surface,(600, 100))
            text_rect.midtop = ((WIDTH / 3)+ 100,  150)
            window.blit(text_surface, text_rect)



            pygame.display.update()










#  fecha o pygame 
pygame.quit() 