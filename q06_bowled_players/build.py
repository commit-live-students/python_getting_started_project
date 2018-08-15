# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players=[]
    innings=data['innings']
    second=innings[1]
    final_inning_list=second['2nd innings']['deliveries']
    for x in final_inning_list:
        for key,value in x.items():
            for k,v in value.items():
                #print('key',k,'value',v)
                if(k=='wicket' and v['kind']=='bowled'):
                                    bowled_players.append(v['player_out'])
                        
                            

    # Write your code here


    return bowled_players

bowled_out()



