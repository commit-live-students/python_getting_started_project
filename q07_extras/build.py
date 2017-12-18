# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    extras1=[]
    extras2=[]
    deliveries1=data['innings'][0]['1st innings']['deliveries']
    deliveries2=data['innings'][1]['2nd innings']['deliveries']
    for balls1 in deliveries1:
        if 'extras' in  balls1.values()[0].keys():
            extras= balls1.values()[0]['extras'].values()[0]
            extras1.append(extras)


    for balls2 in deliveries2:
        if 'extras' in  balls2.values()[0].keys():
            extras= balls2.values()[0]['extras'].values()[0]
            extras2.append(extras)

        difference=len(extras2)-len(extras1)



    return difference
