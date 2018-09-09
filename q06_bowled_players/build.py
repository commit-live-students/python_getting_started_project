from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def bowled_out(data=data):
    bowled_players = []
    d = list(data['innings'][1]['2nd innings']['deliveries'])
    for index, value in enumerate(d):
        for key in value:
            try:
                if value[key]['wicket']['kind'] == 'bowled':
                      bowled_players.append(value[key]['wicket']['player_out'])
            
            except:
                   continue
            
            
    


    return bowled_players








