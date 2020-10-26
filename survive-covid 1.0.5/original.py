# coding: iso-8859-1 -*-

#Bibliotecas que estão sendo importadas.

import pygame
import math
import random
import time

#Inicia o pygame.

pygame.init()

#Variável definindo o largura e a altura da tela, respectivamente.
screen = pygame.display.set_mode((800,600))

#Variável definindo o plano de fundo.

background = pygame.image.load('survive-covid 1.0.5/Imagens/background.png')

#Objeto da biblioteca time, que conta os segundos que se passaram desde o inicio do aplicativo.

current_time = 0

#Variável contendo o valor da vida do jogador.

vida_value = 10

#Variável contendo o valor do multiplicador de pontos.

multiplicador = 1

#Variável contendo o valor de quantos itens o jogador pegou em sequência.

combo_value = 0

#Variável contendo o valor de pontos.

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)

#Localização, em pixels, das variáveis score, vida, e combo, respectivamente.

scoreX = 10 
scoreY = 50

vidaX = 10
vidaY = 10

comboX = 10
comboY = 100


#Nome do aplicativo.

pygame.display.set_caption("Survive Covid")

#Ícone do aplicativo.

icon = pygame.image.load('survive-covid 1.0.5/Imagens/icon.png')
pygame.display.set_icon(icon)

#Variáveis do jogador, que incluem sua imagem, localização e velocidade.

playerImg = pygame.image.load('survive-covid 1.0.5/Imagens/carrinho.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 400
playerY = 480
playerX_change = 0

#Variáveis do item Covid, que incluem sua imagem, localização e velocidade.

covidImg = pygame.image.load('survive-covid 1.0.5/Imagens/covid.png')
covidImg = pygame.transform.scale(covidImg, (50, 50))
covidX = random.randint(0, 700)
covidY = -15000
covidY_change = 2.5

#Variáveis do item Feijão, que incluem sua imagem, localização e velocidade.

feijaoImg = pygame.image.load('survive-covid 1.0.5/Imagens/feijao.png')
feijaoImg = pygame.transform.scale(feijaoImg, (50, 50))
feijaoX = random.randint(0, 700)
feijaoY = -60
feijaoY_change = 1.5

#Variáveis do item Arroz, que incluem sua imagem, localização e velocidade.

arrozImg = pygame.image.load('survive-covid 1.0.5/Imagens/arroz.png')
arrozImg = pygame.transform.scale(arrozImg, (50, 50))
arrozX = random.randint(0, 700)
arrozY = -3000
arrozY_change = 2

#Variáveis do item Gel, que incluem sua imagem, localização e velocidade.

gelImg = pygame.image.load('survive-covid 1.0.5/Imagens/gel.png')
gelImg = pygame.transform.scale(gelImg, (50, 50))
gelX = random.randint(0, 700)
gelY = -8000
gelY_change = 2.5

#Função que adiciona a pontução no aplicativo.

def show_score(x, y):
    score = font.render("Pontos: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

#Função que adiciona a vida no aplicativo.

def show_vida(x, y):
    vida = font.render("Vida: " + str(vida_value), True, (255, 255, 255))
    screen.blit(vida, (x, y))

#Função que adiciona o combo no aplicativo.

def show_combo(x, y):
    combo = font.render("Combo: x" + str(multiplicador), True, (255, 255, 255))
    screen.blit(combo, (x, y))

#Função que adiciona o player no aplicativo.

def player(x, y):
    screen.blit(playerImg, (x, y))

#Função que adiciona o item covid no aplicativo.
    
def covid(x, y):
    screen.blit(covidImg, (x, y))

#Função que adiciona o item feijão no aplicativo.

def feijao(x, y):
    screen.blit(feijaoImg, (x, y))

#Função que adiciona a pontução no aplicativo.

def arroz(x, y):
    screen.blit(arrozImg, (x, y))

#Função que adiciona o gel no aplicativo.

def gel(x, y):
    screen.blit(gelImg, (x, y))

#Função que adiciona a colisão do item covid com o player no aplicativo.

def isCollisionCovid(playerX, playerY, covidX, covidY):
    distance = math.sqrt((math.pow(playerX-covidX,2)) + (math.pow(playerY-covidY,2)))
    if distance < 65:
        return True
    else:
        return False

#Função que adiciona a colisão do item feijão com o player no aplicativo.

def isCollisionFeijao(playerX, playerY, feijaoX, feijaoY):
    distance = math.sqrt((math.pow(playerX-feijaoX,2)) + (math.pow(playerY-feijaoY,2)))
    if distance < 65:
        return True
    else:
        return False

#Função que adiciona a colisão do item arroz com o player no aplicativo.

def isCollisionArroz(playerX, playerY, arrozX, arrozY):
    distance = math.sqrt((math.pow(playerX-arrozX,2)) + (math.pow(playerY-arrozY,2)))
    if distance < 65:
        return True
    else:
        return False

#Função que adiciona a colisão do item gel com o player no aplicativo.

def isCollisionGel(playerX, playerY, gelX, gelY):
    distance = math.sqrt((math.pow(playerX-gelX,2)) + (math.pow(playerY-gelY,2)))
    if distance < 65:
        return True
    else:
        return False


#Loop para iniciar o aplicativo.
while True:

    #Define a cor do fundo.

    screen.fill((0, 0, 0))

    #Define o background como fundo.

    screen.blit(background, (0, 0))

    #Loop que espera um evento acontecer para realizar uma determinada ação

    for event in pygame.event.get():

        #Espera o evento quit, e então fecha o jogo

        if event.type == pygame.QUIT:
            pygame.quit()

        #Espera o evento keydown, que é quando um tecla é pressionada.

        if event.type == pygame.KEYDOWN:

            #Move o player em 5 pontos de velocidade para a esquerda, caso a seta esquerda seja pressionada.

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            #Move o player em 5 pontos de velocidade para a direita, caso a seta direita seja pressionada.

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        #Retira a velocidade do player, deixando-o parado, caso pare de pressionar a tecla esquerda ou tecla direita.

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    #Recebe o tempo que se passou durante o loop.
    current_time = pygame.time.get_ticks()

    #Adicionam valores na localização vertical e horizontal de cada item, fazendo-os irem para esquerda, direita, ou para baixo.
    covidY += covidY_change
    feijaoY += feijaoY_change
    arrozY += arrozY_change
    gelY += gelY_change
    playerX += playerX_change

    #Trava a localização do player em 0 pixels na horizontal, para que o jogador não saia da tela.

    if playerX <= 0:
        playerX = 0
    
    #Trava a localização do player em 730 pixels na horizontal, para que o jogador não saia da tela.

    elif playerX >= 730:
        playerX = 730

    #Define que, caso o valor da sequência de itens seja 5, o multiplicador de pontos será de 2x.

    if combo_value >= 5:
        multiplicador = 2

    #Define que, caso o valor da sequência de itens seja 10, o multiplicador de pontos será de 4x.

    if combo_value >= 10:
        multiplicador = 4

    #Define que, caso o valor da sequência de itens seja 15, o multiplicador de pontos será de 6x.

    if combo_value >= 15:
        multiplicador = 6

    #Efetua uma série de ações caso ocorra a colisão entre o covid e o player, como o multiplicador, retirar vida, etc.
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

    #Efetua uma série de ações caso ocorra a colisão entre o feijão e o player, como o aumentar os pontos em 5, adicionar vida, etc.

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

    #Efetua uma série de ações caso ocorra a colisão entre o arroz e o player, como o aumentar os pontos em 10, adicionar vida, etc.

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

    #Efetua uma série de ações caso ocorra a colisão entre o gel e o player, como o aumentar os pontos em 20, adicionar vida, etc.
    
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

    #Efetua uma série de ações caso o item passe do jogador.

    if covidY >= 600:
        covidX = random.randint(0, 700)
        covidY = -60
        covidY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        vida_value -=0
    
    #Efetua uma série de ações caso o item passe do jogador, como resetar o multiplicador, diminuir a vida, etc

    if feijaoY >= 600:
        feijaoX = random.randint(0, 700)
        feijaoY = -60
        feijaoY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=1

    #Efetua uma série de ações caso o item passe do jogador, como resetar o multiplicador, diminuir a vida, etc

    if arrozY >= 600:
        arrozX = random.randint(0, 770)
        arrozY = -60
        arrozY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=2
    
    #Efetua uma série de ações caso o item passe do jogador, como resetar o multiplicador, diminuir a vida, etc

    if gelY >= 600:
        gelX = random.randint(0, 770)
        gelY = -60
        gelY_change += 0.02
        playerX_change += 0.02
        combo_value = 0
        multiplicador = 1
        vida_value -=3
    
    #Libera o arroz para cair quando o tempo chegar em 10 segundos. (Medido em milisegundos)

    if current_time >= 10000:
        arroz(arrozX, arrozY)
    
    #Libera o gel para cair quando o tempo chegar em 25 segundos. (Medido em milisegundos)

    if current_time >= 25000:
        gel(gelX, gelY)
    
    #Libera o covid para cair quando o tempo chegar em 35 segundos. (Medido em milisegundos)
    
    if current_time >= 35000:
        covid(covidX, covidY)
    
    #Define o máximo de vida igual a 10.

    if vida_value >= 10:
        vida_value = 10
    
    #Define o mínimo de vida igual a 0.

    if vida_value <= 0:
        vida_value = 0

    #Funções a serem chamadas para adicionar a imagem de cada item.
    covid(covidX, covidY)
    player(playerX, playerY)
    feijao(feijaoX, feijaoY)
    show_score(scoreX, scoreY)
    show_combo(comboX, comboY)
    show_vida(vidaX, vidaY)
    #Função para manter a tela atualizada a cada a ação.
    pygame.display.update()

    