import json

def print_data():
    with open("static/data.json") as file:
        data = json.load(file);
    
    print(data)