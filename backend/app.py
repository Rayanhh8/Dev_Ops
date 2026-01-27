#from fastapi import FastAPI
#app = FastAPI()
#@app.get("/")
#def root():
#    return {"message": "Hello from Docker!"}


from flask import Flask, jsonify, request  
from flask_cors import CORS  
from pymongo import MongoClient
import os
import datetime  # <-- Ajoute ça pour la date des messages

app = Flask(__name__)
CORS(app)  # <--- Ajoute ça pour autoriser le frontend

# Connexion à MongoDB (on utilise le nom du service K8s : mongodb-service)
client = MongoClient('mongodb://mongodb-service:27017/')
db = client.blog_db
messages_col = db.messages
collection = db.visites

# @app.route('/')
# def hello():
#     # On incrémente le compteur dans MongoDB
#     res = collection.find_one_and_update(
#         {"id": "compteur"},
#         {"$inc": {"nb": 1}},
#         upsert=True,
#         return_document=True
#     )
#     return f"Hello from Docker! Nombre de visites : {res['nb']}"

@app.route('/messages', methods=['GET'])
def get_messages():
    # On récupère les 10 derniers messages
    messages = list(messages_col.find({}, {'_id': 0}).sort('date', -1).limit(10))
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def add_message():
    data = request.json
    new_message = {
        "text": data.get("text"),
        "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    messages_col.insert_one(new_message)
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    
    
    
   