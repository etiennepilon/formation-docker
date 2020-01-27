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
    1. Pour ce faire, nous allons utiliser des variables d'environnements.
    2. Docker nous permet d'ajouter facilement d'ajouter des variables d'environnments avec l'option `-e NOM_VARIABLE="Valeur"`
2. Ouvrir le Dockerfile dans le répertoire src/ afin de comprendre chaque section.
3. Compiler l'image afin de bâtir des container par la suite: `docker build -t docker-basic-webapp .`
    1. Ici, l'option `-t` permet de mettre un tag sur l'image afin de l'addresser par un nom au lieu d'un hash.
4. Une fois que l'image est compiler, valider qu'elle se trouve sur votre
   système avec `docker image ls`
5. Déployer un container avec l'image nouvellement créé `docker run -p 127.0.0.1:8800:5000 -e HOSTNAME="0.0.0.0" docker-basic-webapp`
    6. Ici, remarquer que lorsque je roule le container, j'utilise l'option -p. Cette option permet de spécifier le port sur lequel l'application va
       rouler. Cela très facile de faire des configurations dans ce cas.
6. Naviguer dans votre navigateur à l'adresse: `http://127.0.0.1:8800/`
    7. Voilà! Nous avons déployé notre premier container localement. Maintenant, nous n'avons plus besoin de documenter notre environnement.

### Arrêt, réutilisation et Nettoyage des containers
8. Ouvrez une autre fenêtre de votre terminal (sans fermer la fenêtre précédente).
9. Avec `docker ps`, trouver le id du container qui instancie notre image.
10. Afin d'arrêter le container simplement écrire `docker stop <container_id>`
11. Lorsque vous faites `docker container ls -a`, vous devriez voir votre
    container qui a été créé. 
    1. Si vous roulez de nouveau `docker run -p 127.0.0.1:8800:5000 -e HOSTNAME="0.0.0.0" docker-basic-webapp`, un nouveau container sera créé à chaque fois.
    2. Afin d'éviter cette situation, nous pouvons réutiliser un container
    existant, `docker start --attach <container_id>`
    3. Une autre option est de toujours démarrer un container avec le flag --rm. Par exemple, `docker run --rm -p 127.0.0.1:8800:5000 -e HOSTNAME="0.0.0.0" docker-basic-webapp`, afin que le container soit effacer à chaque fois.

## Problème Circulaire - documentation des commandes Docker?

> Si vous avez remarqué, le problème de documentation des commandes est simplement repoussé. Maintenant, nous devons documenter la commande de démarrage de notre container. Heureusement, Docker offre une solution à ce problème.

### Docker compose
1. Lors de l'installation de Docker, vous avez aussi installé l'outil `docker-compose` qui permet de scripter le démarrage d'un container.
2. Dans le répertoire, ouvrez le fichier `docker-compose.yml`. Vous y retrouverez des configurations que vous reconnaitrez des exercises précédents.
3. Comme vous l'avez déjà fait, compiler l'image mais cette fois, avec
   `docker-compose build`.
    1. Vous pouvez valider que l'image existe bien avec `docker image ls`
4. Maintenant, vous pouvez simplement éxecuter la commande `docker-compose up webapp`
    1. Ici, webapp est le nom du Service défini dans le fichier docker-compose.yml
5. Vous pouvez maintenant naviguer à l'adresse `http://127.0.0.1:8800`.
6. Vous pouvez aussi voir le processus Docker avec `docker ps`

### Arrêt de Docker-compose
1. Dans une nouvelle fenêtre du Terminal, aller au répertoire où le fichier
   docker-compose.yml se trouve `cd path/to/docker-compose.yml`
2. Vous avez deux options afin d'arrêter le container.
    1. Si vous voulez effacer le container: `docker-compose down`
    2. Si vous voulez garder le container `docker-compose stop`

