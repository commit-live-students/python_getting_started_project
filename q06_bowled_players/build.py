from greyatomlib.python_getting_started.q01_read_data.build import read_data
data1 = read_data()

bowled_players = []
def bowled_out(data):
    lst = data['innings'][1]['2nd innings']['deliveries']

    for d in lst:
        Balled = d.values()
        if 'wicket' in Balled[0]:
            if Balled[0]['wicket']['kind'] == 'bowled':
                bowled_players.append(Balled[0]['wicket']['player_out'])
    return bowled_players

bowled_out(data1)
