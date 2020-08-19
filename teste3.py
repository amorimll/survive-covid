import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Survive Covid")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('carrinho.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 370
playerY = 480
playerX_change = 0

frutaImg = pygame.image.load('fruta.png')
frutaImg = pygame.transform.scale(frutaImg, (50, 50))
frutaX = random.randint(0, 770)
frutaY = -60
frutaY_change = 0.2

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def fruta(x, y):
    screen.blit(frutaImg, (x, y))

def isCollision(playerX, playerY, frutaX, frutaY):
    distance = math.sqrt((math.pow(playerX-frutaX,2)) + (math.pow(playerY-frutaY,2)))
    if distance < 30:
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
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    frutaY += frutaY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    collision = isCollision(playerX, playerY, frutaX, frutaY)
    if collision:
        frutaX = random.randint(0, 770)
        frutaY = -60
        score += 1
        print(score)
    
    if frutaY >= 600:
        frutaX = random.randint(0, 770)
        frutaY = -60
        score -=1
        print(score)

    player(playerX, playerY)
    fruta(frutaX, frutaY)
    pygame.display.update()