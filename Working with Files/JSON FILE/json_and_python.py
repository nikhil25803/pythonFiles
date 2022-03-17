
import json
# from unicodedata import name
import requests
import csv
from users import user_list
# from data_list import user_data_list

user_data_list = []

for user in  user_list:
    URL = "https://api.github.com/users/"+user
    r = requests.get(url = URL)
    data = r.json()
    json_write = json.dumps(data, indent=4)
    with open(f"json_files/{user}.json", "w") as f:
        # data =json.load(f)
        print(data["name"])

    li=[]

    name_id = data['name']
    userlogin = data["login"]
    userid = data["id"]
    repocount = data["public_repos"]
    follow = data["followers"]
    following_user = data["following"]

    li.append(name_id)
    li.append(userlogin)
    li.append(userid)
    li.append(repocount)
    li.append(follow)
    li.append(following_user)

    user_data_list.append(li)


# print(user_data_list)

file_name  = "data.csv"

with open(file_name, 'w') as csv_file:

    csv_writer = csv.writer(csv_file)

    csv_writer.writerows(user_data_list)


