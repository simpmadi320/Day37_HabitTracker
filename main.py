import requests

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN ="K7hLpRq2xZ"
USERNAME = "simpmadi320"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Pokemon Km Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)