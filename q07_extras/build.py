# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    deliveries = [x.values() for x in data['innings'][1]['2nd innings']['deliveries']]   
    inning1 =[int(list(z)[0]['runs']['extras']) for z in deliveries if int(list(z)[0]['runs']['extras'])
 !=0]
    deliveries1 = [x.values() for x in data['innings'][0]['1st innings']['deliveries']]   
    inning2 =[int(list(z)[0]['runs']['extras']) for z in deliveries1  if int(list(z)[0]['runs']['extras'])
 !=0]
    difference = len(inning1) - len(inning2)

    return difference

extras_runs()


