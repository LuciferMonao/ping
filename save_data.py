import json, datetime

def save():
    with open("data.txt", "r+") as f:
        data = json.load(f)
        json.dump({"000-00-00 00:00:00.000000": 42.00},f)
    
    with open(f"data/{str(datetime.datetime.now())}.txt", "w") as f:
        json.dump(data, f)