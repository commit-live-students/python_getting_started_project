# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    s_batsman = "BB McCullum"
    # stores the deliveries faced by the batsman
    i_count = 0
    i_runs_scored = 0
    innings_list = data["innings"]
    i = 0
    while True:
        if i >= 2:
            break
        elif i == 0:
            inning_details_lst = innings_list[0]["1st innings"]["deliveries"]
            i = i + 1
        else:
            inning_details_lst = innings_list[1]["2nd innings"]["deliveries"]
            i = i + 1

        # parse the inning_details
        for delivery_dtl in inning_details_lst:
            for delivery_value in delivery_dtl.itervalues():
                if delivery_value["batsman"] ==  s_batsman:
                    i_runs_scored = i_runs_scored + delivery_value["runs"]["batsman"]
                    i_count = i_count + 1
                    if  "wicket" in delivery_value:
                        # if given batsman is out on delivery then break
                        # assuming the deliveries are in sequence
                        break


    return i_runs_scored
