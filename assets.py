import pygame


WIDTH = 480
HEIGHT = 600  

fundos = {}

fundos['praia'] = pygame.image.load('imagens/fundos/praia.png').convert()
fundos['praia'] = pygame.transform.scale(fundos['praia'],(WIDTH, HEIGHT))
fundos['cidade'] = pygame.image.load('imagens/fundos/cidade.png').convert()
fundos['cidade'] = pygame.transform.scale(fundos['cidade'],(WIDTH, HEIGHT))
fundos['bambus'] = pygame.image.load('imagens/fundos/bambus.png').convert()
fundos['bambus'] = pygame.transform.scale(fundos['bambus'],(WIDTH, HEIGHT))


carros = {}

WIDTH_carro =  60
HEIGHT_carro = 100

WIDTH_caminhao =  50
HEIGHT_caminhao = 200

carros['policia'] = pygame.image.load('imagens/carros/policia.png').convert()
carros['policia'] = pygame.transform.scale(carros['policia'],(WIDTH_carro, HEIGHT_carro))
carros['caminhao']= pygame.image.load('imagens/carros/caminhao.png').convert()
carros['caminhao']= pygame.transform.scale(carros['caminhao'],(WIDTH_caminhao, HEIGHT_caminhao))
carros['amarelo'] = pygame.image.load('imagens/carros/genericoamarelo.png').convert()
carros['amarelo'] = pygame.transform.scale(carros['amarelo'],(WIDTH_carro, HEIGHT_carro))
carros['verde'] = pygame.image.load('imagens/carros/genericoverde.png').convert()
carros['verde'] = pygame.transform.scale(carros['verde'],(WIDTH_carro, HEIGHT_carro))
carros['caminhaozinho'] = pygame.image.load('imagens/carros/caminhaozinho.png').convert()
carros['caminhaozinho'] = pygame.transform.scale(carros['caminhaozinho'],(WIDTH_carro, HEIGHT_carro))
carros['jogador'] = pygame.image.load('imagens/carros/jogador.png').convert()
carros['jogador'] = pygame.transform.scale(carros['jogador'],(WIDTH_carro, HEIGHT_carro))


