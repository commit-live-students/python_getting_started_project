# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    innings = data ['innings'][1]
    second_innings = innings['2nd innings']
    deliveries = second_innings['deliveries']
    counter = 0
    for k in deliveries:
        for key, value in  k.iteritems():
            if 'wicket' in value:
                 if  value['wicket']['kind'] == 'bowled':
                        bowled_players.insert(counter, value['wicket']['player_out'])
                        counter += 1
    return bowled_players
print (bowled_out(data))
