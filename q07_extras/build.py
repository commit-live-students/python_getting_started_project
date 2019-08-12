# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    subset_data_1= data['innings'][0]['1st innings']['deliveries']
    extras_1=[]
    for i in subset_data_1:
        if i.values()[0].get('runs') != None:
            if i.values()[0]['runs']['extras'] <> 0:
                extras_1.append(i.values()[0]['runs']['extras'])
                subset_data_2= data['innings'][1]['2nd innings']['deliveries']
                extras_2=[]
    for i in subset_data_2:
        if i.values()[0].get('runs') != None:
            if i.values()[0]['runs']['extras'] <> 0:
                extras_2.append(i.values()[0]['runs']['extras'])
                difference = len(extras_2)-len(extras_1)
    return difference
