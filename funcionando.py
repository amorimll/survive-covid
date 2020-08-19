import pygame
import math
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

current_time = 0

pygame.display.set_caption("Survive Covid")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('carrinho.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 370
playerY = 480
playerX_change = 0

feijaoImg = pygame.image.load('feijao.png')
feijaoImg = pygame.transform.scale(feijaoImg, (50, 50))
feijaoX = random.randint(0, 700)
feijaoY = -60
feijaoY_change = 0.175

arrozImg = pygame.image.load('arroz.png')
arrozImg = pygame.transform.scale(arrozImg, (50, 50))
arrozX = random.randint(0, 700)
arrozY = -1000
arrozY_change = 0.230

gelImg = pygame.image.load('gel.png')
gelImg = pygame.transform.scale(gelImg, (50, 50))
gelX = random.randint(0, 700)
gelY = -3000
gelY_change = 0.3



score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

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

running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    current_time = pygame.time.get_ticks()

    clock.tick(1000)

    feijaoY += feijaoY_change
    arrozY += arrozY_change
    gelY += gelY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    collision = isCollisionFeijao(playerX, playerY, feijaoX, feijaoY)
    if collision:
        feijaoX = random.randint(0, 770)
        feijaoY = -60
        score += 5
        print(score)

    collision = isCollisionArroz(playerX, playerY, arrozX, arrozY)
    if collision:
        arrozX = random.randint(0, 700)
        arrozY = -60
        score += 10
        print(score)
    
    collision = isCollisionGel(playerX, playerY, gelX, gelY)
    if collision:
        gelX = random.randint(0, 700)
        gelY = -60
        score += 20
        print(score)
    
    if feijaoY >= 600:
        feijaoX = random.randint(0, 700)
        feijaoY = -60
        score -=5
        print(score)

    if arrozY >= 600:
        arrozX = random.randint(0, 770)
        arrozY = -60
        score -=10
    
    if gelY >= 600:
        gelX = random.randint(0, 770)
        gelY = -60
        score -=20
    
    if current_time >= 3000:
        arroz(arrozX, arrozY)
    
    if current_time >= 10000:
        gel(gelX, gelY)

    player(playerX, playerY)
    feijao(feijaoX, feijaoY)
    pygame.display.update()

    