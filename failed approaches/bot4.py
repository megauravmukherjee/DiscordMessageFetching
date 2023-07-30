import requests
import json

server_id = '974519864045756446'
HEADERS = {'authorization': 'NjA0NTExMzA0NDM4NTEzNjcw.GIcxDa.1BsFTjIRHlQzi1eHc2ec9wCjFmh2t3Y2_IiQq8'}
LIMIT=100
all_messages = []

r = requests.get(f'https://discord.com/api/v9/guilds/{server_id}/channels', headers=HEADERS)
all_messages.extend(r.json())

print(f'len(r.json()) is {len(r.json())}','\n')

while len(r.json()) == LIMIT:
    all_messages.extend(r.json())
with open("data.json" , "w") as f:
    json.dump(all_messages, f)
