from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    lst=[]
    deliveries = data['innings'][1]['2nd innings']['deliveries']

    for j in deliveries:
        for key,value in j.items():
            if 'wicket' in value.keys():
                if value['wicket']['kind'] == 'bowled':
                    lst.append(value['wicket']['player_out'])


    bowled_players = lst
    return bowled_players
