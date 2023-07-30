import json
import requests
import emoji



def retrieve_messages(input_channel_name, server_id, user_token):
    headers = {
        'authorization': f'{user_token}'
    }
    params = {
        'limit': 100  # Set the limit to 10 to retrieve only 1000 messages
    }

    # Get the list of channels in the server
    r = requests.get(f'https://discord.com/api/v9/guilds/{server_id}/channels', headers=headers)
    json_data = json.loads(r.text)

    channel_id = None
    for channel in json_data:
        # Check if the input channel name is a partial match to any existing channel name
        if input_channel_name.lower() in channel['name'].lower():
            channel_id = channel['id']
            break

    if not channel_id:
        print(f"No channel matching the input name '{input_channel_name}' found in the server.")
        return

    # Fetch messages from the found channel
    r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages',
                     headers=headers, params=params)
    json_data = json.loads(r.text)

    results = []
    for message in json_data:
        author_username = message['author']['username']

        # Get reactions if available, otherwise set an empty list
        reactions = message.get('reactions', [])

        reaction_counts = {}
        for reaction in reactions:
            emoji_name = reaction['emoji']['name']
            count = reaction['count']
            reaction_counts[emoji_name] = count

        image_url = None
        for attachment in message['attachments']:
            if attachment.get('url'):
                image_url = attachment['url']
                break  # Assuming there's only one image per message, break out after finding one
        content= message['content']
        timestamp= message['timestamp']
        channel_name= channel['name']
        result_data = {
            'channel_name' : channel_name,
            'author_username': author_username,
            'reaction_counts': reaction_counts,
            'image_url': image_url,
            'content' : content,
            'timestamp' : timestamp
            
        }
        results.append(result_data)

    # Save the results to a JSON file
    with open('channel_results_user.json', 'w') as file:
        json.dump(results, file, indent=4)


# Replace 'YOUR_USER_TOKEN' with your actual user token

user_token = 'NjA0NTExMzA0NDM4NTEzNjcw.G_KXpZ.4mNOLxE3Pi9eOHYa_uFrAhGNMZRtHfc3GrC0Uk'
input_channel_name = 'gpt-4-discussions'
server_id = '974519864045756446'  # Replace with the ID of the server where the channel is located


retrieve_messages(input_channel_name, server_id, user_token)







