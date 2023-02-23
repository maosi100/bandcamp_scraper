import json

def read_all():
    with open("database.json", "r") as outfile:
        json_object = json.load(outfile)
        return json_object

def oldest():
    with open("database.json", "r") as outfile:
        json_object = json.load(outfile)
        
        for item in json_object:
            if item[2] == "0":
                return item

def oldest_release():
    with open("database.json", "r") as outfile:
        json_object = json.load(outfile)
        
        for item in json_object:
            if item[2] == "0":
                item[2] = "1"
                return item[1]
