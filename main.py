# to people editing this code - PLEASE USE CAMELCASE
# I know most people in Python use snake_case, but deal with it

import pygame

SCALE = .7

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280 * SCALE, 720 * SCALE)) # aspect ratio: 16:9.
# when working in Piskel, you can do 640x360
clock = pygame.time.Clock()
running = True
dt = 0
item = "none"
locked = True

roomNum = 0 # lowest room number is 0

playerImage = pygame.image.load("genEric.png")
wizardImage = pygame.image.load("wizard.png")
book = pygame.image.load("book.png")
grass = pygame.image.load("grass.png")
knot = pygame.image.load("knot.png")
socks = pygame.image.load("socks.png")
titleScreen = pygame.image.load("titleScreen.png")
background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.gif")
background4 = pygame.image.load("background4.png")
portal = pygame.image.load("portal.gif")
monster1 = pygame.image.load("monster1.png")
monster2 = pygame.image.load("monster2.gif")
lockedPortal = pygame.image.load("lockedPortal.gif")

# sprite class. Set the image for it, xy position, and sprite scale
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, spriteScale):
        super().__init__()
        scaledWidth = image.get_width() * spriteScale * SCALE
        scaledHeight = image.get_height() * spriteScale * SCALE
        self.image = pygame.transform.scale(image, (scaledWidth, scaledHeight))
        self.rect = self.image.get_rect(center=(x, y))
        
background1 = MySprite(background1, 0, 0, 1)
background2 = MySprite(background2, 0, 0, 1)
background3 = MySprite(background3, 0, 0, 6.5)

# set/change rooms. All excusive sprites and backgrounds for that level will be generated here
def roomSet(): 
    # ROOMS = ["start; 0", "roomName; roomNum"]
    # don't use the list above, just look at it for reference to figure out the genral room names4
    global roomNum
    global lockedPortal
    if roomNum == 0:
        door = MySprite(portal, 250, 240, 2.5)
        door1 = MySprite(portal, 620, 10, 2.5)
        door2 = MySprite(lockedPortal, screen.get_width() // 1.1,  screen.get_height() // 1.1, 2.5)
        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 2
            player.rect.x = screen.get_width() // 2
            roomNum = 1
        if pygame.sprite.collide_rect(door1,  player):
            player.rect.y = screen.get_height() // 2 + 50
            player.rect.x = screen.get_width() // 2 - 100
            roomNum = 2
        if locked == False:
            lockedPortal = pygame.image.load("portal.gif")
            if pygame.sprite.collide_rect(lockedPortal, player):
                player.rect.y = screen.get_height() // 2
                player.rect.x = screen.get_width() // 2
                roomNum = 4
        screen.blit(background1.image, (0, 0))
        screen.blit(door.image, door.rect)
        screen.blit(door1.image, door1.rect)
        screen.blit(door2.image, door2.rect)
    if roomNum == 1:
        screen.blit(background2.image, (0, 0))
        door = MySprite(portal, 140, screen.get_height() - portal.get_height(), 2.5)
        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 2
            player.rect.x = screen.get_width() // 2
            roomNum = 0
        screen.blit(door.image, door.rect)
    if roomNum == 2:
        screen.blit(background3.image, (0, 0))
        door = MySprite(portal, 140, screen.get_height() - portal.get_height(), 2.5)
        monster = MySprite(monster2, screen.get_width() // 1.3, screen.get_height() // 2, 2.5)
        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 2
            player.rect.x = screen.get_width() // 2
            roomNum = 0
        screen.blit(door.image, door.rect)
        screen.blit(monster.image, monster.rect)
    if roomNum == 3:
        pass
    if roomNum == 4:
        screen.blit(background4.image(0, 0))
    screen.blit(text, (screen.get_width() / 2, 20))

player = MySprite(playerImage, screen.get_width() / 2, screen.get_height() / 2, 0.2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    font = pygame.font.SysFont("Arial", 20)
    #font.set_bold(True)
    text = font.render(item, True, (255, 255, 255))


    roomSet()

    # movements
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.rect.y -= 300 * dt * SCALE
    if keys[pygame.K_s]:
        player.rect.y += 300 * dt * SCALE
    if keys[pygame.K_a]:
        player.rect.x -= 300 * dt * SCALE
    if keys[pygame.K_d]:
        player.rect.x += 300 * dt * SCALE

    # idk what this does. Just don't touch it
    if any(keys):
        player.rect.centerx = player.rect.x + player.rect.width / 2
        player.rect.centery = player.rect.y + player.rect.height / 2

    screen.blit(player.image, player.rect)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    if keys[pygame.K_MINUS]:
        running = False

pygame.quit()
