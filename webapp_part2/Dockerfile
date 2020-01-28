# L'image prise de DockerHub de d'un OS de base avec Python 3.X installer
FROM python:3

# Le répertoire dans lequel le code sera dans le container et où les prochaines
# commandes seront éxecutées
WORKDIR /usr/src/app

# Commande qui copie le contenu du répertoire src/ dans WORKDIR
COPY . .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Ouverture du port 5000 local
EXPOSE 5000

# La commande à éxecuter quand nous allons "run" l'application
CMD ["python", "./main.py"]
