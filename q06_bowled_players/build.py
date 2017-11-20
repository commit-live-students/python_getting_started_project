# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    deliveries_list=data["innings"][1]["2nd innings"]["deliveries"]
    for target_list in deliveries_list:
            for overs in target_list:
                 default = None
                 val = target_list[overs].get('wicket', default)
                 if val!=None:
                     wicket_type='bowled'
                     if wicket_type==target_list[overs]["wicket"]["kind"]:

                         bowled_players.append(target_list[overs]["batsman"])


    return bowled_players
