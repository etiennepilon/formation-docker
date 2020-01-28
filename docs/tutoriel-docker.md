# Déploiement d'une application de base
> Nous allons déployer une application web de base. Vous trouverez cette
> [application sur GitHub](https://github.com/etiennepilon/formation-docker/tree/master/src/webapp_part1)

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

# Déploiement d'une application avec données persistentes
> Nous allons maintenant déployer une application web similaire à la précédente mais cette fois avec données persistentes. Vous trouverez cette
> [application sur GitHub](https://github.com/etiennepilon/formation-docker/tree/master/src/webapp_part2)

## Création de l'image
1. Nous allons réutiliser exactement le même fichier `docker-compose.yml`
    1. Un seul ajout c'est glissé afin de faciliter la suite du tutoriel. Vous
       remarquerez que l'entrée `image: etiennepilon/tutoriel-docker` c'est
       ajouter au fichier.
3. Comme vous l'avez déjà fait, compiler l'image mais cette fois, avec `docker-compose build`.
    1. Vous pouvez valider que l'image existe bien avec `docker image ls`
4. Maintenant, vous pouvez simplement éxecuter la commande `docker-compose up webapp`
5. Vous pouvez maintenant naviguer à l'adresse `http://127.0.0.1:8800`.
6. Vous pouvez aussi voir le processus Docker avec `docker ps`

### Ajout de membre dans l'application
7. Via le menu `Add Member` dans l'application, ajouter des membres au tableau.
   Idéalement

## Confirmation de l'écriture des données et exploration d'une container
1. L'application sauvegarde sur le disque les noms des nouveaux membres. Dans le
   cas de cette application, les données sont sauvegardés dans un fichier JSON.
   Par contre, nous aurions pu utiliser quelconque base de données (SQL,
   PostGres, etc.) Le fichier `members.json` se trouve simplement dans le
   dossier `data/`.
2. Jusqu'à maintenant, nous n'avons pas exploré nos containers. Allons voir si
   les données sont belle et bien écrites sur le disque.
3. Afin de vous connecter au container, vous devez tout d'abord vous assurez
   qu'il roule. Roulez `docker ps`
4. Ensuite, nous ouvrirons un shell Bash au container. C'est l'équivalent
   d'utiliser le "système d'opération" du container.
   1. Roulez la commande `docker run -it etiennepilon/tutoriel-docker`
   2. Vous êtes maintenant connecté. Vous pouvez retrouver tous les fichiers
      avec lesquels nous travaillons. Confirmez avec `ls`.
   3. Ensuite, nous irons voir le contenu du fichier `members.json`. La façon la
      plus simple est d'afficher directement son contenu avec la commande `cat
      data/members.json
   4. Il n'y a rien..!
   5. Quitter le shell bash simplement avec `CTRL+D`
5. On constate que les données ne sont pas écrite sur le disque, c'est un
   problème.

## Redémarrage du Container
1. Arrêtons le container avec la commande `docker-compose down`
2. Redémarrons le container avec la commande `docker-compose up webapp`. Comme vous
   voyez en accédant à la route `/table`, il n'y a plus aucun membres qui avait
   été ajouté préalablement.

## Création d'un Volume
1. Docker ne garde aucune donnée persistente. Un container maintien toujours
   son état sur le Disque et "copie" l'image sur laquelle il est basée.
2. Pour résoudre cette problématique, nous allons ajouter un Volume. Un Volume
   est l'équivalent de "mount" un disque dur ou une partition sur un ordinateur.
   Il nous donne accès en lecture et écriture à ce disque.
3. Dans notre cas, nous allons "mount" un dossier de notre ordinateur dans notre
   container afin qu'il puisse y lire/écrire.
   1. Ouvrez `docker-compose.yml` dans un éditeur de texte ou IDE.
   2. Dans la section webapp, ajouter une sous-section `volumes` ainsi:
   ```
    volumes:
        -./data:/usr/src/app/data
   ```
   3. Ce code aura pour effet de lier le dossier `data` local au dossier du
      container `/usr/src/app/data`. Ce dossier est où l'application écrit son
      fichier JSON.
   4. Sauvegarder le fichier.

## Création de l'image avec le nouveau Volume et validation de la solution
1. Il ne reste plus qu'à rebâtir l'image `docker-compose build` et la reéxecuter
   avec `docker-compose up webapp`.
2. Via le menu `Add Member` dans l'application, ajouter des membres au tableau.
3. Validons que l'écriture se fait simplement en regardant local du fichier
   `data/members.json`
4. Nous constatons donc qu'il est possible de maintenir des données
   persistentes dans un container qui écrit directement sur notre disque!
