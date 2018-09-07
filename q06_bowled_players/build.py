# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    
    


    return bowled_players

# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):

    # Write your code here
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    
    for delivery in deliveries:
        
        for key in delivery:
            
            run_variable = delivery[key]
            
            if 'wicket' in run_variable and run_variable['wicket']['kind'] == 'bowled':
                
                bowled_players.append(run_variable['batsman'])
    
    


    return bowled_players



