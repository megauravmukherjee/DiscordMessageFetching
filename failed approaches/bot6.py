import websocket
import json
import threading
import time

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    print("Heartbeat Begin")
    while True:
        time.sleep(interval)
        heartbeatJSON = {
           "op" : 1, 
           "d" : "null"
        }
        send_json_request(ws, heartbeatJSON)
        print("heartbeat sent")

ws= websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval']/1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

token = "NjA0NTExMzA0NDM4NTEzNjcw.GIcxDa.1BsFTjIRHlQzi1eHc2ec9wCjFmh2t3Y2_IiQq8"
payload ={
    'op':2, #identify opcode
    'd' :
    {
        'token': token,
        'properties':
         {
            '$os':'windows',
            '$browser':'chrome',
            '$device':'pc'
         }
    }
}
send_json_request(ws, payload)

while True:
    event = recieve_json_response(ws)

    try:
       print(f"{event['d']['author']['username']}: {event['d']['content']}")
       if op_code==11:
        print("Heartbeat recieved") 
    except:
        pass



