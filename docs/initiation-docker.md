# Initiation Docker

## Étapes préliminaires

1. [Installation Docker](https://docs.docker.com/install/) en fonction de votre
   système d'opération.
2. [Création de compte](https://hub.docker.com/signup)

## Exploration initiale

1. Une fois installé, Docker agit comme un service ou une application accessible via un Terminal (ou une interface utilisateur)
2. Testons si l'installation a été complétée et le daemon démarré. Dans votre terminal, écrivez: `docker --version`
    1. Le numéro de version devrait être affiché.
3. Testons les commandes de bases.
    1. Listons tous les containers sur votre machine: `docker container ls`.
       Normalement, il ne devrait rien avoir pour l'instant.
    2. Listons tous les images sur votre machine: `docker image ls`. Normalement, il ne devrait rien avoir pour l'instant. 

## Premier Container local
1. Nous allons maintenant rouler notre premier Container, portez attention aux
   messages indiqués. Roulez: `docker run hello-world`
2. Regardons ce qui a changé: `docker image ls`
    3. Vous devriez avoir une nouvelle image.
3. Regardons ce qui a changé: `docker container ls -a`
    4. Vous devriez avoir un nouveau container qui a un status arrêté.
4. Plusieurs interactions avec les containers sont possibles.
    1. Afin de réutiliser un container local: `docker start --attach <contained_name/id>`
    2. Afin d'arrêter un container: `docker stop <container_name/id>`
    3. Afin d'effacer le container local: `docker rm <contained_name/id>`
    4. Afin de lister tous les processus actifs `docker ps`

## Nettoyage
1. Trouver l'id du container hello-world avec la commande `docker ps -a`
2. Effacer le container: `docker rm <contained_name/id>`
3. Effacer les images non utilisées par des container `docker image prune -a` 
