"""
Nom : Ping-Tong-Points
Auteur : StaringLow
Fichier : 7-test_SystèmeDePoints.py
Création : 06-09-2026
Version : 1.0
Description : Développement du système de points pour le jeu Ping-Tong-Points. (Test de la création du système de points.)
"""

###################
### IMPORTATION ###
###################

# Importation
import pygame
import random

#################
### VARIABLES ###
#################

# Initialisation des variables du jeu.
running = True # Permet de démarrer la page de jeu.
player1_y = 250 # Position de départ du joueur 1 (Côté gauche du terrain de jeu.)
player2_y = 250 # Position de départ du joueur 2 (Côté droit du terrain de jeu.)
player_speed = 0.3 # Vitesse de déplacement des joueurs.
ball_speed_x = random.choice([-0.1, 0.1]) # Vitesse de déplacement et direction de la balle sur l'axe X.
ball_speed_y = random.choice([-0.1, 0.1]) # Vitesse de déplacement de la balle sur l'axe Y.
ball_x = 400 # Position de départ de la balle sur l'axe X.
ball_y = 300 # Position de départ de la balle sur l'axe Y.
score_player1 = 0 # Score du joueur 1 (Côté gauche du terrain de jeu.)
score_player2 = 0 # Score du joueur 2 (Côté droit du terrain de jeu.)

######################
### INITIALISATION ###
######################

# Initialisation de pygame (Initialisation du son, affichage, etc...)
pygame.init()
font = pygame.font.Font(None, 50) # Police d'écriture pour l'affichage du score.

# Affichage de la fenêtre de jeu (800 pixels de largeur sur 600 pixels de hauteurs).
window = pygame.display.set_mode((800, 600))

#####################
### BOUCLE DU JEU ###
#####################

# Boucle principale du jeu (Boucle qui permet de garder la fenêtre ouverte et d'attendre que l'utilisateur ferme la fenêtre).
while (running):

    ###################
    ### PARAMETRAGE ###
    ###################

    # Remplissage de la fenêtre avec une couleur (noir).
    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed() # Récupération des touches du clavier.

    ##############
    ### CENTRE ###
    ##############

    # Dessin de la ligne a trait centrale (Séparant les deux terrains du jeu.)
    for y in range(0, 600, 20):
        pygame.draw.line(window, (255, 255, 255), (400, y), (400, y + 10), 5)

    ################
    ### JOUEUR 1 ###
    ################

    # Trait du joueur 1 (Côté gauche du terrain de jeu.)
    pygame.draw.rect(window, (255, 255, 255), (20, player1_y, 20, 100), 0)

    # Déplacement du joueur 1 (Côté gauche du terrain de jeu.)
    if keys[pygame.K_w]: # Si la touche w haut est pressée, le joueur 1 monte.
        player1_y -= player_speed
    if keys[pygame.K_s]: # Si la touche s est pressée, le joueur 1 descend.
        player1_y += player_speed
        
    if player1_y < 0: # Si le joueur 1 sort du terrain de jeu par le haut, il revient en bas.
        player1_y = 0
    if player1_y > 500: # Si le joueur 1 sort du terrain de jeu par le bas, il revient en haut.
        player1_y = 500

    ################
    ### JOUEUR 2 ###
    ################

    # Trait du joueur 2 (Côté droit du terrain de jeu.)
    pygame.draw.rect(window, (255, 255, 255), (760, player2_y, 20, 100), 0)

    # Déplacement du joueur 2 (Côté droit du terrain de jeu.)
    if keys[pygame.K_UP]: # Si la touche flèche haut est pressée, le joueur 2 monte.
        player2_y -= player_speed  
    if keys[pygame.K_DOWN]: # Si la touche flèche bas est pressée, le joueur 2 descend.
        player2_y += player_speed

    if player2_y < 0: # Si le joueur 2 sort du terrain de jeu par le haut, il revient en bas.
        player2_y = 0
    if player2_y > 500: # Si le joueur 2 sort du terrain de jeu par le bas, il revient en haut.
        player2_y = 500

    #############
    ### BALLE ###
    #############

    # Dessin de la balle (Cercle blanc au centre du terrain de jeu.)
    pygame.draw.circle(window, (255, 255, 255), (ball_x, ball_y), 10)

    ball_x += ball_speed_x # Position de départ de la balle sur l'axe X.
    ball_y += ball_speed_y # Position de départ de la balle sur l'axe Y

    # Gestion des collisions de la balle avec les bords de la fenêtre (Si la balle touche le bord de la fenêtre, elle rebondit.)
    if ball_y <= 10:
        ball_speed_y = -ball_speed_y
    if ball_y >= 590:
        ball_speed_y = -ball_speed_y

    ##########################
    ### TIRE AVEC RAQUETTE ###
    ##########################
    # Gestion des collisions de la balle avec les raquettes (Si la balle touche une raquette, elle rebondit.)
    if ball_x <= 50 and player1_y <= ball_y <= player1_y + 100:
        ball_speed_x = -ball_speed_x

    if ball_x >= 750 and player2_y <= ball_y <= player2_y + 100:
        ball_speed_x = -ball_speed_x

    
    #######################
    ### MANCHE TERMINEE ###
    #######################

    # Gestion des points (Si la balle sort du terrain de jeu, le joueur adverse marque un point et la balle revient au centre du terrain de jeu.)
    if ball_x < 0 or ball_x > 800:
        if ball_x < 0:
            score_player2 += 1
        else:
            score_player1 += 1
        
        ball_x = 400
        ball_y = 300
        ball_speed_x = random.choice([-0.1, 0.1])
        ball_speed_y = random.choice([-0.1, 0.1])

    # Affichage du score des joueurs (Côté gauche et droit du terrain de jeu.)
    text_score_player1 = font.render(str(score_player1), True, (255, 255, 255))
    rect_score_player1 = text_score_player1.get_rect(center=(360, 30))

    text_score_player2 = font.render(str(score_player2), True, (255, 255, 255))
    rect_score_player2 = text_score_player2.get_rect(center=(440, 30))

    window.blit(text_score_player1, rect_score_player1)
    window.blit(text_score_player2, rect_score_player2)

    ###############
    ### QUITTER ###
    ###############

    # Evenement de fermeture de la fenêtre (Lorsque l'utilisateur clique sur la croix, la fenêtre se ferme).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ########################
    ### RAFRAICHISSEMENT ###
    ########################

    #   Rafraichissement de l'affichage (Met à jour l'affichage de la fenêtre).
    pygame.display.flip()
    