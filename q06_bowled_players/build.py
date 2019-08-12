from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def bowled_out(data=data):
            subset_data= data['innings'][1]['2nd innings']['deliveries']
            bowled_out_players=[]
            for i in subset_data:
                        if i.values()[0].get('wicket') != None:
                                    if i.values()[0]['wicket']['kind']=='bowled':
                                                bowled_out_players.append(i.values()[0]['wicket']['player_out'])
            return bowled_out_players
bowled_out(data)
