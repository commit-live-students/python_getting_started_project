# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    number_of_bowl = len(data['innings'][0]['1st innings']['deliveries']) #no of ball in 1st innings
    runs = 0 #to count the number of runs scored by Brendon maCcullum
    
    for ball_no in range(number_of_bowl): #loop over each ball
    
        #return dictionary of particular ball no
        di = data['innings'][0]['1st innings']['deliveries'][ball_no]
        
        for ke  in di.keys():
            if data['innings'][0]['1st innings']['deliveries'][ball_no][ke]['batsman'] == 'BB McCullum':
                
                runs = runs + data['innings'][0]['1st innings']['deliveries'][ball_no][ke]['runs']['batsman']
            

    return(runs)

BC_runs(data)


