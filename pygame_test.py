import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))
# fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

# Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
# perso = pygame.image.load("perso.png").convert()
perso = pygame.image.load("perso_8bits.png").convert_alpha()

fenetre.blit(perso, (200, 300))

# Rafraîchissement de l'écran
pygame.display.flip()

continuer = 1

# Boucle infinie
while continuer:
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle
