# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here


    Innings1Extra,Innings2Extra=0,0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings1Extra=Innings1Extra+delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                    Innings1Extra=Innings1Extra+delivery_info['extras']['legbyes']

    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if 'extras' in delivery_info:
                if 'wides' in delivery_info['extras']:
                    Innings2Extra=Innings2Extra+delivery_info['extras']['wides']
                elif 'legbyes' in delivery_info['extras']:
                     Innings2Extra=Innings2Extra+delivery_info['extras']['legbyes']


    difference =Innings2Extra-Innings1Extra

    return difference
