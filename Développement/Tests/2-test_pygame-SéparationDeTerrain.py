"""
Nom : Ping-Tong-Points
Auteur : StaringLow
Fichier : test_pygame-SéparationDeTerrain.py
Création : 05-09-2026
Version : 1.00
Description : Test de la séparation entre terrain des deux joueurs. (Test de la ligne centrale du terrain de jeu.)
"""

# Importation
import pygame

# Initialisation des variables du jeu.
running = True

# Initialisation de pygame (Initialisation du son, affichage, etc...)
pygame.init()

# Affichage de la fenêtre de jeu (800 pixels de largeur sur 600 pixels de hauteurs).
window = pygame.display.set_mode((800, 600))

# Boucle principale du jeu (Boucle qui permet de garder la fenêtre ouverte et d'attendre que l'utilisateur ferme la fenêtre).
while (running):

    # Remplissage de la fenêtre avec une couleur (noir).
    window.fill((0, 0, 0))

    # Dessin de la ligne a trait centrale (Séparant les deux terrains du jeu.)
    for y in range(0, 600, 20):
        pygame.draw.line(window, (255, 255, 255), (400, y), (400, y + 10), 5)

    # Evenement de fermeture de la fenêtre (Lorsque l'utilisateur clique sur la croix, la fenêtre se ferme).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #   Rafraichissement de l'affichage (Met à jour l'affichage de la fenêtre).
    pygame.display.flip()
