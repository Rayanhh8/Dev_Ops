# 1. Image de base légère avec Python pré-installé
FROM python:3.9-slim

# 2. On se place dans le dossier /app à l'intérieur du conteneur
WORKDIR /app

# 3. On copie le fichier des dépendances d'abord (optimisation du cache)
COPY requirements.txt .

# 4. On installe les bibliothèques nécessaires (ex: FastAPI, Uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le reste du code du dossier backend vers /app
COPY . .

# 6. On indique que l'app écoute sur le port 8000
#EXPOSE 8000

# 7. La commande pour lancer l'API
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "app.py"]