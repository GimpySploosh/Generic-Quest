import pygame

playerImage = pygame.image.load("player.png")

# Resize the image to a smaller size
newWidth = 25
newHeight = 25
playerImage = pygame.transform.scale(playerImage, (newWidth, newHeight))

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player = MySprite(playerImage, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    player.rect.centerx = player_pos.x
    player.rect.centery = player_pos.y

    screen.blit(player.image, player.rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
