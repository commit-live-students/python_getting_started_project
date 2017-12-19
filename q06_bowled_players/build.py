from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
deliveries =  data['innings'][1]['2nd innings']['deliveries']
bowled_players = list()
def bowled_out(data=data):
    for balls in deliveries:
        inter = balls.values()[0]
        for i in inter:
            if i == 'wicket':
                if inter['wicket']['kind'] == 'bowled':
                    trial = inter['wicket']['player_out']
                    bowled_players[:0]=[trial]
    bowled_players.sort()
    return bowled_players
