"""
Nom : Ping-Tong-Points
Auteur : StaringLow
Fichier : 4-test_pygame-CréationDesJoueurs(Jouable).py
Création : 06-09-2026
Version : 1.00
Description : Création des joueurs (Jouable) pour le jeu Ping-Tong-Points. (Test de la création des joueurs.)
"""

# Importation
import pygame

# Initialisation des variables du jeu.
running = True # Permet de démarrer la page de jeu.
player1_y = 250 # Position de départ du joueur 1 (Côté gauche du terrain de jeu.)
player2_y = 250 # Position de départ du joueur 2 (Côté droit du terrain de jeu.)
player_speed = 0.3 # Vitesse de déplacement des joueurs.

# Initialisation de pygame (Initialisation du son, affichage, etc...)
pygame.init()

# Affichage de la fenêtre de jeu (800 pixels de largeur sur 600 pixels de hauteurs).
window = pygame.display.set_mode((800, 600))

# Boucle principale du jeu (Boucle qui permet de garder la fenêtre ouverte et d'attendre que l'utilisateur ferme la fenêtre).
while (running):

    # Remplissage de la fenêtre avec une couleur (noir).
    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed() # Récupération des touches du clavier.

    # Dessin de la ligne a trait centrale (Séparant les deux terrains du jeu.)
    for y in range(0, 600, 20):
        pygame.draw.line(window, (255, 255, 255), (400, y), (400, y + 10), 5)

    # Joueur 1 (Côté gauche du terrain de jeu.)
    # Trait du joueur 1 (Côté gauche du terrain de jeu.)
    pygame.draw.rect(window, (255, 255, 255), (20, player1_y, 20, 100), 0)

    # Déplacement du joueur 1 (Côté gauche du terrain de jeu.)
    if keys[pygame.K_w]: # Si la touche w haut est pressée, le joueur 1 monte.
        player1_y -= player_speed

    if keys[pygame.K_s]: # Si la touche s est pressée, le joueur 1 descend.
        player1_y += player_speed

    # Joueur 2 (Côté droit du terrain de jeu.)
    # Trait du joueur 2 (Côté droit du terrain de jeu.)
    pygame.draw.rect(window, (255, 255, 255), (760, player2_y, 20, 100), 0)

    # Déplacement du joueur 2 (Côté droit du terrain de jeu.)
    if keys[pygame.K_UP]: # Si la touche flèche haut est pressée, le joueur 2 monte.
        player2_y -= player_speed  

    if keys[pygame.K_DOWN]: # Si la touche flèche bas est pressée, le joueur 2 descend.
        player2_y += player_speed


    # Evenement de fermeture de la fenêtre (Lorsque l'utilisateur clique sur la croix, la fenêtre se ferme).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #   Rafraichissement de l'affichage (Met à jour l'affichage de la fenêtre).
    pygame.display.flip()
    