# Déploiement d'une application
> Nous allons déployer une application de web de base. Vous trouverez cette
> [application sur GitHub](TODO)

## Sans Docker
1. Démonstration du deploiement sans Docker
2. Vérifions les prérequis et faisons rouler l'application
    1. Python 3.x: `python --version`
    2. Pip3: `pip3 --version`
    3. Démarrons un environnement virtuel: `python3 -m venv docker-demo-env`
    4. Activons le `source docker-demo-env/bin/activate`
    5. Téléchargons les dépendances `pip3 install -r requirements.txt`
    6. Testons si l'application fonctionne
    `http://127.0.0.1:5000/`
3. Ce qu'il faut remarquer ici est que pour une application très simple, j'ai
   déjà beaucoup d'étapes répétitives et il y a déjà plusieurs possibilités de
   conflits de dépendances ou des problèmes d'environnements.

