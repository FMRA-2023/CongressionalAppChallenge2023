from networking.VolunteerEvent import VolunteerEvent
import pygame


events = [
    VolunteerEvent("Beach Cleanup", "Save the Oceans Org",
                   "Help pick up trash on the beach",
                   "123 Ocean Ave, Beach City, CA", "e", 12, 18, "beach.jpg"),
    VolunteerEvent("Dog Shelter", "Animal Rescue Org",
                   "Walk, play with, and care for shelter dogs",
                   "456 Bark Ave, Woofville, NY", "e", 12, 18, "dog.jpg"),
    VolunteerEvent("Event 3", "Company 3", "Description 3", "Address 3", "e",
                   12, 18, "image3.jpg"),
    VolunteerEvent("Event 4", "Company 4", "Description 4", "Address 4", "e",
                   12, 18, "image4.jpg"),
    VolunteerEvent("Event 5", "Company 5", "Description 5", "Address 5", "e",
                   12, 18, "image5.jpg"),
    VolunteerEvent("Event 6", "Company 6", "Description 6", "Address 6", "e",
                   12, 18, "image6.jpg"),
    VolunteerEvent("Event 7", "Company 7", "Description 7", "Address 7", "e",
                   12, 18, "image7.jpg")
]
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.freetype.Font("Arial.ttf", 16)

event_surfaces = []
y_offset = 20
for event in events:
    surface = pygame.Surface((300, 300))
    title_font = pygame.freetype.Font("Arial.ttf", 32)
    title_surf = title_font.render(event.eventName, fgcolor="black")
    title_rect = title_surf.get_rect(midtop=(150, 10))
    surface.blit(title_surf, title_rect)
    font.render_to(surface, (10, 50), event.company, fgcolor="gray")
    font.render_to(surface, (10, 70), event.description, fgcolor="black")
    font.render_to(surface, (10, 90), event.address, fgcolor="gray")
    image = pygame.image.load(event.featuredImage)
    image = pygame.transform.smoothscale(image, (200, 100))
    surface.blit(image, (50, 170))
    event_surfaces.append((surface, y_offset))
    y_offset += 320

scroll = 0
scroll_max = len(event_surfaces) * 320 - 600
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if scroll < scroll_max:
                    scroll += 100
            elif event.key == pygame.K_UP:
                if scroll > 0:
                    scroll -= 100

    screen.fill((255, 255, 255))
    for surface, y in event_surfaces:
        screen.blit(surface, (100, y - scroll))

    pygame.display.flip()

pygame.quit()
