import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

USERNAME = os.environ.get('GRAPH_USERNAME')
TOKEN = os.environ.get('GRAPH_TOKEN')
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

# CREATE GRAPH
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

# CREATE A PIXEL
# today = datetime.now()
today = datetime(2021, 8, 24).strftime("%Y%m%d")

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_params = {
  "date": today,
  "quantity": "10",
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# UPDATE PIXEL
update_pixel_endpoint = f'{pixel_endpoint}/{today}'
print(update_pixel_endpoint)
update_pixel_params = {
  "quantity": "20",
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)


# DELETE PIXEL
date_pixel = "20220824"
delete_pixel_endpoint = f'{pixel_endpoint}/{date_pixel}'
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
