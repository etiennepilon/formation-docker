# Déploiement d'une application
> Nous allons déployer une application web de base. Vous trouverez cette
> [application sur GitHub](https://github.com/etiennepilon/formation-docker/tree/master/src)

## Sans Docker
1. Démonstration du deploiement de l'application sans Docker
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
   conflits de dépendances ou des problèmes d'environnements. Pourrions nous
   simplement écrire du code afin de gèrer l'environnement au lieu de maintenir une
   documentation?

## Avec Docker
1. Nous allons donc coder notre environnement de développement au lieu de le documenter
2. Nous devons changer un peu le code afin  de s'assurer que le code est accessible à l'extérieur du container.
    1. Ouvrir main.py
    2. Commenter la ligne 14 (avec le character `#`)
    3. Décommenter la ligne 15
2. Ouvrir le Dockerfile dans le répertoire src/ afin de comprendre chaque section.
3. Compiler l'image afin de bâtir des container par la suite: `docker build -t docker-basic-webapp .`
    1. Ici, l'option `-t` permet de mettre un tag sur l'image afin de l'addresser par un nom au lieu d'un hash.
4. Une fois que l'image est compiler, valider qu'elle se trouve sur votre
   système avec `docker image ls`
5. Déployer un container avec l'image nouvellement créé `docker run -p 127.0.0.1:8800:5000 docker-basic-webapp`
    6. Ici, remarquer que lorsque je roule le container, j'utilise l'option -p. Cette option permet de spécifier le port sur lequel l'application va
       rouler. Cela très facile de faire des configurations dans ce cas.
6. Naviguer dans votre navigateur à l'adresse: `http://127.0.0.1:8800/`
    7. Voilà! Nous avons déployé notre premier container localement. Maintenant, nous n'avons plus besoin de documenter notre environnement.

### Arrêt, réutilisation et Nettoyage des containers
8. Ouvrez une autre fenêtre de votre terminal (sans fermer la fenêtre précédente).
9. Avec `docker ps`, trouver le id du container qui instancie notre image.
10. Afin d'arrêter le container simplement écrire `docker stop <container_id>
11. Lorsque vous faites `docker container ls -a`, vous devriez voir votre
    container qui a été créé. 
    1. Si vous roulez de nouveau `docker run -p 127.0.0.1:8800:5000 docker-basic-webapp`, un nouveau container sera créé à chaque fois.
    2. Afin d'éviter cette situation, nous pouvons réutiliser un container
    existant, `docker start --attach <container_id>`
    3. Une autre option est de toujours démarrer un container avec le flag --rm. Par exemple, `docker run --rm -p 127.0.0.1:8800:5000
       docker-basic-webapp`, afin que le container soit effacer à chaque fois.
