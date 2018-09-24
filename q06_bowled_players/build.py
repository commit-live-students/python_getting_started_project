
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def bowled_out (data=data):
    # Initialize the variable
    bowled_players =[]
    runs = 0
    runs_scored = 0
    # Read list value for deliveries
    deliveries_info = data['innings'][1]['2nd innings']['deliveries']
    for i in range (len(deliveries_info)):
        for key, value in (data['innings'][1]['2nd innings']['deliveries'][i]).items():
            batsman_name = value['batsman']
            if ('wicket' in data['innings'][1]['2nd innings']['deliveries'][i][key].keys()):
                wicket_kind = value ['wicket']
                for key, value in wicket_kind.items():
                    if (value == 'bowled'):
                        bowled_players.append(batsman_name)  
    return bowled_players









