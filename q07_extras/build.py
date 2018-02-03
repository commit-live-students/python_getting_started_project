# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1stInn = []
    extras_2ndInn = []
    #for extra in
    for delivery  in data['innings'][0]['1st innings']['deliveries'] :
        if 'extras' in delivery.values()[0].keys():
            extras_1stInn.append(delivery.values()[0]['extras'])
    for delivery in data['innings'][1]['2nd innings']['deliveries']:
        if 'extras' in delivery.values()[0].keys():
            extras_2ndInn.append(delivery.values()[0]['extras'])
    #print extras_1stInn
    #print extras_2ndInn
    total_extra_1st = len(extras_1stInn)
    total_extra_2nd = len(extras_2ndInn)
    difference = total_extra_2nd - total_extra_1st

    return difference
print extras_runs(data)
