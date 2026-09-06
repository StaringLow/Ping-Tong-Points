"""
Nom : Ping-Tong-Points
Auteur : StaringLow
Fichier : 1-test_pygame-installation.py
Création : 05-09-2026
Version : 1.00
Description : Test d'installation de Pygame + création de la fenêtre de jeu.
"""

# Importation
import pygame

# Initialisation des variables du jeu.
running = True # Permet de démarrer la page de jeu.
 
# Initialisation de pygame (Initialisation du son, affichage, etc...)
pygame.init()

# Affichage de la fenêtre de jeu (800 pixels de largeur sur 600 pixels de hauteurs).
window = pygame.display.set_mode((800, 600))

# Boucle principale du jeu (Boucle qui permet de garder la fenêtre ouverte et d'attendre que l'utilisateur ferme la fenêtre).
while (running):

    # Remplissage de la fenêtre avec une couleur (noir).
    window.fill((0, 0, 0))

    # Evenement de fermeture de la fenêtre (Lorsque l'utilisateur clique sur la croix, la fenêtre se ferme).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #   Rafraichissement de l'affichage (Met à jour l'affichage de la fenêtre).
    pygame.display.flip()
