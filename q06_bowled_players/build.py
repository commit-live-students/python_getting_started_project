# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


bowled_players = []

#deliveries = data['innings'][1]['2nd innings']['deliveries']
#print (deliveries)

# Your Solution
def bowled_out(data=data):
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    #print (deliveries)
    for delivery in deliveries:
        for deliver_key, deliver_val in delivery.items():
            if 'wicket' in deliver_val:
                if deliver_val['wicket']['kind']=='bowled':
                    #count = 1
                    #wicket.append(count)
                    bowledbatsman = deliver_val['wicket']['player_out']
                    bowled_players.append(bowledbatsman)
    return (bowled_players)
