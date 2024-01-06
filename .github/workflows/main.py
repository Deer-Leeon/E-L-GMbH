import pygame

pygame.init()

Bar_Breite = 442
Bar_Höhe = 50
SpielerX = 40
SpielerY = 75
screen = pygame.display.set_mode((1920, 1080))
Speed = 5
positionx = 920
positiony = 629

hintergrund_bild1 = pygame.image.load('Hintergrund.gif')
hintergrund_bild3 = pygame.image.load('Tab.png')
hintergrund_bild2 = pygame.image.load('Boden.png')

running = True
while running:
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    laufen = pygame.key.get_pressed()
    if laufen[pygame.K_LEFT]:
        positionx = positionx - Speed
    if laufen[pygame.K_RIGHT]:
        positionx = positionx + Speed

    
    screen.blit(hintergrund_bild1, (0, 0))
    screen.blit(hintergrund_bild2, (0, 0))
    screen.blit(hintergrund_bild3, (737, 1000))
    pygame.draw.rect(screen,(255,0,0), (positionx,positiony,SpielerX,SpielerY))

    pygame.display.update()

pygame.quit()
