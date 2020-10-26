import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, playerX, playerY):
        super(Player, self).__init__()
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
        self.rect.topleft = [playerX, playerY]
    
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
pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

moving_spritesRight = pygame.sprite.Group()
moving_spritesLeft = pygame.sprite.Group()
player = Player(10, 10)
moving_spritesRight.add(player)
moving_spritesLeft.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.animateRight()
            if event.key == pygame.K_LEFT:
                player.animateLeft()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.not_animateRight()
            if event.key == pygame.K_LEFT:
                player.not_animateLeft()

    screen.fill((0, 0, 0))
    moving_spritesRight.draw(screen)
    moving_spritesRight.update()
    moving_spritesLeft.draw(screen)
    moving_spritesLeft.update()
    pygame.display.flip()
    clock.tick(60)