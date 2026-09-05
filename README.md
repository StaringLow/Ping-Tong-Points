# Ping-Tong-Points 🏓

Un clone du jeu **Pong**, le tout premier jeu vidéo d'arcade sorti en **1972**, recréé en **Python** avec **Pygame**.

![Statut](https://img.shields.io/badge/statut-en%20d%C3%A9veloppement-yellow)
![Python](https://img.shields.io/badge/python-3.14-blue)
![Pygame](https://img.shields.io/badge/pygame--ce-2.5.8-green)

---

## 📖 À propos du projet

Ce dépôt n'a pas pour ambition de proposer une version innovante ou complexe de Pong : c'est avant tout un **projet d'apprentissage**.

Après une pause avec Python, j'ai voulu m'y remettre en repartant sur un projet concret plutôt que de simples exercices théoriques. Recréer Pong — un jeu simple dans son concept mais riche en petites problématiques de programmation (boucle de jeu, affichage, entrées clavier, physique de base, collisions, score) — est un excellent moyen de se réapproprier le langage tout en construisant quelque chose de jouable.

Ce projet sert donc à :
- Remettre en pratique les bases de Python (variables, boucles, conditions, fonctions)
- Découvrir et manipuler la bibliothèque **Pygame** pour la première fois (ou après longtemps)
- Comprendre des concepts fondamentaux du développement de jeux vidéo : boucle de jeu, double buffering, détection de collisions, gestion des entrées utilisateur
- Structurer un projet Python de façon propre, avec versionnement Git/GitHub

Le code n'est donc pas toujours optimisé ou "parfait" — il reflète une progression d'apprentissage, étape par étape, avec les erreurs et ajustements que ça implique. N'hésite pas à explorer l'historique des commits pour voir cette évolution !

## 🕹️ Le jeu

**Pong** est un jeu d'arcade à deux joueurs simulant du tennis de table en 2D, vu de dessus. Chaque joueur contrôle une raquette verticale sur un côté de l'écran et doit renvoyer une balle pour empêcher qu'elle ne sorte de son côté du terrain. Chaque balle manquée donne un point à l'adversaire.

Cette version reprend les mécaniques essentielles du jeu original :
- Un terrain délimité par une ligne centrale pointillée séparant les deux camps
- Deux raquettes, une par joueur, déplaçables verticalement
- Une balle rebondissant sur les raquettes et les bords du terrain
- Un système de score

## ✨ Fonctionnalités

### ✅ Déjà implémentées
- [x] Fenêtre de jeu (800x600 pixels) avec boucle de jeu principale
- [x] Ligne centrale pointillée séparant visuellement les deux terrains
- [x] Affichage des deux raquettes (joueur gauche / joueur droit)

### 🚧 En cours de développement
- [ ] Déplacement des raquettes au clavier
- [ ] Balle avec mouvement et rebonds sur les bords
- [ ] Détection de collision balle/raquette
- [ ] Système de score affiché à l'écran
- [ ] Mode 1 joueur contre un bot (intelligence artificielle simple)
- [ ] Mode 2 joueurs en local
- [ ] Écrans de menu, pause et fin de partie
- [ ] Effets sonores (rebond, score, etc.)

## 🛠️ Prérequis

- [Python](https://www.python.org/downloads/) 3.10 ou supérieur
- [pip](https://pip.pypa.io/en/stable/) (généralement inclus avec Python)

## 🚀 Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/<ton-utilisateur>/Ping-Tong-Points.git
   cd Ping-Tong-Points
   ```

2. **Créer un environnement virtuel** *(recommandé)*
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows :
     ```bash
     venv\Scripts\activate
     ```
   - macOS / Linux :
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install pygame-ce
   ```

   > 💡 Ce projet utilise **pygame-ce** (Community Edition), un fork actif et à jour de la bibliothèque Pygame, offrant une meilleure compatibilité avec les versions récentes de Python. Son fonctionnement et son API restent identiques à Pygame classique (`import pygame`).

## ▶️ Lancer le jeu

```bash
python Développement/Game/main.py
```

## 🎮 Contrôles *(à venir)*

| Action                 | Joueur 1 (gauche) | Joueur 2 (droite) |
|------------------------|:------------------:|:-------------------:|
| Déplacer vers le haut  | `Z` / `↑`          | `↑`                 |
| Déplacer vers le bas   | `S` / `↓`          | `↓`                 |
| Quitter le jeu         | Fermer la fenêtre  | —                   |

## 📁 Structure du projet

```
Ping-Tong-Points/
├── Développement/
│   └── Game/
│       └── main.py          # Point d'entrée du jeu
├── Documentations/           # Notes et documentation du projet
├── .gitignore
├── .gitattributes
└── README.md
```

## 🧰 Technologies utilisées

- **Python 3.14**
- **pygame-ce** — bibliothèque graphique utilisée pour l'affichage, la gestion des entrées clavier et la boucle de jeu

## 📝 Progression du développement

Le projet avance étape par étape, chaque étape correspondant à un concept appris ou consolidé :

1. Mise en place de Pygame et de la boucle de jeu principale
2. Affichage statique des éléments du terrain (ligne centrale, raquettes)
3. Gestion des entrées clavier pour déplacer les raquettes
4. Ajout de la balle et de sa physique de base (déplacement, rebonds)
5. Détection des collisions (balle/raquette, balle/bords)
6. Logique de jeu complète (score, victoire, réinitialisation)
7. Finitions (menus, sons, IA du bot pour le mode solo)

## 📄 Licence

Projet à but éducatif. Aucune licence formelle n'est appliquée pour l'instant — n'hésite pas à me contacter si tu souhaites réutiliser ou t'inspirer du code.
