# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    list1=[]
    list2=[]
    for dict in data['innings'][0]['1st innings']['deliveries']:
        for delivery_dict in dict.values():
            if 'extras' in delivery_dict:
                list1.append(delivery_dict['runs']['extras'])
                
    list2=[delivery_dict['runs']['extras'] for dict in data['innings'][1]['2nd innings']['deliveries'] for delivery_dict in dict.values() if 'extras' in delivery_dict]                   


    difference =len(list2)-len(list1)


    return difference

data
print(extras_runs(data))


