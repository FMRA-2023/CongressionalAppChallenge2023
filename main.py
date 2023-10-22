import os
import sys

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from consts import SIZE, BEZEL, BORDER_RADIUS

pygame.init()
window = pygame.display.set_mode((SIZE[0]+BEZEL*2, SIZE[1]+BEZEL*2))
screen = pygame.Surface(SIZE, flags=pygame.SRCALPHA)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw actual display screen and put iPhone outline on it
    # fill screens
    window.fill((58, 201, 236))
    screen.fill((60, 60, 60))

    # create basis phone chassis
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, 0, SIZE[0]+2*BEZEL, SIZE[1]+2*BEZEL), border_radius=BORDER_RADIUS)
    # draw true screen
    window.blit(screen, (BEZEL, BEZEL))
    # iPhone notch
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect((SIZE[0]+2*BEZEL)*0.3, 0, (SIZE[0]+2*BEZEL)*0.4, SIZE[1]*0.05), border_radius=BEZEL, border_top_left_radius=0, border_top_right_radius=0)
    # fix the display rect sticking out on corners
    display_rounded = pygame.Surface((BORDER_RADIUS, BORDER_RADIUS), flags=pygame.SRCALPHA)
    pygame.draw.circle(display_rounded, (0, 0, 0), (0, 0), BORDER_RADIUS)
    pygame.draw.circle(display_rounded, (0, 0, 0, 0), (0, 0), BORDER_RADIUS-BEZEL)
    window.blit(display_rounded, (SIZE[0]+2*BEZEL-BORDER_RADIUS, SIZE[1]+2*BEZEL-BORDER_RADIUS))
    window.blit(pygame.transform.rotate(display_rounded, 90), (SIZE[0]+2*BEZEL-BORDER_RADIUS, 0))
    window.blit(pygame.transform.rotate(display_rounded, 180), (0, 0))
    window.blit(pygame.transform.rotate(display_rounded, 270), (0, SIZE[1]+2*BEZEL-BORDER_RADIUS))




    pygame.display.update()

pygame.quit()
sys.exit()
