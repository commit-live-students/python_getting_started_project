from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    x=data['innings'][1]['2nd innings']['deliveries']
    for a in x:
        for i in a:
            if 'wicket' in a[i]:
                if a[i]['wicket']['kind'] == 'bowled':
                    bowled_players.append(a[i]['wicket']['player_out'])

    return bowled_players
