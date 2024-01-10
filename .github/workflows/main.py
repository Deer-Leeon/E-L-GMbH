import pygame

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))

Bar_Breite = 442
Bar_Höhe = 50
SpielerX = 40
SpielerY = 75
Speed = 5
positionx = 0.48*screen_width
positiony = 0.58*screen_height

isJumping = False
jumpHeight = 5

hintergrund_bild1 = pygame.image.load('Hintergrund.gif')
hintergrund_bild2 = pygame.image.load('Boden.png')
hintergrund_bild3 = pygame.image.load('Tab.png')

hintergrund_bild1 = pygame.transform.scale(hintergrund_bild1, (screen_width, screen_height))
hintergrund_bild2 = pygame.transform.scale(hintergrund_bild2, (screen_width, screen_height))
hintergrund_bild3 = pygame.transform.scale(hintergrund_bild3, (screen_width, screen_height))


running = True
while running:
    pygame.time.delay(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #laufen
    Eingabe = pygame.key.get_pressed()
    if Eingabe[pygame.K_LEFT]:
        positionx = positionx - Speed
    if Eingabe[pygame.K_RIGHT]:
        positionx = positionx + Speed

    #springen
    if not isJumping:
        if Eingabe[pygame.K_SPACE]:
            isJumping = True
    else:
        if jumpHeight >= -5:
            neg = 1.5
            if jumpHeight < 0:
                neg = -1.5
            positiony -= (jumpHeight ** 4) * 0.5 * neg
            jumpHeight -= 1
        else:
            isJumping = False
            jumpHeight = 5


    
    screen.blit(hintergrund_bild1, (0, 0))
    screen.blit(hintergrund_bild2, (0, 0))
    screen.blit(hintergrund_bild3, (737, 1000))
    pygame.draw.rect(screen,(255,0,0), (positionx,positiony,SpielerX,SpielerY))

    pygame.display.update()

pygame.quit()
