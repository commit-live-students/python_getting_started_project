from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for key, val in delivery.items():
            for x,y in val.items():
                if x == 'wicket' and y['kind']=='bowled':
                    player = y['player_out']
                    bowled_players.append(player)
    return bowled_players

print bowled_out()
