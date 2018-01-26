# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    innings_list = data["innings"]

    inning_details_lst = innings_list[1]["2nd innings"]["deliveries"]

    # parse the inning_details
    # find the batsman bowled out in second innings
    for delivery_dtl in inning_details_lst:
        for delivery_value in delivery_dtl.itervalues():
            if  "wicket" in delivery_value:
                if delivery_value["wicket"]["kind"] == "bowled":
                    # if given batsman is out on delivery then break
                    # assuming the deliveries are in sequence
                    bowled_players.append(delivery_value["batsman"])

    return bowled_players
