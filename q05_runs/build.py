# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    first_innings = data['innings'][0].get('1st innings').get('deliveries')
    count = 0
    runs = 0
    for x in range(0,len(first_innings)):
        delivery = first_innings[x]
        for key in delivery:
            if delivery[key].get('batsman') == 'BB McCullum':
                runs = runs + delivery[key].get('runs').get('batsman')  
    return runs



