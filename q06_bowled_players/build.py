from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def bowled_out(data=data):
    bowled=''
    bowled_players=[]
    d=data['innings'][1]['2nd innings']['deliveries']
    for index,values in enumerate(d):
        for key,val in values.items():
            for key,v in val.items():
                if key=='wicket':
                    for key,va in v.items():
                        if key=='kind':
                            if va=='bowled':
                                bowled=v.get('player_out')
                                bowled_players.append(bowled)
                                                    
    return bowled_players                                                

