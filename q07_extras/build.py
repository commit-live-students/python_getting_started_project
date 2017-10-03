from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    f_extra = 0
    s_extra = 0
    f_deliveries = data["innings"][0]["1st innings"]["deliveries"]
    s_deliveries = data["innings"][1]["2nd innings"]["deliveries"]
    for delivery in f_deliveries:
        for d, delivery_info in delivery.items():
            if "extras" in delivery_info:
                f_extra +=  1

    for delivery in s_deliveries:
        for d, delivery_info in delivery.items():
            if "extras" in delivery_info:
                s_extra += 1
    difference = s_extra - f_extra
    return difference
