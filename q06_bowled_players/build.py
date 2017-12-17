# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    count = data['innings'][1]['2nd innings']['deliveries']
    bowled_players = []
    for i in count:
        sub_list=i.values()
        if 'wicket' in sub_list[0]:
            if sub_list[0]['wicket']['kind'] == 'bowled':
                bowled_players.append(sub_list[0]['batsman'])

    return bowled_players

bowled_players=bowled_out(data)
