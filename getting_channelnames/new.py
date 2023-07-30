import requests
import json

def get_channel_names(server_id):
  """Gets the channel names from a Discord server.

  Args:
    server_id: The ID of the Discord server.

  Returns:
    A list of the channel names in the server.
  """
  headers = {
        'authorization': f'NjA0NTExMzA0NDM4NTEzNjcw.G_KXpZ.4mNOLxE3Pi9eOHYa_uFrAhGNMZRtHfc3GrC0Uk'
    }
  url = "https://discord.com/api/v8/guilds/{}/channels".format(server_id)
  response = requests.get(url, headers = headers)

  if response.status_code != 200:
    raise ValueError("Error getting channel names: {}".format(
        response.status_code))

  channel_names = []
  for channel in response.json():
    channel_names.append(channel['name'])

  return channel_names


if __name__ == "__main__":

  server_id = input("Enter the server ID: ")

  try:
    channel_names = get_channel_names(server_id)
  except ValueError as e:
    print(e)
  else:
    print(channel_names)
  with open('channel_names.json', 'w') as file:
        json.dump(channel_names, file, indent=4)