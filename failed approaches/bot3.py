import requests

def get_channel_info(channel_id):
  """Gets the information about a channel.

  Args:
    channel_id: The ID of the channel to get the information about.

  Returns:
    The information about the channel.
  """

  url = "https://discord.com/api/v9/channels/" + channel_id
  response = requests.get(url)
  data = response.json()

  return data

def get_message_history(channel_id):
  """Gets the message history for a channel.

  Args:
    channel_id: The ID of the channel to get the message history for.

  Returns:
    The message history for the channel.
  """

  url = "https://discord.com/api/v9/channels/" + channel_id + "/messages"
  response = requests.get(url)
  data = response.json()

  return data

def main():
  channel_id = "1134738417893257268"

  channel_info = get_channel_info(channel_id)
  message_history = get_message_history(channel_id)

  print(channel_info)
  print(message_history)

if __name__ == "__main__":
  main()
