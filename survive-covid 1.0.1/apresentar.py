# -*- coding: cp1252 -*-

import pygame
import math
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load('Imagens/background.png')

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

playerImg = pygame.image.load('Imagens/carrinho.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 400
playerY = 480
playerX_change = 0

covidImg = pygame.image.load('Imagens/covid.png')
covidImg = pygame.transform.scale(covidImg, (50, 50))
covidX = random.randint(0, 700)
covidY = -15000
covidY_change = 2.5

feijaoImg = pygame.image.load('Imagens/feijao.png')
feijaoImg = pygame.transform.scale(feijaoImg, (50, 50))
feijaoX = random.randint(0, 700)
feijaoY = -60
feijaoY_change = 1.5

arrozImg = pygame.image.load('Imagens/arroz.png')
arrozImg = pygame.transform.scale(arrozImg, (50, 50))
arrozX = random.randint(0, 700)
arrozY = -3000
arrozY_change = 2

gelImg = pygame.image.load('Imagens/gel.png')
gelImg = pygame.transform.scale(gelImg, (50, 50))
gelX = random.randint(0, 700)
gelY = -8000
gelY_change = 2.5

def show_score(x, y):
    score = font.render("Pontos: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_vida(x, y):
    vida = font.render("Vida: " + str(vida_value), True, (255, 255, 255))
    screen.blit(vida, (x, y))

def show_combo(x, y):
    combo = font.render("Combo: x" + str(multiplicador), True, (255, 255, 255))
    screen.blit(combo, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))
    
def covid(x, y):
    screen.blit(covidImg, (x, y))

def feijao(x, y):
    screen.blit(feijaoImg, (x, y))

def arroz(x, y):
    screen.blit(arrozImg, (x, y))
    
def gel(x, y):
    screen.blit(gelImg, (x, y))

def isCollisionCovid(playerX, playerY, covidX, covidY):
    distance = math.sqrt((math.pow(playerX-covidX,2)) + (math.pow(playerY-covidY,2)))
    if distance < 65:
        return True
    else:
        return False

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

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    current_time = pygame.time.get_ticks()

    covidY += covidY_change
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

    collision = isCollisionCovid(playerX, playerY, covidX, covidY)
    if collision:

        soma_covid = 0
        covidMultiplicado = multiplicador * soma_covid
        covidX = random.randint(0, 770)
        covidY = -60
        covidY_change += 0.02
        score_value += covidMultiplicado
        playerX_change += 0.02
        combo_value += 0
        vida_value -=5

    collision = isCollisionFeijao(playerX, playerY, feijaoX, feijaoY)
    if collision:

        soma_feijao = 5
        feijaoMultiplicado = multiplicador * soma_feijao
        feijaoX = random.randint(0, 770)
        feijaoY = -60
        feijaoY_change += 0.02
        score_value += feijaoMultiplicado
        playerX_change += 0.02
        combo_value += 1
        vida_value +=1

    collision = isCollisionArroz(playerX, playerY, arrozX, arrozY)
    if collision:

        soma_arroz = 10
        arrozMultiplicado = multiplicador * soma_arroz
        arrozX = random.randint(0, 700)
        arrozY = -60
        arrozY_change += 0.02
        playerX_change += 0.02
        score_value += arrozMultiplicado
        combo_value += 1
        vida_value +=2
    
    collision = isCollisionGel(playerX, playerY, gelX, gelY)
    if collision:

        soma_gel = 20
        gelMultiplicado = multiplicador * soma_gel
        gelX = random.randint(0, 700)
        gelY = -60
        gelY_change += 0.02
        playerX_change += 0.02
        score_value += gelMultiplicado
        combo_value += 1
        vida_value +=3

    if covidY >= 600:
        covidX = random.randint(0, 700)
        covidY = -60
        covidY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=0
    
    if feijaoY >= 600:
        feijaoX = random.randint(0, 700)
        feijaoY = -60
        feijaoY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=1

    if arrozY >= 600:
        arrozX = random.randint(0, 770)
        arrozY = -60
        arrozY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=2
    
    if gelY >= 600:
        gelX = random.randint(0, 770)
        gelY = -60
        gelY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=3
    
    if current_time >= 10000:
        arroz(arrozX, arrozY)
    
    if current_time >= 25000:
        gel(gelX, gelY)
    
    if current_time >= 35000:
        covid(covidX, covidY)
    
    if vida_value >= 10:
        vida_value = 10
    
    if vida_value <= 0:
        vida_value = 0

    covid(covidX, covidY)
    player(playerX, playerY)
    feijao(feijaoX, feijaoY)
    show_score(scoreX, scoreY)
    show_combo(comboX, comboY)
    show_vida(vidaX, vidaY)
    pygame.display.update()

    