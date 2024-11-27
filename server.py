import asyncio
import websockets

clients = set()

async def handle_client(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            for client in clients:
                if client != websocket:
                    await client.send(message)
    finally:
        clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())