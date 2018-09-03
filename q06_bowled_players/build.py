from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data1=data['innings'][1]['2nd innings']['deliveries']

def bowled_out(data=data):
    bowled_players=[]
    for x in data1:
        for k,v in x.items():
            for p,q in v.items():
                if p =='wicket':
                    for u,v in q.items():
                        if u=='kind' and v=='bowled':
                            bowled_players.append(q['player_out'])                
    return bowled_players


