import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
frameclock = pygame.time.Clock()
jynx = pygame.image.load('Jynx.png')
done = False
is_blue = False
x = 150
y = 100

 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_UP]: y -= 3
                if pressed[pygame.K_DOWN]: y += 3
                if pressed[pygame.K_LEFT]: x -= 3
                if pressed[pygame.K_RIGHT]: x += 3
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                else:
                        if is_blue:
                                color = (0, 128, 255)
                        else:
                                color = (255, 100, 0)
                        screen.fill((0, 0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        frameclock.tick(60)
        pygame.display.flip()