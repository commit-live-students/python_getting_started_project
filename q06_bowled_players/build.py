# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    bowled_players=[]
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            wicket_exist=delivery_info.get('wicket',0)
            if wicket_exist !=0:
                if delivery_info['wicket']['kind']== 'bowled':
                    bowled_players.append(delivery_info['wicket']['player_out'])


    return bowled_players
