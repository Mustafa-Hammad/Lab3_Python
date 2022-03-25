import glob
import json
import os
import re

# as create file
# class Project:
#
#     # Create Project
#     def createProject(userId, title, details, totalTarget, startDate, endDate):
#         newProjectDocument = [{
#             'email': userId,
#             'title': title,
#             'details': details,
#             'total': totalTarget,
#             'startDate': startDate,
#             'endDate': endDate
#         }]
#         regex = '^[1-31]+[/]+[1-12]+[/]+[2022-2027]$'
#         if glob.glob(f"./all/{title}.json"):
#             print("Already exist")
#             return 0
#         elif (re.search(regex, startDate)) and (re.search(regex, endDate)):
#                 with open(f'./all/{title}.json', 'w') as f:
#                     print("The json file is created")
#                     json.dump(newProjectDocument, f, indent=2)
#                     return 1
#         else:
#             print("Wrong Data Formate")
#             return 0
#
#
#     # View All Project
#     def findAllProject(userId):
#         for file in glob.glob("./all/*.json"):
#
#             with open(file, 'r') as file1:
#                 data = json.load(file1)
#             for lindex in range(len(data)):
#                 m = data[lindex]["email"]
#                 t = data[lindex]["title"]
#                 d = data[lindex]["details"]
#                 o = data[lindex]["total"]
#                 s = data[lindex]["startDate"]
#                 e = data[lindex]["endDate"]
#             projectDictionry = {
#
#                 'owner': m,
#                 'title': t,
#                 'details': d,
#                 'total': o,
#                 'startDate': s,
#                 'endDate': e
#             }
#             print(projectDictionry)
#
#         # View All Project
#
#     def findstartProject(userId,date):
#         for file in glob.glob("./all/*.json"):
#
#             with open(file, 'r') as file1:
#                 data = json.load(file1)
#             for lindex in range(len(data)):
#                 m = data[lindex]["email"]
#                 t = data[lindex]["title"]
#                 d = data[lindex]["details"]
#                 o = data[lindex]["total"]
#                 s = data[lindex]["startDate"]
#                 e = data[lindex]["endDate"]
#                 if re.match(date, s):
#                     projectDictionry = {
#
#                         'owner': m,
#                         'title': t,
#                         'details': d,
#                         'total': o,
#                         'startDate': s,
#                         'endDate': e
#                     }
#                     print(projectDictionry)
#
#     def findendProject(userId, date):
#         for file in glob.glob("./all/*.json"):
#
#             with open(file, 'r') as file1:
#                 data = json.load(file1)
#             for lindex in range(len(data)):
#                 m = data[lindex]["email"]
#                 t = data[lindex]["title"]
#                 d = data[lindex]["details"]
#                 o = data[lindex]["total"]
#                 s = data[lindex]["startDate"]
#                 e = data[lindex]["endDate"]
#                 if re.match(date, e):
#                     projectDictionry = {
#
#                         'owner': m,
#                         'title': t,
#                         'details': d,
#                         'total': o,
#                         'startDate': s,
#                         'endDate': e
#                     }
#                     print(projectDictionry)
#
#
#     # Update Project For One User
#     def update(userId, title):
#         regex = '^[1-31]+[/]+[1-12]+[/]+[2022-2027]$'
#         file = f'./all/{title}.json'
#         with open(file, "r") as jsonFile:
#             data = json.load(jsonFile)
#         for lindex in range(len(data)):
#             m = data[lindex]["email"]
#             t = data[lindex]["title"]
#             if re.match(userId, m) and re.match(title, t):
#                 txt = input("What do you want to change? ")
#                 if re.match(txt, "title"):
#                     print("Can't update the title")
#                     return 0
#                 txt2 = input("Enter the new value ")
#                 if re.match(txt, "startDate") or re.match(txt, "endDate"):
#                     if re.search(regex, txt2):
#                         data[lindex][txt] = txt2
#                         with open(file, "w") as jsonFile:
#                             json.dump(data, jsonFile)
#                             return True
#                     else:
#                         print("Wrong formula")
#                         return False
#                 else:
#                     data[lindex][txt] = txt2
#                     with open(file, "w") as jsonFile:
#                         json.dump(data, jsonFile)
#                         return True
#             else:
#                 print("Not Exist !!")
#                 return 0
#
#
#     # Delete One Project For One User
#     def deleteOneProject(userID, title):
#         filename = f'./all/{title}.json'
#         print(filename)
#         with open(filename, 'r') as file:
#             data = json.load(file)
#         for lindex in range(len(data)):
#             m = data[lindex]["email"]
#             t = data[lindex]["title"]
#             if re.match(userID, m) and re.match(title, t):
#                 os.remove(filename)
#                 return True
#             else:
#                 print("Not Exist !!")
#                 return False


# as edite in the same file
class Project:

    # Create Project
    def createProject(userId, title, details, totalTarget, startDate, endDate):
        newProjectDocument = ({
            'email': userId,
            'title': title,
            'details': details,
            'total': totalTarget,
            'startDate': startDate,
            'endDate': endDate
        })
        with open('./all/a.json', 'r') as f:
            data = json.load(f)
        print(type(data))
        data.append(newProjectDocument)
        with open('./all/a.json', "w") as jsonFile:
            json.dump(data, jsonFile)
            return 1



    # View All Project
    def findAllProject(userId):
        filename = "./all/a.json"
        with open(filename, 'r') as file:
            data = json.load(file)
        for i in range(len(data)):

            print(f"""
            
            Project No.{i + 1}""")
            for j in data[i]:
                print(f"{j}:", data[i][j])

        print("")


    def findstartProject(userId,date):
        for file in glob.glob("./all/a.json"):

            with open(file, 'r') as file1:
                data = json.load(file1)
            for lindex in range(len(data)):

                s = data[lindex]["startDate"]

                if re.match(date, s):
                    print(f"""

                               Project No.{lindex + 1}""")
                    for j in data[lindex]:
                        print(f"{j}:", data[lindex][j])

    def findendProject(userId, date):
        for file in glob.glob("./all/a.json"):

            with open(file, 'r') as file1:
                data = json.load(file1)
            for lindex in range(len(data)):
                e = data[lindex]["endDate"]
                if re.match(date, e):
                    print(f"""

                                                   Project No.{lindex + 1}""")
                    for j in data[lindex]:
                        print(f"{j}:", data[lindex][j])


    # Update Project For One User
    def update(userId, title):
        regex = '^[1-31]+[/]+[1-12]+[/]+[2022-2027]$'
        file = './all/a.json'
        with open(file, "r") as jsonFile:
            data = json.load(jsonFile)
        for lindex in range(len(data)):
            m = data[lindex]["email"]
            t = data[lindex]["title"]
            if re.match(userId, m) and re.match(title, t):
                txt = input("What do you want to change? ")
                txt2 = input("Enter the new value ")
                if re.match(txt, "startDate") or re.match(txt, "endDate"):
                    if re.search(regex, txt2):
                        data[lindex][txt] = txt2
                        with open(file, "w") as jsonFile:
                            json.dump(data, jsonFile)
                            return True
                    else:
                        print("Wrong formula")
                        return False
                else:
                    data[lindex][txt] = txt2
                    with open(file, "w") as jsonFile:
                        json.dump(data, jsonFile)
                        return True
            else:
                print("Not Exist !!")
                return 0


    # Delete One Project For One User
    def deleteOneProject(userID, title):
        filename = './all/a.json'
        print(filename)
        with open(filename, 'r') as file:
            data = json.load(file)
        for lindex in range(len(data)):
            m = data[lindex]["email"]
            t = data[lindex]["title"]
            print(t)
            print(m)
            print(title)
            print(userID)
            if re.match(userID, m) and re.match(title, t):
                data.pop(lindex)
                with open('./all/a.json', 'w') as data_file:
                    json.dump(data, data_file)
                    return True

        print("Not Exist !!")
        return False
