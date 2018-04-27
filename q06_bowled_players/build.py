from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def bowled_out(data=data):
    bowled_players=[]
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for deli in deliveries:
        for key, value in deli.items():
            if 'wicket' in value:
                if(value['wicket']['kind']=='bowled'):
                    bowled_players.append(value['wicket']['player_out'])
    return bowled_players

bowled_out()

