# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
import math
# Your Solution
def extras_runs(data=data):

    # Write your code here
    run_first_innings = 0
    run_second_innings = 0
    
    r1 = data['innings'][0]['1st innings']['deliveries']
    for d in r1: 
        for read_inside in d:
            if d[read_inside]['runs']['extras'] != 0:
                run_first_innings += 1 #d[read_inside]['runs']['extras']
            else:
                pass
            
    
    
    
    r2 = data['innings'][1]['2nd innings']['deliveries']
    for d in r2: 
        for read_inside in d:
            if d[read_inside]['runs']['extras'] != 0:
                run_second_innings += 1 #d[read_inside]['runs']['extras']
            else:
                pass
            
    difference = abs(run_second_innings - run_first_innings) 
            
    return difference

extras_runs()



