#!/usr/bin/python3
""" export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    ID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?ID={}".
                        format(ID), verify=False).json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    json_file = {}
    json_file[ID] = tasks
    with open("{}.json".format(ID), 'w') as jsfile:
        json.dump(json_file, jsfile)
