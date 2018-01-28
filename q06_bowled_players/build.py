# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]

    for i in data["innings"][1]["2nd innings"]["deliveries"]:

        for key in i:

             if "wicket" in i[key]:

                 if i[key]["wicket"]["kind"] == "bowled":

                     bowled_players.append(i[key]["batsman"])



    return bowled_players
