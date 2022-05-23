import pygame


WIDTH = 480
HEIGHT = 600  

fundos = {}

fundos['praia'] = pygame.image.load('imagens/fundos/praia.png').convert()
fundos['praia'] = pygame.transform.scale(fundos['praia'],(WIDTH, HEIGHT))


carros = {}
carros['jogador'] = pygame.image.load('imagens/carros/policia.png').convert()
carros['caminhao']= pygame.image.load('imagens/carros/caminhao.png').convert()


