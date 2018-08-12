# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries1:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info.has_key('wicket'):
                if delivery[delivery_number]['wicket']['kind']=='bowled':
                    bowled_players.append(delivery_info['batsman'])
    for delivery in deliveries2:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info.has_key('wicket'):
                if delivery[delivery_number]['wicket']['kind']=='bowled':
                    bowled_players.append(delivery_info['batsman'])

    return bowled_players
