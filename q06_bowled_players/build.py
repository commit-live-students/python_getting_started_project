from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data["innings"][0]["1st innings"]["deliveries"]
    all_deliveries = deliveries +  data["innings"][1]["2nd innings"]["deliveries"]
    for delivery in all_deliveries:
        for d, delivery_info in delivery.items():
            if "wicket" in delivery_info:
                if delivery_info["wicket"]["kind"] == "bowled":
                        bowled_players.append(delivery_info["wicket"]["player_out"])
            else:
                break
    # Write your code here

    return bowled_players
