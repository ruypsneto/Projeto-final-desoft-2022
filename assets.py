import pygame
pygame.mixer.init()
# estados do jogo
state = 0
inicio = 1
jogando = 2
morto = 3
antes_de_start = 4
vencedor = 5
mapa = ''
#  tamanho tela 
WIDTH = 1200    
HEIGHT = 700 

# tamanho da rua 
WIDTH_RUA_A=  280
WIDTH_RUA_B = WIDTH-280

#  fazendo load dos fundos 
fundos = {}

fundos['praia'] = pygame.image.load('imagens/fundos/praia.png').convert()
fundos['praia'] = pygame.transform.scale(fundos['praia'],(WIDTH, HEIGHT))
fundos['cidade'] = pygame.image.load('imagens/fundos/cidade.png').convert()
fundos['cidade'] = pygame.transform.scale(fundos['cidade'],(WIDTH, HEIGHT))
fundos['bambus'] = pygame.image.load('imagens/fundos/bambus.png').convert()
fundos['bambus'] = pygame.transform.scale(fundos['bambus'],(WIDTH, HEIGHT))
fundos['inicio'] = pygame.image.load('imagens/fundos/inicio.png').convert()
fundos['inicio'] =  pygame.transform.scale(fundos['inicio'],(WIDTH, HEIGHT))
fundos['gameover'] = pygame.image.load('imagens/fundos/game_over.jpg').convert()
fundos['gameover'] =  pygame.transform.scale(fundos['gameover'],(WIDTH, HEIGHT))


#  fazendo os loads dos cards pos mapas
WIDTH_INICIO = 150
HEIGHT_INICIO =300
cor_pb = {}

cor_pb['praia_pb'] = pygame.image.load('imagens/fundos/inicio_praia_pb.png').convert()
cor_pb['praia_pb'] = pygame.transform.scale(cor_pb['praia_pb'],(WIDTH_INICIO, HEIGHT_INICIO))
cor_pb['praia'] = pygame.image.load('imagens/fundos/inicio_praia.png').convert()
cor_pb['praia'] = pygame.transform.scale(cor_pb['praia'],(WIDTH_INICIO, HEIGHT_INICIO))
cor_pb['cidade_pb'] = pygame.image.load('imagens/fundos/inicio_cidade_pb.png').convert()
cor_pb['cidade_pb'] = pygame.transform.scale(cor_pb['cidade_pb'],(WIDTH_INICIO, HEIGHT_INICIO))
cor_pb['cidade'] = pygame.image.load('imagens/fundos/inicio_cidade.png').convert()
cor_pb['cidade'] = pygame.transform.scale(cor_pb['cidade'],(WIDTH_INICIO, HEIGHT_INICIO))
cor_pb['bambus_pb'] = pygame.image.load('imagens/fundos/inicio_bambus_pb.png').convert()
cor_pb['bambus_pb'] = pygame.transform.scale(cor_pb['bambus_pb'],(WIDTH_INICIO, HEIGHT_INICIO))
cor_pb['bambus'] = pygame.image.load('imagens/fundos/inicio_bambus.png').convert()
cor_pb['bambus'] = pygame.transform.scale(cor_pb['bambus'],(WIDTH_INICIO, HEIGHT_INICIO))




# load das imagens dos carros(player e inimigos) 
carros = {}

WIDTH_CARRO =  80
HEIGHT_CARRO = 130

WIDTH_CAMINHAO =  80
HEIGHT_CAMINHAO = 160

carros['policia'] = pygame.image.load('imagens/carros/policia.png').convert_alpha()
carros['policia'] = pygame.transform.scale(carros['policia'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['caminhao']= pygame.image.load('imagens/carros/caminhao.png').convert_alpha()
carros['caminhao']= pygame.transform.scale(carros['caminhao'],(WIDTH_CAMINHAO, HEIGHT_CAMINHAO))
carros['amarelo'] = pygame.image.load('imagens/carros/genericoamarelo.png').convert_alpha()
carros['amarelo'] = pygame.transform.scale(carros['amarelo'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['verde'] = pygame.image.load('imagens/carros/genericoverde.png').convert_alpha()
carros['verde'] = pygame.transform.scale(carros['verde'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['caminhaozinho'] = pygame.image.load('imagens/carros/caminhaozinho.png').convert_alpha()
carros['caminhaozinho'] = pygame.transform.scale(carros['caminhaozinho'],(WIDTH_CAMINHAO, HEIGHT_CAMINHAO))
carros['jogador'] = pygame.image.load('imagens/carros/jogador.png').convert_alpha()
carros['jogador'] = pygame.transform.scale(carros['jogador'],(WIDTH_CARRO, HEIGHT_CARRO))

#  é o sapo 
sapo = pygame.image.load('imagens/fundos/sapo.png').convert_alpha()
sapo = pygame.transform.scale(sapo,(80, 50))

# fonte para textos 
score_font = pygame.font.Font('musicas/PressStart2P.ttf', 28)



#  loads de sons 
musicas = {}
musicas['select'] = pygame.mixer.Sound('musicas/selct_.wav')
musicas['ratinho'] = pygame.mixer.Sound('musicas/ratinho.wav')
musicas['crash'] = pygame.mixer.Sound('musicas/acidente.wav')





