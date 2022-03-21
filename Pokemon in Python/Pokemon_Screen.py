import pygame

pygame.init()

def scale_coords(coords, factor):
    scaled_coords = []
    for num in coords:
        scaled_coords.append(num * factor)
    return scaled_coords

def get_scale_factor(window_res, base_res):
    x_scl = window_res[0] / base_res[0]
    y_scl = window_res[1] / base_res[1]
    return min(x_scl, y_scl)

def to_aspect(coords, aspect):
    return (coords[1] * (aspect[0]/aspect[1]), coords[1])

base_res_x = 1152
base_res_y = 648
base_res = (base_res_x, base_res_y)
scale_factor = 1
window_res = scale_coords(base_res, scale_factor)
window = pygame.display.set_mode(base_res, pygame.RESIZABLE)


white = (255, 255, 255)
black = (0, 0, 0)

frameclock = pygame.time.Clock()
gameloop = True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        window = pygame.display.set_mode(to_aspect(window_res, (16, 9)), pygame.RESIZABLE)
        window.fill(white)
        scale_factor = get_scale_factor(window.get_size(), base_res)
        window_res = scale_coords(base_res, scale_factor)

        pygame.draw.rect(window, black, pygame.Rect(scale_coords(window_res, 0.5), (50, 50)))
    pygame.display.flip()
    frameclock.tick(60)