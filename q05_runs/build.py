# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()
# Your Solution
def BC_runs(data=data):

    # Write your code here
    
    
    #initialize runs variable
    runs = 0
    
    #list of bales for first innings
    balls = data['innings'][0]['1st innings']['deliveries']

    #iterate through each ball
    for bal in balls:
        #iterate through each batsman in each ball and calcuting the runs 
        for batsmn in bal.values():
            if batsmn['batsman'] == 'BB McCullum':
                runs = runs + batsmn['runs']['batsman']

    return runs

if __name__  == '__main__':
    BC_runs()
    print(BC_runs())



