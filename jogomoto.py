import pygame
import random
import time

# Inicializa o pygame
pygame.init()

# Define as cores utilizadas no jogo
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Define as dimensões da tela
LARGURA_TELA = 800
ALTURA_TELA = 600

# Define as dimensões da moto
LARGURA_MOTO = 75
ALTURA_MOTO = 50

# Define as dimensões dos carros
LARGURA_CARRO = 50
ALTURA_CARRO = 50

# Define a velocidade da moto
VELOCIDADE_MOTO = 5

# Define a velocidade dos carros
VELOCIDADE_CARRO = 10

# Define a posição inicial da moto
POSICAO_MOTO_X = LARGURA_TELA / 2 - LARGURA_MOTO / 2
POSICAO_MOTO_Y = ALTURA_TELA - ALTURA_MOTO - 10

# Define o tempo máximo para reparar o carro
TEMPO_MAXIMO_REPARO = 10

# Define a classe da moto
class Moto(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([LARGURA_MOTO, ALTURA_MOTO])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.rect.x = POSICAO_MOTO_X
        self.rect.y = POSICAO_MOTO_Y
    
    def mover_esquerda(self):
        self.rect.x -= VELOCIDADE_MOTO
        if self.rect.x < 0:
            self.rect.x = 0
    
    def mover_direita(self):
        self.rect.x += VELOCIDADE_MOTO
        if self.rect.x > LARGURA_TELA - LARGURA_MOTO:
            self.rect.x = LARGURA_TELA - LARGURA_MOTO
    
    def mover_cima(self):
        self.rect.y -= VELOCIDADE_MOTO
        if self.rect.y < 0:
            self.rect.y = 0
    
    def mover_baixo(self):
        self.rect.y += VELOCIDADE_MOTO
        if self.rect.y > ALTURA_TELA - ALTURA_MOTO:
            self.rect.y = ALTURA_TELA - ALTURA_MOTO

# Define a classe dos carros
class Carro(pygame.sprite.Sprite):
    def __init__(self, velocidade):
        super().__init__()
        self.image = pygame.Surface([LARGURA_CARRO, ALTURA_CARRO])
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(LARGURA_TELA - LARGURA_CARRO)
        self.rect.y = random.randrange(-100, -ALTURA_CARRO)
        self.velocidade = velocidade
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > ALTURA_TELA:
            self.rect.x = random.randrange(LARGURA_TELA - LARGURA_CARRO)
            self.rect.y = random.randrange(-100, -ALTURA_CARRO)
            self.velocidade = random.randrange(VELOCIDADE_CARRO - 5, VELOCIDADE_CARRO + 5)
