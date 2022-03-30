import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2   # Posição X inicial do retângulo vermelho
y = altura/2   # Posição Y inicial do retângulo vermelho
x_azul = randint(40, 600)
y_azul = randint(50, 430)
cont = 0   # Contador de colisões
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

pygame.display.set_caption('Tentando')

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            print(f'O jogador colidiu {cont} vezes!!!')
            exit()
    if pygame.key.get_pressed()[K_a]:
        x -= 15
    if pygame.key.get_pressed()[K_d]:
        x += 15
    if pygame.key.get_pressed()[K_w]:
        y -= 15
    if pygame.key.get_pressed()[K_s]:
        y += 15
    vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50)) # largura do retângulo == 40, altura == 50
    azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
    if vermelho.colliderect(azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        cont += 1
    pygame.display.update()
