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
