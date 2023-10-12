from flask import Flask, render_template, request, jsonify
import socket
import threading

# Définition des paramètres de connexion
HOST = 'localhost'  # adresse IP du serveur
PORT = 5001  # port d'écoute du serveur

# Création d'une socket pour établir la connexion avec le serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

app = Flask(__name__)

# Initialisation du tableau avec des couleurs par défaut
tableau = [["#FFFFFF" for _ in range(1000)] for _ in range(700)]

def envoyer_message(message):
    client_socket.sendall(message.encode())
    print(client_socket.recv(1024).decode())
    #client_socket.close()

@app.route('/')
def index():
    return render_template('index.html', tableau=tableau)

@app.route('/update_cell', methods=['POST'])
def update_cell():
    x = int(request.form['x'])
    y = int(request.form['y'])
    color = request.form['color']
    envoyer_message("test")
    tableau[y][x] = color
    return jsonify({'message': 'Cellule mise à jour avec succès'})

if __name__ == '__main__':
    app.run(debug=True)
