# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

import math

# Your Solution
def extras_runs(data=data):
    extra_1 = []
    a = data['innings'][0]['1st innings']['deliveries']
    for deliveries in a:
        for ball in deliveries:

            #E = deliveries[ball]['runs']['extras']
            if deliveries[ball]['runs']['extras'] != 0:
                extra_1.append(deliveries[ball]['runs']['extras'])
        #sum_extra_1 = len(extra_1)
    #print extra_1


            #print extra_1
    extra_2 = []
    b = data['innings'][1]['2nd innings']['deliveries']
    for deliveries in b:
        for ball in deliveries:
            #F = deliveries[ball]['runs']['extras']
            if deliveries[ball]['runs']['extras'] != 0:
                extra_2.append(deliveries[ball]['runs']['extras'])
        #sum_extra_2 = len(extra_2)
    #print extra_2
    difference = len(extra_2) - len(extra_1)


    return difference

print extras_runs()
