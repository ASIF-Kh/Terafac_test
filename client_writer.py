import asyncio
import websockets
import json
import os

async def receive_and_write_files():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                filename = data['filename']
                content = data['content']

                # Create 'downloaded_files' directory if it doesn't exist
                os.makedirs('downloaded_files', exist_ok=True)

                # Write the file
                with open(os.path.join('downloaded_files', filename), 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Received and wrote: {filename}")

                # Execute the file and print its output
                if filename.endswith('.py'):
                    print(f"Executing {filename}:")
                    exec(content)
                    print("Execution complete.\n")

            except websockets.exceptions.ConnectionClosed:
                print("Connection to server closed")
                break
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(receive_and_write_files())

