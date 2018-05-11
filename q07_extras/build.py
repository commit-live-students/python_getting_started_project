# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extrasFirst = []
    extrasSecond = []
    # Write your code here
    deliveriesInFirst = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveriesInFirst:
        for ball in delivery.keys():
            extrasFirst.append(delivery[ball]['runs']['extras'])
    
    deliveriesInSecond = data['innings'][1]['2nd innings']['deliveries']
    for delivery2 in deliveriesInSecond:
        for ball2 in delivery2.keys():
            extrasSecond.append(delivery2[ball2]['runs']['extras'])
    
    ExtrasFirst = list(filter(lambda a: a!=0 ,extrasFirst))
    ExtrasSecond = list(filter(lambda a: a!=0 ,extrasSecond))
    difference = abs(len(ExtrasFirst) - len(ExtrasSecond))
    return difference



