import pygame


WIDTH = 700
HEIGHT = 800  


WIDTH_RUA_A=  160
WIDTH_RUA_B = WIDTH-160

fundos = {}

fundos['praia'] = pygame.image.load('imagens/fundos/praia.png').convert()
fundos['praia'] = pygame.transform.scale(fundos['praia'],(WIDTH, HEIGHT))
fundos['cidade'] = pygame.image.load('imagens/fundos/cidade.png').convert()
fundos['cidade'] = pygame.transform.scale(fundos['cidade'],(WIDTH, HEIGHT))
fundos['bambus'] = pygame.image.load('imagens/fundos/bambus.png').convert()
fundos['bambus'] = pygame.transform.scale(fundos['bambus'],(WIDTH, HEIGHT))


carros = {}

WIDTH_CARRO =  60
HEIGHT_CARRO = 100

WIDTH_CAMINHAO =  50
HEIGHT_CAMINHAO = 200

carros['policia'] = pygame.image.load('imagens/carros/policia.png').convert()
carros['policia'] = pygame.transform.scale(carros['policia'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['caminhao']= pygame.image.load('imagens/carros/caminhao.png').convert()
carros['caminhao']= pygame.transform.scale(carros['caminhao'],(WIDTH_CAMINHAO, HEIGHT_CAMINHAO))
carros['amarelo'] = pygame.image.load('imagens/carros/genericoamarelo.png').convert()
carros['amarelo'] = pygame.transform.scale(carros['amarelo'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['verde'] = pygame.image.load('imagens/carros/genericoverde.png').convert()
carros['verde'] = pygame.transform.scale(carros['verde'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['caminhaozinho'] = pygame.image.load('imagens/carros/caminhaozinho.png').convert()
carros['caminhaozinho'] = pygame.transform.scale(carros['caminhaozinho'],(WIDTH_CARRO, HEIGHT_CARRO))
carros['jogador'] = pygame.image.load('imagens/carros/jogador.png').convert()
carros['jogador'] = pygame.transform.scale(carros['jogador'],(WIDTH_CARRO, HEIGHT_CARRO))


