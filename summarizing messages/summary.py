import json
from collections import Counter

def get_summary(data):

# load the JSON data

# count the number of messages and unique users
  num_messages = len(data)
  unique_users = set(msg['author_username'] for msg in data)

# count the number of messages per user
  user_messages = Counter(msg['author_username'] for msg in data)

# get the top 10 users and their message counts
  top_users = user_messages.most_common(10)

# count the number of members in the channel
  num_members = len(set(msg['channel_name'] for msg in data))

  summary_data = {
    'Number of total messages:' : num_messages,
    "Unique Users": list(sorted(list(unique_users))),
    'user message' : user_messages,
    'top_users' : top_users

  }

  return summary_data
# print the summary
  

"""Gets the summary of the data.

  Args:
    data: The data to summarize.

  Returns:
    A dictionary containing the summary of the data.
  """

"""#  summary = {}
 # total_messages = 0
  #unique_users = []
  #top_users = []
  #members = 0
  #for message in data:
    #total_messages += 1
    #unique_users.append(message["author_username"])
    #if message["author_username"] in top_users:
      #continue
    ##if message["reaction_counts"] == {}:
      #members += 1
    #else:
      #top_users.append(message["author_username"])
  ##summary["total_messages"] = total_messages
  #summary["unique_users"] = unique_users
  #summary["top_users"] = top_users
  #summary["members"] = members
  #return summary"""
def read_json_file(file_path):
  
    """Reads a JSON file.

  Args:
    file_path: The path to the JSON file.

  Returns:
    The contents of the JSON file as a Python object."""


    with open(file_path, "r") as file:
      data = file.read()
    return json.loads(data)
if __name__ == "__main__":
  file_path = r"C:\Users\Gaurav Mukherjee\Documents\channel_results_user.json"
  data = read_json_file(file_path)  
  summary = get_summary(data)
  with open('summary.json', "w") as file:
    json.dump(summary, file)
