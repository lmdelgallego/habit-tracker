import requests

pixela_endpoint = 'https://pixela.io/v1/users'

user_params = {
  "token": "1q2w3e4r5t6",
  "username": "lmdelgallego",
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)
