# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

bowled_out_var = []
wicket_type = 'bowled'
runs = 0


def get_for_both(innings):
    for item in innings:
        for k,v in item.items():
            new_val = item[k]
            if new_val.has_key('wicket'):
                if new_val['wicket']['kind'] == wicket_type:
                    bowled_out_var.append(new_val['wicket']['player_out'])

# Your Solution
def bowled_out(data=data):

    # Write your code here
    get_for_both(data['innings'][0]['1st innings']['deliveries'])
    get_for_both(data['innings'][1]['2nd innings']['deliveries'])
    bowled_players = bowled_out_var
    print bowled_players
    return bowled_players

bowled_out(data)
