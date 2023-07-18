# to people editing this code - PLEASE USE CAMELCASE
# I know most people in Python use snake_case, but deal with it

import pygame

SCALE = 0.7
playerImage = pygame.image.load("placeholder.png")
wizardImage = pygame.image.load("wizard.png")
book = pygame.image.load("book.png")
grass = pygame.image.load("grass.png")
knot = pygame.image.load("knot.png")
socks = pygame.image.load("socks.png")
titleScreen = pygame.image.load("titleScreen.png")


class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(image, (width * SCALE, height * SCALE))
        self.rect = self.image.get_rect(center=(x, y))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280 * SCALE, 720 * SCALE))
clock = pygame.time.Clock()
running = True
dt = 0

player = MySprite(playerImage, screen.get_width() / 2, screen.get_height() / 2, 100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.rect.y -= 300 * dt * SCALE
    if keys[pygame.K_s]:
        player.rect.y += 300 * dt * SCALE
    if keys[pygame.K_a]:
        player.rect.x -= 300 * dt * SCALE
    if keys[pygame.K_d]:
        player.rect.x += 300 * dt * SCALE

    player.rect.centerx = player.rect.x + player.rect.width / 2
    player.rect.centery = player.rect.y + player.rect.height / 2

    screen.blit(player.image, player.rect)

    pygame.display.flip()

    dt = clock.tick(30) / 1000

pygame.quit()
