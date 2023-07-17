import pygame

SCALE = 1
playerImage = pygame.image.load("player.png")

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

playerPos = pygame.Vector2(screen.get_width()/ 2, screen.get_height()/ 2)
player = MySprite(playerImage, playerPos.x, playerPos.y, 25, 25)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPos.y -= 300 * dt * SCALE
    if keys[pygame.K_s]:
        playerPos.y += 300 * dt * SCALE
    if keys[pygame.K_a]:
        playerPos.x -= 300 * dt * SCALE
    if keys[pygame.K_d]:
        playerPos.x += 300 * dt * SCALE

    player.rect.centerx = playerPos.x
    player.rect.centery = playerPos.y

    screen.blit(player.image, player.rect)

    pygame.display.flip()

    dt = clock.tick(30) / 1000

    """
    pygame.display.set_caption(str(playerPos.y))
    pygame.display.flip()
    """

pygame.quit()
