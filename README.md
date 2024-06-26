# Auto-sokoban

## Sokoban

Le Sokoban est un jeu de puzzle. Le but de ce puzzle est de déplacer des
caisses à travers un entrepôt pour les amener à un emplacement bien
précis. Les caisses peuvent être
poussées, mais ne peuvent pas être
tirées. Le joueur doit être prudent et
bien anticiper ses mouvements pour
ne pas coincer une caisse contre un
mur ou dans un angle.
Une caisse peut être rangée sur
n’importe quel emplacement libre,
prévu à cet effet dans l'entrepôt. Les
caisses rangées peuvent tout de même être déplacées à nouveau si le joueur
a besoin de la pousser à un emplacement différent. La partie se termine
quand toutes les caisses ont été rangées aux emplacements qui leur étaient
prévus.

## L'IA

Etant des étudiants en IA, il est normal de vouloir intégrer une IA à notre jeu. Afin que celle-ci ne joue pas au hasard mais de manière "réfléchie" et optimal, elle utilise la distance euclidienne afin de calculer la distance puis un algorithme de recherche Breadth-First Search (BFS) pour determiner le meilleur coup à jouer.

## Gameplay

Le déplacement çe fait via les touches z, q, s, d, ou les flèches. La touche e sert à revenir sur le coup précédant. Le touche r à réinitialiser la partie. La touche échap à quitter. La touche t active l'IA qui va jouer à la place du joueur. 

## Architecture

Le projet est diviser en 4 fichier et 2 dossier. Le fichier build_game.py gère le gameplay, la crétaion de la matrice et la logique du jeu. Le fichier display_game.py gère l'interface graphique. Le fichier main.py appel build_game afin de lancer le jeu. Le fichier ia.py contient comme son nom l'indique l'IA permettant de gagner avec le meilleur score. Les dossiers image et music contiennent quand à eux les fichiers nécessaire au focntionnement du jeu
