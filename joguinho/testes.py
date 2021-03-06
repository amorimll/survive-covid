# -*- coding: cp1252 -*-

import pygame
import math
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

current_time = 0

vida_value = 10

multiplicador = 1

combo_value = 0

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)

scoreX = 10 
scoreY = 50

vidaX = 10
vidaY = 10

comboX = 10
comboY = 100

pygame.display.set_caption("Survive Covid")
icon = pygame.image.load('Imagens/icon.png')
pygame.display.set_icon(icon)

#playerImg = pygame.image.load('Imagens/carrinho.png')
#playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 400
playerY = 480
playerX_change = 0

feijaoImg = pygame.image.load('Imagens/feijao.png')
feijaoImg = pygame.transform.scale(feijaoImg, (50, 50))
feijaoX = random.randint(0, 700)
feijaoY = -60
feijaoY_change = 0.175

arrozImg = pygame.image.load('Imagens/arroz.png')
arrozImg = pygame.transform.scale(arrozImg, (50, 50))
arrozX = random.randint(0, 700)
arrozY = -3000
arrozY_change = 0.230

gelImg = pygame.image.load('Imagens/gel.png')
gelImg = pygame.transform.scale(gelImg, (50, 50))
gelX = random.randint(0, 700)
gelY = -6000
gelY_change = 0.3

class Player(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY):
        super().__init__()
        self.spritesRight = []
        self.spritesLeft = []
        self.is_animatingRight = False
        self.is_animatingLeft = False
        self.spritesRight.append(pygame.image.load("Imagens/player/PR.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R2.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R3.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R4.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R5.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R6.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R7.png"))
        self.spritesRight.append(pygame.image.load("Imagens/player/R8.png"))

        self.spritesLeft.append(pygame.image.load("Imagens/player/PL.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L1.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L2.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L3.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L4.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L5.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L6.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L7.png"))
        self.spritesLeft.append(pygame.image.load("Imagens/player/L8.png"))

        self.current_sprite = 0
        self.image = self.spritesRight[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect = [200, 280, 10, 10]
    
    def animateRight(self):
        self.is_animatingRight = True
    
    def animateLeft(self):
        self.is_animatingLeft = True
    
    def not_animateRight(self):
        self.is_animatingRight = False
        self.is_animatingLeft = False
        self.current_sprite = 0
        self.image = self.spritesRight[self.current_sprite]
    
    def not_animateLeft(self):
        self.is_animatingRight = False
        self.is_animatingLeft = False
        self.current_sprite = 0
        self.image = self.spritesLeft[self.current_sprite]

    def update(self):
        if self.is_animatingRight == True:
            self.current_sprite += 0.1

            if self.current_sprite >= len(self.spritesRight):
                self.current_sprite = 0

            self.image = self.spritesRight[int(self.current_sprite)]

        if self.is_animatingLeft == True:
            self.current_sprite += 0.1

            if self.current_sprite >= len(self.spritesLeft):
                self.current_sprite = 0

            self.image = self.spritesLeft[int(self.current_sprite)]

def show_score(x, y):
    score = font.render("Pontos: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_vida(x, y):
    vida = font.render("Vida: " + str(vida_value), True, (255, 255, 255))
    screen.blit(vida, (x, y))

def show_combo(x, y):
    combo = font.render("Combo: x" + str(multiplicador), True, (255, 255, 255))
    screen.blit(combo, (x, y))

def feijao(x, y):
    screen.blit(feijaoImg, (x, y))

def arroz(x, y):
    screen.blit(arrozImg, (x, y))
    
def gel(x, y):
    screen.blit(gelImg, (x, y))

def isCollisionFeijao(playerX, playerY, feijaoX, feijaoY):
    distance = math.sqrt((math.pow(playerX-feijaoX,2)) + (math.pow(playerY-feijaoY,2)))
    if distance < 65:
        return True
    else:
        return False

def isCollisionArroz(playerX, playerY, arrozX, arrozY):
    distance = math.sqrt((math.pow(playerX-arrozX,2)) + (math.pow(playerY-arrozY,2)))
    if distance < 65:
        return True
    else:
        return False

def isCollisionGel(playerX, playerY, gelX, gelY):
    distance = math.sqrt((math.pow(playerX-gelX,2)) + (math.pow(playerY-gelY,2)))
    if distance < 65:
        return True
    else:
        return False

moving_spritesRight = pygame.sprite.Group()
moving_spritesLeft = pygame.sprite.Group()
playerChar = Player(playerX, playerY)
moving_spritesRight.add(playerChar)
moving_spritesLeft.add(playerChar)

running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
                playerChar.animateLeft()
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.8
                playerChar.animateRight()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerChar.not_animateLeft()
                playerX_change = 0

            if event.key == pygame.K_RIGHT:
                playerChar.not_animateRight()
                playerX_change = 0
    current_time = pygame.time.get_ticks()

    feijaoY += feijaoY_change
    arrozY += arrozY_change
    gelY += gelY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    if combo_value >= 5:
        multiplicador = 2

    if combo_value >= 10:
        multiplicador = 4

    if combo_value >= 15:
        multiplicador = 6

    collision = isCollisionFeijao(playerX, playerY, feijaoX, feijaoY)
    if collision:

        soma_feijao = 5
        feijaoMultiplicado = multiplicador * soma_feijao
        feijaoX = random.randint(0, 770)
        feijaoY = -60
        playerX_change += 0.002
        feijaoY_change += 0.002
        score_value += feijaoMultiplicado
        combo_value += 1
        vida_value +=1
        print(f"Sua vida agora é {vida_value}!")

    collision = isCollisionArroz(playerX, playerY, arrozX, arrozY)
    if collision:

        soma_arroz = 10
        arrozMultiplicado = multiplicador * soma_arroz
        arrozX = random.randint(0, 700)
        arrozY = -60
        playerX_change += 0.002
        arrozY_change += 0.002
        score_value += arrozMultiplicado
        combo_value += 1
        vida_value +=2
        print(f"Sua vida agora é {vida_value}!")
    
    collision = isCollisionGel(playerX, playerY, gelX, gelY)
    if collision:

        soma_gel = 20
        gelMultiplicado = multiplicador * soma_gel
        gelX = random.randint(0, 700)
        gelY = -60
        playerX_change += 0.002
        gelY_change += 0.002
        score_value += gelMultiplicado
        combo_value += 1
        vida_value +=3
        print(f"Sua vida agora é {vida_value}!")
    
    if feijaoY >= 600:
        feijaoX = random.randint(0, 700)
        feijaoY = -60
        playerX_change += 0.002
        feijaoY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -=1
        print(f"Sua vida agora é {vida_value}!")

    if arrozY >= 600:
        arrozX = random.randint(0, 770)
        arrozY = -60
        playerX_change += 0.002
        arrozY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -=2
        print(f"Sua vida agora é {vida_value}!")
    
    if gelY >= 600:
        gelX = random.randint(0, 770)
        gelY = -60
        playerX_change += 0.002
        gelY_change += 0.002
        combo_value = 0
        multiplicador = 1
        vida_value -=3
        print(f"Sua vida agora é {vida_value}!")
    
    if current_time >= 10000:
        arroz(arrozX, arrozY)
    
    if current_time >= 25000:
        gel(gelX, gelY)
    
    if vida_value >= 10:
        vida_value = 10
    
    if vida_value <= 0:
        vida_value = 0
    

    feijao(feijaoX, feijaoY)
    show_score(scoreX, scoreY)
    show_combo(comboX, comboY)
    show_vida(vidaX, vidaY)

    moving_spritesRight.draw(screen)
    moving_spritesRight.update()
    moving_spritesLeft.draw(screen)
    moving_spritesLeft.update()
    pygame.display.flip()

    