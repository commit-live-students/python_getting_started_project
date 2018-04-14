# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_1 = []
    extras_2 = []
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        for ball in delivery:
            if delivery[ball]['runs']['extras'] > 0:
                extras_1.append( delivery[ball]['runs']['extras'] )
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for ball in delivery:
            if delivery[ball]['runs']['extras'] > 0:
                extras_2.append( delivery[ball]['runs']['extras'] )
    
    list_extras_1 = []
    list_extras_2 = []
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        for ball in delivery:
            if 'extras' in delivery[ball]:
#                 print(delivery[ball]['extras'])
                list_extras_1.append(delivery[ball]['extras'])
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        for ball in delivery:
            if 'extras' in delivery[ball]:
#                 print(delivery[ball]['extras'])
                list_extras_2.append(delivery[ball]['extras'])
                
    # Write your code here
    # extras_1 = extra_runs_in_an_innings(data['innings'][0]['1st innings'])
    # extras_2 = extra_runs_in_an_innings(data['innings'][1]['2nd innings'])
    difference = len(list_extras_2) - len(list_extras_1)
    return difference
extras = extras_runs(data)

extras



