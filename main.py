import requests
from datetime import datetime

USERNAME = 'lmdelgallego'
TOKEN = "1q2w3e4r5t6"
GRAPH_ID = "graph-1"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
  "id": GRAPH_ID,
  "name": "Commits Graph",
  "unit": "commit",
  "type": "int",
  "color": "kuro",
}
headers = {
  "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.now()
today = datetime(2021, 8, 24)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_params = {
  "date": today.strftime("%Y%m%d"),
  "quantity": "10",
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

