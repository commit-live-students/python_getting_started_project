# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    Innings_1  , Innings_2 = 0 , 0
    deliveries1 = data ['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries1:
        for deli_num, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings_1 += delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    Innings_1 += delivery_info['extras']['legbyes']
                
    deliveries2 = data ['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries2:
        for deli_num, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings_2 += delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    Innings_2 += delivery_info['extras']['legbyes']


  #  print('Total no in innings_2: ',Innings_2)
   # print('Total no in innings_1: ',Innings_1)
    difference = Innings_2 - Innings_1
    return difference
extras_runs()



