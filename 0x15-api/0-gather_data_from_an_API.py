#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys
import requests
import sys

# import requests

# import urllib.request

# Rest of your code goes here
# Make a GET request to a URL
# response = requests.get('https://api.example.com')

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Print the response content
#     print(response.text)
# else:
#     print('Request failed with status code:', response.status_code)
    
if __name__ == "__main__":


    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0
    
    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1
    
    print("Employee {} is done with tasks({}/{}):".format(name,completed, totalTasks ))
    for task in todos.json():
        if task.get('userId') == int(userId) and task.get('completed'):
            print("\t" + task.get('title'))
