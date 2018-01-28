# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extra_1 = []
    a = data['innings'][0]['1st innings']['deliveries']
    for deliveries in a:
        for ball in deliveries:
            E = deliveries[ball]['extras']
            extra_1.append(E.values)
            sum_extra_1 = int(sum(extra_1))
            #print extra_1
    extra_2 = []
    b = data['innings'][1]['2nd innings']['deliveries']
    for deliveries in a:
        for ball in deliveries:
            F = deliveries[ball]['extras']
            extra_2.append(F.values)
            sum_extra_2 = int(sum(extra_2))
    difference = sum_extra_2 - sum_extra_1


    return difference
