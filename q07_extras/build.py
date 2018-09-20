# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    innings_1 ,innings_2 = 0, 0
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries1:
        for deli_num,delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    innings_1 +=delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    innings_1 += delivery_info['extras']['legbyes']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries2:
        for deli_num,delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    innings_2 += delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    innings_2 += delivery_info['extras']['legbyes']
    print('Total no in innings2: ',innings_2)
    print('Total no in innings1: ',innings_1)
    difference = innings_2 - innings_1
    return difference
extras_runs()


