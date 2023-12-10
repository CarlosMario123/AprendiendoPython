import pygame
import sys
import math

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Simulador de Disparo de Cañón")
font = pygame.font.Font(None, 36)

def calcular_trayectoria(angulo, velocidad_inicial):
    angulo_rad = math.radians(angulo)
    velocidad_x = velocidad_inicial * math.cos(angulo_rad)
    velocidad_y = velocidad_inicial * math.sin(angulo_rad)
    gravity = 9.81
    time_of_flight = (2 * velocidad_y) / gravity
    
    time = 0
    points = []
    
    while time <= time_of_flight:
        x = velocidad_x * time
        y = (velocidad_y * time) - (0.5 * gravity * time ** 2)
        points.append((x, y))
        time += 0.1
    
    max_x = max(points, key=lambda item: item[0])[0]
    max_y = max(points, key=lambda item: item[1])[1]
    scaling_factor = min(WIDTH / max_x, HEIGHT / max_y)
    scaled_points = [(point[0] * scaling_factor, HEIGHT - point[1] * scaling_factor) for point in points]
    
    return scaled_points

def get_angle():
    angle = 0
    selecting = True

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                angle = math.degrees(math.atan2(HEIGHT - event.pos[1], event.pos[0]))
                selecting = False

        screen.fill(WHITE)
        text_surface = font.render("Haga clic y arrastre para seleccionar el ángulo:", True, BLACK)
        screen.blit(text_surface, (50, HEIGHT // 2 - 50))

        pygame.display.flip()
        clock.tick(FPS)

    return angle

def main():
    angulo = 45
    velocidad_inicial = 20
    
    trayectoria = calcular_trayectoria(angulo, velocidad_inicial)
    
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for point in trayectoria:
            pygame.draw.circle(screen, BLACK, (int(point[0]), int(point[1])), 2)
        
        pygame.draw.line(screen, RED, (0, HEIGHT), (WIDTH, HEIGHT), 2)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
