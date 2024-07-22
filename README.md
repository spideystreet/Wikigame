# WikiGame

WikiGame est un jeu où l'objectif est de naviguer d'une page Wikipedia à une autre en utilisant uniquement les liens hypertextes présents sur les pages, avec le moins de clics possible. Ce README couvre les trois versions du jeu, chacune apportant des améliorations et des fonctionnalités supplémentaires.
La VERSION 3 est le wikigame_v3.py, le livrable attendu et commenté.
Je laisse les 3 versions pour moi si je suis amener à réutiliser plus tard :p

## Installation Générale

### Prérequis
- Python 3.x
- TkInter (inclus avec Python sur la plupart des systèmes)

### Étapes d'installation
1. Clonez le dépôt :
   ```bash
   git clone <url_du_depot>
   cd wikigame

### Dépendances
pip install -r requirements.txt

### WikiGame - Version 1
Cette version est en mode CLI brute. L'objectif est de naviguer d'une page Wikipedia aléatoire à une autre en utilisant uniquement les liens hypertextes présents sur les pages, avec le moins de clics possible.

Utilisation
Exécutez le jeu : python3 wikigame_v1.py

Fonctionnement
Le programme affichera les liens hypertextes disponibles sur la page actuelle et vous demandera de choisir un lien pour naviguer jusqu'à la page cible.


### WikiGame - Version 2
Cette version utilise tkinter pour améliorer l'interface CLI, offrant une expérience utilisateur plus agréable.

Utilisation
Exécutez le jeu : python3 wikigame_v2.py

Fonctionnement
Le programme affichera une interface améliorée en ligne de commande avec les liens hypertextes disponibles sur la page actuelle. Sélectionnez un lien pour naviguer jusqu'à la page cible.

### WikiGame - Version 3
Cette version utilise TkInter pour une interface graphique et inclut des fonctionnalités avancées telles que le mode historique, le mode timer et le mode thématique.

Utilisation
Mode Normal
Exécutez le jeu : python3 wikigame_v3.py

Exécutez le jeu avec un fichier contenant des URLs thématiques : python wikigame_tkinter_v3.py -d <chemin_du_fichier>

Fonctionnement
Le programme affichera une interface graphique avec les liens hypertextes disponibles sur la page actuelle. Sélectionnez un lien pour naviguer jusqu'à la page cible. Le programme inclut un compteur de temps et affiche l'historique des pages visitées une fois que vous atteignez la page cible.

Fonctionnalités Avancées
Mode Historique : Affiche l'historique des pages visitées.
Mode Timer : Compte le temps pris pour atteindre la page cible.
Mode Thématique : Utilise un corpus réduit de pages Wikipedia basées sur un thème spécifique.
Avec ces instructions, vous devriez pouvoir installer et exécuter chaque version du WikiGame, en profitant des fonctionnalités de base et avancées selon la version utilisée.