import discord

def get_channel_info(channel):
  """Gets the information about a channel.

  Args:
    channel: The channel to get the information about.

  Returns:
    The information about the channel.
  """

  return {
      "name": channel.name,
      "topic": channel.topic,
      "members": [member.name for member in channel.members],
  }

def get_message_history(channel):
  """Gets the message history for a channel.

  Args:
    channel: The channel to get the message history for.

  Returns:
    The message history for the channel.
  """

  messages = []
  for message in channel.history():
    messages.append({
        "text": message.content,
        "timestamp": message.timestamp,
    })

  return messages

def get_user_info(user):
  """Gets the information about a user.

  Args:
    user: The user to get the information about.

  Returns:
    The information about the user.
  """

  return {
      "username": user.name,
      "discriminator": user.discriminator,
      "avatar": user.avatar,
      "join_date": user.joined_at,
  }

def on_message(message):
  """Called when a new message is sent.

  Args:
    message: The new message.
  """

  channel_info = get_channel_info(message.channel)
  message_history = get_message_history(message.channel)
  user_info = get_user_info(message.author)

  print(f"Channel: {channel_info}")
  print(f"Message history: {message_history}")
  print(f"User: {user_info}")

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print("Ready!")

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  await on_message(message)

client.run('MTEzNDcxMTU4MzI2MDU2MTQyOA.GPyvZr.3egF8Z-Gb4TfDSO9zlyr7jUpGtJ20DC9xeoAb4')