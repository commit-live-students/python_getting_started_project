# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    #count = 0
    names = []
    
    for i in deliveries:   
        for key in i:
            #print(i[key])
            if('wicket' in i[key]):
               if(i[key]['wicket']['kind']=='bowled'):
                    #print(i)
                #count+=1
                    names.append(i[key]['wicket']['player_out'])
    return names
    
bowled_out(data)



