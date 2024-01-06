import pygame

pygame.init()


Breite = 442
Höhe = 50

screen = pygame.display.set_mode((1920, 1080))


# Bild laden und auf Fenstergröße skalieren
hintergrund_bild2 = pygame.image.load('Hintergrund.gif')
hintergrund_bild = pygame.image.load('Tab.png')  # Passe 'hintergrundbild.jpg' mit dem Namen deines Bildes an
hintergrund_bild = pygame.transform.scale(hintergrund_bild, (Breite, Höhe))
hintergrund_bild3 = pygame.image.load('Boden.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hintergrundbild zeichnen
    screen.blit(hintergrund_bild2, (0, 0))
    screen.blit(hintergrund_bild3, (0, 0))
    screen.blit(hintergrund_bild, (737, 1000))

    pygame.display.update()

pygame.quit()
