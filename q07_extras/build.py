# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras1=0
    extras2=0
    for dict4 in data['innings'][0]['1st innings']['deliveries']:
        for k,v in dict4.items():
            if 'extras' in v:
                extras1+=1
            
    for dict5 in data['innings'][1]['2nd innings']['deliveries']:
        for k,v in dict5.items():
            if 'extras' in v:
                extras2+=1
            
    difference=extras2-extras1


    return difference
extras_runs()






