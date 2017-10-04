# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def extras_runs(data=data):
    count1=0
    count2=0
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']

    for j in deliveries1:
        for key,value in j.items():
                if value['runs']['extras']>0:
                    count1 = count1 +1


    for l in deliveries2:
        for key,value in l.items():
                if value['runs']['extras']>0:
                    count2 = count2 +1




    difference = count2-count1
    return difference
