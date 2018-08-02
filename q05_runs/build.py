# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
runs = 0

# Your Solution
def BC_runs(data):
    runs = 0
    dely=data['innings'][0]['1st innings']['deliveries']
    for key in dely:
        for key,value in key.items():
            for key1,value1 in value.items():
                if (key1 == 'batsman')& (value1=='BB McCullum'):
                    for key2, value2 in value.items():
                        if key2 == 'runs':
                            for key3, value3 in value2.items():
                                if key3 == 'batsman':
                                    runs = runs + value3
                                    
        
    # Write your code here


    return(runs)

BC_runs(data)

                
            


