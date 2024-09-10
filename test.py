from typing import Optional
import requests
import json


# function to get data from api with url https://jsonplaceholder.typicode.com/todos/2
def get_data(url: str, id: int) -> Optional[dict]:
    response = requests.get(url + str(id))
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)


# function to post data to api with url https://jsonplaceholder.typicode.com/todos
def post_data(url: str, data: dict):
    response = requests.post(url, json=data)
    if response.status_code == 201:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)


# function to update data to api with url https://jsonplaceholder.typicode.com/todos/2
def update_data(url: str, id: int, data: dict):
    response = requests.put(url + str(id), json=data)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)


print(get_data("https://jsonplaceholder.typicode.com/todos/", 2))
print(
    post_data(
        "https://jsonplaceholder.typicode.com/todos",
        {"userId": 2, "title": "test", "completed": True},
    )
)
# print(update_data("https://jsonplaceholder.typicode.com/todos/2", {"completed": True}))
print(get_data("https://jsonplaceholder.typicode.com/todos/", 2))
