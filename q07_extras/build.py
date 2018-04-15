# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    d_1= data['innings'][0]['1st innings']['deliveries']
    d_2= data['innings'][1]['2nd innings']['deliveries']
    extras1=[]
    extras2=[]
    for d in d_1:
        extras1.extend([d[key]['extras'] for key in d.keys() if 'extras' in d[key].keys()])
                
                    
    for d in d_2:
        for key,value in d.items():
            if 'extras' in value.keys():
                extras2.append(value['extras'])


    difference = len(extras2)-len(extras1)
    return difference

extras_runs(data)


