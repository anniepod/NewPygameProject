import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PIZZA GAME')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
qt = False
pizzImg = pygame.image.load('CheesePizza.jpg')


def pizzaa(x, y):
    gameDisplay.blit(pizzImg, (x, y))


x = (display_width * 0.25)
y = (display_height * 0.3)

while not qt:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           qt = True

    gameDisplay.fill(white)
    pizzaa(x, y)

    pygame.display.update()
    clock.tick(60)

pizzImg = pygame.image.load('CheesePizza.jpg')


def mushroom(x, y):
    gameDisplay.blit(pizzImg, (x, y))



pygame.quit()
quit()