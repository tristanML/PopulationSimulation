from organism_code import *
import pygame
from pygame.locals import *
import time

lizard_genome = [Genotype("e", name = "eye color"), Genotype("c", name = "claw color"), Genotype("s", name = "spine color")]

lizard1 = Organism(lizard_genome, "lizard")
lizard2 = Organism(lizard_genome, "lizard")

lizard_sprite = pygame.image.load("base_images/StandardSprite.png")

spine_coords_list = [(360, 240), (360, 264), (360, 288), (384, 312), (384, 336), (384, 360),
                    (360, 384), (360, 408), (360, 432), (384, 456), (384, 480), (384, 504),
                    (360, 528), (360, 552), (384, 576), (384, 600), (408, 624), (432, 648), 
                    (456, 672), (480, 696), (504, 672), (528, 648), (504, 624), (480, 600)] 

claw_coords_list = [(192, 216), (216, 192), (264, 192), (480, 192), (528, 192), (552, 216), (192, 384), (192, 432),
                    (216, 456), (552, 384), (552, 432), (528, 456)]

eye_coords_list = [(312, 144), (432, 144)]

coords_dict = {"spine color": spine_coords_list, "claw color": claw_coords_list, "eye color": eye_coords_list}

color_booleans = {"spine color":{True: (255,0,0),
                                 False: (255,0,255),
                                 "coords":spine_coords_list},
                "claw color":{True: (0,255,0),
                               False: (255,252,0),
                              "coords": claw_coords_list},
                "eye color":{True: (0,227,255),
                             False: (0,103,255),
                             "coords":eye_coords_list}}

def organism_phenotype_maker(organism1, organism2, color_list):
    global organism_colors
    organism1.breeding(organism2)
    organism_colors = {}
    for g in organism1.offspring_genome:
        organism_colors[g.name] = color_list[g.name][g.isdominant]

def draw_colors(boolean_list, surface):
    surface.set_colorkey((0,0,0))
    for x in boolean_list:
        for y in boolean_list[x]["coords"]:
            color = organism_colors[x]
            default = pygame.rect.Rect(y, (24, 24))
            print(color)
            pygame.draw.rect(surface, color, default)
    #display.blit(square_surface, (0,0))

def wrapper_function(organism1, organism2, boolean_list, display):
    square_surface = pygame.Surface((768, 768))
    organism_phenotype_maker(organism1, organism2, boolean_list)
    draw_colors(boolean_list, square_surface)
    display.blit(square_surface, (0,0))

pygame.init()
screen = pygame.display.set_mode((768, 768))
on = True

while on:
    screen.fill((255, 255, 255))
    screen.blit(lizard_sprite, (0,0))
    wrapper_function(lizard1, lizard2, color_booleans, screen)
#     pygame.display.flip()
    time.sleep(0.5)
    for event in pygame.event.get():
        if event.type == QUIT:
            on = False
        
pygame.quit()




