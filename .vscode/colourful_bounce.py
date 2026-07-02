import pygame
import random 

pygame.init()

Sprite_color_change_event = pygame.USEREVENT + 1
Background_color_change_event = pygame.USEREVENT + 2

BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("Orange")
WHITE = pygame.Color("white")

class Sprite(pygame.sprite.Sprite):

    def __init__ (self, color, height, width):
        super.__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    
    def update(self):
        self.rect.move_ip(self.velocity)
        
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0], -self.velocity[0]
        
        boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1], -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event (Sprite_color_change_event))
            pygame.event.post(pygame.event.Event (Background_color_change_event))

    def change_color(self):
        self.image.fill(random.choice([MAGENTA, YELLOW, ORANGE, WHITE]))

def change_background_color():
    global bg_color 
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])