# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    
    # Write your code here
    first_innings_data = data['innings'][0]['1st innings']['deliveries']
    second_innings_data = data['innings'][1]['2nd innings']['deliveries']
    
    extra_first_innings = 0
    extra_second_innings = 0
    # Extras scored in first innings
    for bowls in first_innings_data:
        for exruns in bowls:
            if bowls[exruns]['runs']['extras'] != 0:
                extra_first_innings += 1
            else:
                pass
    
    # Extras scored in second innings 
    for bowls in second_innings_data:
        for exruns in bowls:
            if bowls[exruns]['runs']['extras'] != 0:
                extra_second_innings += 1
            else:
                pass

        
    difference = abs(extra_second_innings - extra_first_innings)
    return difference

   
extras_runs(data)
r1 = data['innings'][0]['1st innings']['deliveries']
for d in r1:
 
        for read_inside in d:

            # if d[read_inside]['runs']['extras'] != 0:
            print d[read_inside]['runs'], d[read_inside]['runs']['extras']

