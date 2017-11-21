# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players=[]
    for j in range(0,2):
        item = data['innings'][j][data['innings'][j].keys()[0]]['deliveries']
        for i in range(0,len(item)):
            if(len(item[i][item[i].keys()[0]].keys())==5 and item[i][item[i].keys()[0]].keys()[4]=='wicket'):
                if(item[i][item[i].keys()[0]][item[i][item[i].keys()[0]].keys()[4]][item[i][item[i].keys()[0]][item[i][item[i].keys()[0]].keys()[4]].keys()[0]]=='bowled'):
                    bowled_players.append(item[i][item[i].keys()[0]][item[i][item[i].keys()[0]].keys()[4]][item[i][item[i].keys()[0]][item[i][item[i].keys()[0]].keys()[4]].keys()[1]])






    return bowled_players
