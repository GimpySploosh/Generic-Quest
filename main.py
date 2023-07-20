# to people editing this code - PLEASE USE CAMELCASE
# I know most people in Python use snake_case, but deal with it

import pygame
import random
import time
import sys

SCALE = .7

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280 * SCALE, 720 * SCALE)) # aspect ratio: 16:9.
# when working in Piskel, you can do 640x360
clock = pygame.time.Clock()
running = True
dt = 0
item = "None"
wpm = "N/A"
winLocked = True
locked1 = True
win = False
whoBattle = ""
typeList = ["old ", "be ", "help ", "think ", "form ", "plan ", "general ", "off ", "could ", "still ", "fact ", "keep ", "each ", "turn"]
game = False
type1 = "".join(typeList)
text_color = pygame.Color('white')
cursor_color = pygame.Color('white')
monster1Killed = False
monster2Killed = False
monster3Killed = False
spawnKey = False
spawnFinalKey = False

roomNum = 0 # lowest room number is 0

playerImage = pygame.image.load("genEric.png")
wizardImage = pygame.image.load("wizard.png")
book = pygame.image.load("book.png")
finalKey = pygame.image.load("finalKey.png")
grass = pygame.image.load("grass.png")
knot = pygame.image.load("knot.png")
socks = pygame.image.load("socks.png")
titleScreen = pygame.image.load("titleScreen.png")
background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.gif")
background4 = pygame.image.load("background4.png")
background5 = pygame.image.load("background5.png")
background6 = pygame.image.load("background6.png")
portal = pygame.image.load("portal.gif")
lockedPortal = pygame.image.load("lockedPortal.gif")
lockedPortal1 = pygame.image.load("lockedPortal.gif")
winPortal = pygame.image.load("winPortal.gif")
monster1 = pygame.image.load("monster1.png")
monster2 = pygame.image.load("monster2.png")
monster3 = pygame.image.load("monster3.gif")

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
background4 = MySprite(background4, 0, 0, 2)
background5 = MySprite(background5, 0, 0, .1)
background6 = MySprite(background6, 0, 0, .18)

spawnSocks = False

class TextInputField:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is inside the input field
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN: 
                time_elapsed = time.time() - start_time
                if type1 == self.text:
                    global roomNum
                    global game
                    global monster1Killed
                    global monster2Killed
                    global monster3Killed
                    global wpm
                    
                    global spawnSocks
                    global spawnKey
                    global spawnFinalKey

                    print("yep")
                    wpm = int(14/float(time_elapsed / 100))
                    print(str(wpm))
                    if whoBattle == "monster1":
                        if wpm >= 45:
                            monster1Killed = True
                            spawnSocks = True
                            game = False
                            roomNum = 0
                            roomSet()
                        else:
                            monster1Killed = False
                            game = False
                            roomNum = 0
                            roomSet()
                    elif whoBattle == "monster2":
                        if wpm >= 55:
                            monster2Killed = True
                            spawnKey = True
                            game = False
                            roomNum = 0
                            roomSet()
                        else:
                            monster2Killed = False
                            game = False
                            roomNum = 0
                            roomSet()
                    elif whoBattle == "monster3":
                        if wpm >= 75:
                            monster3Killed = True
                            spawnFinalKey = True
                            game = False
                            roomNum = 0
                            roomSet()
                        else:
                            monster3Killed = False
                            game = False
                            roomNum = 0
                            roomSet()
                else:
                    print("nope")
                    print(type1)
                    print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x + 5, self.rect.y + 5, screen.get_width(), 20))
        surface.blit(font.render(self.text, True, text_color), (self.rect.x + 5, self.rect.y + 5))
        if self.active:
            pygame.draw.rect(surface, cursor_color, (self.rect.x + 5 + font.size(self.text)[0], self.rect.y + 5, 2, font.size(self.text)[1]))

text_input = TextInputField(100, 100, 300, 40)  # Adjust the position and size as needed

# set/change rooms. All excusive sprites and backgrounds for that level will be generated here
def roomSet(): 
    # ROOMS = ["start; 0", "roomName; roomNum"]
    # don't use the list above, just look at it for reference to figure out the genral room names4
    global roomNum
    global lockedPortal
    global lockedPortal1
    global whoBattle
    global typeList
    global game
    global start_time
    global wpm
    global win
    global item
    global locked1
    global winLocked
    global spawnKey
    global spawnFinalKey
    if roomNum == 0:
        screen.blit(background1.image, (0, 0))
        if win == False:
            door = MySprite(portal, 250, 240, 2.5)
            door1 = MySprite(lockedPortal1, 620, 10, 2.5)
            door2 = MySprite(lockedPortal, screen.get_width() // 1.1,  screen.get_height() // 1.1, 2.5)
            if pygame.sprite.collide_rect(door,  player):
                player.rect.y = screen.get_height() // 2
                player.rect.x = screen.get_width() // 3
                roomNum = 1
            if winLocked == False:
                lockedPortal = pygame.image.load("portal.gif")
                if pygame.sprite.collide_rect(door2, player):
                    player.rect.y = screen.get_height() // 2
                    player.rect.x = screen.get_width() // 2
                    roomNum = 4
            if locked1 == False:
                lockedPortal1 = pygame.image.load("portal.gif")
                if pygame.sprite.collide_rect(door1, player):
                    player.rect.y = screen.get_height() // 2 + 50
                    player.rect.x = screen.get_width() // 2 - 100
                    roomNum = 2
            screen.blit(door.image, door.rect)
            screen.blit(door1.image, door1.rect)
            screen.blit(door2.image, door2.rect)
        elif win == True:
            roomNum = 0
            door = MySprite(winPortal, 250, 240, 2.5)
            if pygame.sprite.collide_rect(door,  player):
                player.rect.y = screen.get_height() // 2
                player.rect.x = screen.get_width() // 2
                roomNum = 6
            screen.blit(door.image, door.rect)
    if roomNum == 1:
        if monster1Killed == False:
            monster = MySprite(monster1, screen.get_width() // 1.7, screen.get_height() // 2.5, 1.3)
        else:
            monster = MySprite(monster1, screen.get_width() * 2, screen.get_height() * 2, 0.3)
        screen.blit(background2.image, (0, 0))
        door = MySprite(portal, 200, screen.get_height() // 1.02, 2.5)

        if spawnSocks == True:
            visibleItem = MySprite(socks, screen.get_width() // 2, 300, 0.3)
            if pygame.sprite.collide_rect(visibleItem, player):
                item = "Socks"
                locked1 = False
            elif item != "Socks":
                screen.blit(visibleItem.image, visibleItem.rect)
        
        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 1.3
            player.rect.x = screen.get_width() // 2
            roomNum = 0
        if pygame.sprite.collide_rect(monster, player):
            whoBattle = "monster1"
            roomNum = 3
        screen.blit(door.image, door.rect)
        screen.blit(monster.image, monster.rect)
    if roomNum == 2:
        screen.blit(background3.image, (0, 0))
        if monster2Killed == False:
            monster = MySprite(monster2, screen.get_width() // 1.3, screen.get_height() // 2, .7)
        else:
            monster = MySprite(book, screen.get_width() * 1.3, screen.get_height() * 2, .01)
        door = MySprite(portal, 140, screen.get_height() - portal.get_height(), 2.5)

        if spawnKey == True:
            boook = MySprite(book, screen.get_width() // 1.3, screen.get_height() // 2, .06)
            if pygame.sprite.collide_rect(boook, player):
                item = "book"
                winLocked = False
                boook = MySprite(portal, 10000, 10000, 0.0003)
                spawnKey = False
            screen.blit(boook.image, boook.rect)
            
        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 1.3
            player.rect.x = screen.get_width() // 2
            roomNum = 0
        if pygame.sprite.collide_rect(monster, player):
            whoBattle = "monster2"
            roomNum = 3
        screen.blit(door.image, door.rect)
        screen.blit(monster.image, monster.rect)
    if roomNum == 3:
        start_time = time.time()
        game = True
        
    if roomNum == 4:
        screen.blit(background4.image, (0, 0))
        if monster3Killed == False:
            monster = MySprite(monster3, screen.get_width() // 1.3, screen.get_height() // 2, 1.5)
        else:
            monster = MySprite(book, screen.get_width() * 1.3, screen.get_height() * 2, .01)
            roomNum = 4
        door = MySprite(portal, 140, screen.get_height() - portal.get_height(), 2.5)

        if spawnFinalKey == True:
            finalKeyy = MySprite(finalKey, screen.get_width() // 1.2, screen.get_height() // 2, .04)
            if pygame.sprite.collide_rect(finalKeyy, player):
                item = "Final Key"
                finalKeyy = MySprite(portal, 10000, 10000, 0.0003)
                spawnFinalKey = False
                win = True
            screen.blit(finalKeyy.image, finalKeyy.rect)

        if pygame.sprite.collide_rect(door,  player):
            player.rect.y = screen.get_height() // 1.3
            player.rect.x = screen.get_width() // 2
            roomNum = 0
        if pygame.sprite.collide_rect(monster, player):
            whoBattle = "monster3"
            roomNum = 3
        screen.blit(door.image, door.rect)
        screen.blit(monster.image, monster.rect)
    if roomNum == 6:
        screen.blit(background6.image, (0, 0))
    screen.blit(text, (screen.get_width() / 2, 20))
    screen.blit(wpmDisp, (screen.get_width() / 2, 40))

player = MySprite(playerImage, screen.get_width() / 2, screen.get_height() / 2, 0.2)

while running:
    if game == True:
        screen.blit(background5.image, (0, 0))
        if whoBattle == "monster1":
            monster = MySprite(monster1, screen.get_width() // 2, 300, 1.3)
        elif whoBattle == "monster2":
            monster = MySprite(monster2, screen.get_width() // 2, screen.get_height() // 2, .7)
        elif whoBattle == "monster3":
            monster = MySprite(monster3, screen.get_width() // 2, screen.get_height() // 2, 1.5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Pass events to the text input field
            text_input.handle_event(event)
        text_input.draw(screen)  # Draw the text input field on the screen

        screen.blit(monster.image, monster.rect)

        pygame.draw.rect(screen, (255, 0, 0), (0, screen.get_height() // 2, screen.get_width(), 20))
        screen.blit(thingy, (0, screen.get_height() // 2))

        pygame.display.flip()
        clock.tick(30)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        font = pygame.font.SysFont("Arial", 20)
        text = font.render(item, True, (255, 255, 255))
        wpmDisp = font.render("Last WPM: " + str(wpm), True, (255, 255, 255))
        thingy = font.render(type1, True, (255, 255, 255))

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
