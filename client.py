import asyncio
import websockets

async def update_pixels():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = message.split(',')
            if data[0] == 'update_pixels':
                print(data)
                pixels = [row.split(',') for row in data[1:]]
                for row in pixels:
                    print(' '.join(row))
                print("\n")

async def main():
    asyncio.create_task(update_pixels())

    while True:
        try:
            x = int(input("Entrez la coordonnée x du pixel à modifier (0-1000) : "))
            y = int(input("Entrez la coordonnée y du pixel à modifier (0-700) : "))
            color = input("Entrez la couleur du pixel (format HEX, ex: #FF0000) : ")
            async with websockets.connect("ws://localhost:8765") as websocket:
                await websocket.send(f'set_pixel,{x},{y},{color}')
        except ValueError:
            print("Coordonnées invalides. Veuillez réessayer.")

asyncio.get_event_loop().run_until_complete(main())
