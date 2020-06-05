import matplotlib.pyplot as plt, json, datetime as datetime, statistics

def show(QUALITY=95, DIFFERENCE=2, SIZE=300):
    with open("data.txt", "r") as f:
        data = json.load(f)

    median_y_values = []
    average_y_values = []
    x_values = []

    data = [data[key] for key in data]

    if __name__ == "__main__":
        AUTOMATICALLY = False
    else:
        AUTOMATICALLY = True


    for STEP in range(1, len(data)):
        if len(data) / STEP < SIZE:
            break

    for num in range(1, len(data) - 1, STEP):
        median_y_values.append(statistics.median(data[num:num+STEP]))
        if sum(data[num:num+STEP]) / STEP > (statistics.median(data[num:num+STEP]) + DIFFERENCE):
            average_y_values.append(sum(data[num:num+STEP]) / STEP)
        else:
            average_y_values.append(0)
        x_values.append(len(x_values))


    plt.plot(x_values, average_y_values, "or", label="Average ping", linewidth=0.3)
    plt.plot(x_values, median_y_values, "-k", label="Median ping.", linewidth=3)
    plt.xlim(0, SIZE)
    plt.ylim(30, 120)
    plt.xlabel("Ping")
    plt.ylabel("Time in ms.")
    plt.title("Ping graph.")

    plt.savefig(f"graphs/time: {str(datetime.datetime.now())}, size = {str(SIZE)}, difference = {str(DIFFERENCE)}, quality = {str(QUALITY)}, automatically = {str(AUTOMATICALLY)}.jpg", dpi=500, quality=QUALITY)


show()