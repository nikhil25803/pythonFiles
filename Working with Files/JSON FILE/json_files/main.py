user_list = ["Algo-Phantoms","TesseractCoding", "vinitshahdeo","avinashkranjan","flow2ml" ,"ashishsahu1" ,"girlscript" ,"praveenscience", "mindsdb", "ProjectSakura", "Spectrum-CETB", "HITK-TECH-Community", "CircuitVerse", "mishraaditya595","PyAr", "boostorg", "sympy", "vinta", "TheAlgorithms", "kamranahmedse", "30-seconds"]

# print(len(user_list))

import json
import csv

user_data_list = []


for user in user_list:

    with open(f"{user}.json") as file:

        data = json.load(file)

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
