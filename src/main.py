import pygame
from render.render import render


def main():
    pygame.init()

    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    BASE_WIDTH = 640
    scale = WIDTH / BASE_WIDTH

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render(screen, scale)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    print(scale)

if __name__ == "__main__":
    main()
    
