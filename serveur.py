import asyncio
import websockets
import numpy as np

try:
    pixels = np.load('pixel.npy')
except:
    # Créez un tableau de dimensions 1000x700 avec la valeur "#FF0000"
    largeur = 1000
    hauteur = 700
    valeur = "#FF0000"

    # Créez un tableau rempli de cette valeur en utilisant NumPy
    pixels = np.full((hauteur, largeur), valeur, dtype='str')
    # Enregistrez le tableau dans un fichier au format Numpy (.npy)
    np.save('pixel.npy', pixels)
print(pixels)


# Liste des clients connectés
clients = set()

async def handle_client(websocket, path):
    # Ajoute le client à la liste des clients connectés
    clients.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            data = message.split(',')
            if data[0] == 'set_pixel':
                x, y, color = int(data[1]), int(data[2]), data[3]
                if 0 <= x < 10 and 0 <= y < 10:
                    pixels[y][x] = color
                    # Enregistrez le tableau dans un fichier au format Numpy (.npy)
                    np.save('pixel.npy', pixels)
                    # Envoie la mise à jour du tableau à tous les clients
                    for client in clients:
                        await client.send('update_pixels,' + ','.join([','.join(row) for row in pixels]))
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # Retire le client de la liste des clients connectés
        clients.remove(websocket)

# Démarrer le serveur WebSocket
start_server = websockets.serve(handle_client, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
