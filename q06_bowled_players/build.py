# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []

    deliveries = data['innings'][1]['2nd innings']['deliveries'] # deliveries is a list

    for delivery in deliveries: # delivery is a dictionary
        #print delivery
        #print type(delivery)
        for each in delivery:
            match_delivery = delivery[each]
            for match_each in match_delivery:
                #print match_delivery
                if match_each == 'wicket':
                    wickettype = match_delivery[match_each]
                    #print wickettype
                    #print type(wickettype)
                    for eachwt in wickettype:
                        if (eachwt == 'kind' and wickettype[eachwt] == 'bowled'):
                            #print match_delivery
                            bowled_players.append(match_delivery['batsman'])

    #print bowled_players
    return bowled_players

#bowled_out(data)
