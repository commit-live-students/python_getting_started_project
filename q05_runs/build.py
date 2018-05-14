# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    inf=data['innings']
    for i in inf:
        for k,v in i.items():
            for delivery in v['deliveries']:
                for a,b in delivery.items():
                    if b['batsman']=='BB McCullum':
                       runs+=b['runs']['batsman']
                                
                            
                            
                                
                    
                    

    
    

    # Write your code here


    return(runs)



