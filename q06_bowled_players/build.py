# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    
    overs=name=data['innings'][1]['2nd innings']['deliveries']
    #print(overs)
    for i in range(len(overs)):
        for key in overs[i]:
            #print(overs[i][key])
            if 'wicket' in overs[i][key]:
                if 'kind' in overs[i][key]['wicket']:
                    if overs[i][key]['wicket']['kind']=='bowled':
                        bowled_players.append(overs[i][key]['wicket']['player_out'])

    return bowled_players

bowled_out(data)





