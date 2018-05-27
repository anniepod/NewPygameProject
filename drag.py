
import sys, pygame
from pygame import mouse
import random
from threading import Timer
import time


WHITE = (255, 255, 255)


class Pizza(pygame.sprite.Sprite):
    def __init__(self, image_path="CheesePizza.jpg", scale=(600, 600), position=[350, 200]):

        self.image_path = image_path

        self.position = position

        self.scale = scale

        self.held = False


        self.image = pygame.image.load(self.image_path).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.scale)



class Topping(pygame.sprite.Sprite):

    def __init__(self, image_path="chew.png", scale=(100, 160), position=[100, 200]):

        self.image_path = image_path

        self.position = position

        self.scale = scale

        self.held = False


        self.image = pygame.image.load(self.image_path).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.scale)



class Game(object):
    def __init__(self):

        pygame.init()


        self.main_window = pygame.display.set_mode((1280, 1024))


        pygame.display.set_caption("Drag and Drop")

        self.toppings = []

        self.tops = []


        self.clock = pygame.time.Clock()


    def create_toppings(self):
        self.pizza = Pizza()
        self.toppings.append(Topping("mushroom.png", (100, 100), [100, 200]))
        self.toppings.append(Topping("mushroom.png", (80, 80), [100, 300]))
        self.toppings.append(Topping("mushroom.png", (120, 120), [150, 250]))
        self.toppings.append(Topping("pepperoni.png", (100, 100), [550, 50]))
        self.toppings.append(Topping("pepperoni.png", (80, 80), [490, 70]))
        self.toppings.append(Topping("pepperoni.png", (120, 120), [510, 90]))
        self.toppings.append(Topping("nugget.png", (120, 120), [1110, 90]))
        self.toppings.append(Topping("nugget.png", (80, 80), [1110, 90]))


#create random topping function (one state)
#create/ change position of those toppings (move toppings into line)
#random



    def randtops(self):
        for i in range(3):
            x = random.randint(400,750)
            y = random.randint(250,600)
            self.pizza = Pizza()
            self.tops.append(Topping("mushroom.png", (100, 100), [x, y]))
        for i in range(3):
            x = random.randint(400,750)
            y = random.randint(250,600)
            self.pizza = Pizza()
            self.tops.append(Topping("pepperoni.png", (100, 100), [x, y]))
        for i in range(3):
            x = random.randint(400,750)
            y = random.randint(250,600)
            self.pizza = Pizza()
            self.tops.append(Topping("nugget.png", (100, 100), [x, y]))




    def is_over(self, mouse_pos, topping):

        if mouse_pos[0] > topping.position[0] and mouse_pos[0] < topping.position[0] + topping.scale[0]:

            if mouse_pos[1] > topping.position[1] and mouse_pos[1] < topping.position[1] + topping.scale[1]:
                return True
        return False


    def mouse_button_down(self):

        mouse_pos = mouse.get_pos()

        for i in range(0, len(self.toppings)):

            if self.is_over(mouse_pos, self.toppings[i]):
                self.toppings[i].held = True


    def mouse_button_up(self):

        for i in range(0, len(self.toppings)):
            self.toppings[i].held = False


    def update_position(self):

        mouse_pos = mouse.get_pos()

        for i in range(0, len(self.toppings)):

            if self.toppings[i].held:

                self.toppings[i].position[0] = mouse_pos[0] - self.toppings[i].scale[0] / 2
                self.toppings[i].position[1] = mouse_pos[1] - self.toppings[i].scale[1] / 2

#NEW RUN FCTN
    def run2(self):

        self.randtops()

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_button_down()

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_button_up()

            self.update_position()

            self.main_window.fill(WHITE)
            self.main_window.blit(self.pizza.image, self.pizza.position)

            for i in range(0, len(self.tops)):
                 self.main_window.blit(self.tops[i].image, self.tops[i].position)

            pygame.display.flip()

            self.clock.tick(60)

    def run(self):

        self.create_toppings()
        #self.randtops()

        while True:


            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_button_down()

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_button_up()


            self.update_position()


            self.main_window.fill(WHITE)
            self.main_window.blit(self.pizza.image, self.pizza.position)

            for i in range(0, len(self.toppings)):
                self.main_window.blit(self.toppings[i].image, self.toppings[i].position)

           # for i in range(0, len(self.tops)):
           #     self.main_window.blit(self.tops[i].image, self.tops[i].position)

            pygame.display.flip()


            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()




state_num = 0
def advance_state_machine():
    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        game.run()
        state_num = 1

    else:
        state_num == 1  # Transition from state 1 to state 2
        game.run2()
        state_num = 0

t = Timer(5,advance_state_machine)
t.start()

advance_state_machine()