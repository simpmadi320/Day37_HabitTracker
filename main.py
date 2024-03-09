import requests
from datetime import datetime

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

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Pokemon Km Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

DATE = datetime.now().strftime("%Y%m%d")

add_points = {
    "date": DATE,
    "quantity": "1.0"
}


#response = requests.post(url=add_endpoint, json=add_points, headers=headers)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

new_pixel_data = {
    "quantity": "4.5"
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)