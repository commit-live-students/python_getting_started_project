# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    inn = data["innings"][1]["2nd innings"]["deliveries"]
    bowled_players=[]
    for i in range (0,len(inn)):
        delv = inn[i]
        if delv[delv.keys()[0]].get('wicket',None) != None:
            wicket = delv[delv.keys()[0]].get('wicket')
            if wicket.get('kind') == 'bowled':
                bowled_players.append(delv[delv.keys()[0]]['batsman'])


    return bowled_players
