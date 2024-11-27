import asyncio
import websockets
import requests
import json

async def fetch_github_data(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url.split('github.com/')[1]}/contents"
    response = requests.get(api_url)
    return response.json()

async def send_file_content(websocket, file_info):
    if file_info['type'] == 'file':
        content = requests.get(file_info['download_url']).text
        await websocket.send(json.dumps({
            'filename': file_info['name'],
            'content': content
        }))
        print(f"Sent file: {file_info['name']}")

async def main():
    repo_url = "https://github.com/jaspreetsidhu3/voice_assistant"
    try:
        repo_data = await fetch_github_data(repo_url)
        if isinstance(repo_data, dict) and 'message' in repo_data:
            print(f"Error: {repo_data['message']}")
            return

        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            for file_info in repo_data:
                await send_file_content(websocket, file_info)
        print("All files processed successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())