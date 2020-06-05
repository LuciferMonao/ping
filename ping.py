import time, datetime, pythonping, json, save_data
with open("data.txt", "r") as f: count = len(json.load(f))
while True:
    count += 1
    with open("data.txt", "r") as f: data = json.load(f)
    data[str(datetime.datetime.now())] = pythonping.ping('sz.de', size=256, count=1).rtt_avg_ms
    with open("data.txt", "w") as f: json.dump(data, f)
    time.sleep(4.9)
    print(count)
    if count > 10000: save_data.save(); time.sleep(3)