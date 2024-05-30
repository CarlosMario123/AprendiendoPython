import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((820, 620))

logotipo = pygame.image.load('p.jpg')
fondo = pygame.image.load('fondo.png')
banana = pygame.image.load('pene.png')

logo_x = 70
logo_y = 70

banana_x = 383
banana_y = 290

velocidad = 0.2

bananas_comidas = 0
vidas_restantes = 5

niveles = 1  
ultima_cantidad_bananas = 0



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        logo_y -= velocidad
    if keys[pygame.K_DOWN]:
        logo_y += velocidad
    if keys[pygame.K_LEFT]:
        logo_x -= velocidad
    if keys[pygame.K_RIGHT]:
        logo_x += velocidad

    logo_x = max(0, min(750, logo_x))
    logo_y = max(0, min(550, logo_y))

    if logo_x + logotipo.get_width() > banana_x and logo_x < banana_x + banana.get_width():
        if logo_y + logotipo.get_height() > banana_y and logo_y < banana_y + banana.get_height():
            bananas_comidas += 1
            banana_x = 100 + (pygame.time.get_ticks() % 620)
            banana_y = 100 + (pygame.time.get_ticks() % 420)
            if bananas_comidas % 5 == 0:
                velocidad += .2
                
    if bananas_comidas != ultima_cantidad_bananas and bananas_comidas % 10 == 0:
        niveles += 1  
        ultima_cantidad_bananas = bananas_comidas
    


    screen.blit(fondo, (0, 0))
    screen.blit(banana, (banana_x, banana_y))
    screen.blit(logotipo, (logo_x, logo_y))



    pygame.display.set_caption(f"Fierros  comidos: {bananas_comidas}        Vidas Restantes: {vidas_restantes}   Nivel: {niveles}")

    pygame.display.flip()

pygame.quit()
sys.exit()