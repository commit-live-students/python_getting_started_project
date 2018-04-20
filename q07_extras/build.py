# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    difference = 0
    extras_1 = 0
    extras_2 = 0

    deliveries_1 =[]
    deliveries_1 = data['innings'][0]['1st innings']['deliveries']
    for delivery_1 in deliveries_1:
        for dele in delivery_1.values():
                if ( dele.get('extras') != None):
                    extras_1 = extras_1 + 1

#                 extras_1 = extras_1 + dele['runs']['extras']
# print(ex) 
                
    deliveries_2 = []
    deliveries_2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery_2 in deliveries_2:
        for dele in delivery_2.values():
                if ( dele.get('extras') != None):
                    extras_2 = extras_2 + 1

#                 extras_2 = extras_2 + dele['runs']['extras']
#         #     difference =   

    difference = extras_2 - extras_1
    return difference

extras_runs(data)

