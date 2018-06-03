# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    extras2 = 0
    for ball in range (len(data['innings'][1]['2nd innings']['deliveries'])):
            ball_number = list(data['innings'][1]['2nd innings']['deliveries'][ball].keys())[0]
            if 'extras' in (data['innings'][1]['2nd innings']['deliveries'][ball][ball_number].keys()):
                extras2 = extras2 + 1

    
    extras1 = 0
    for ball in range (len(data['innings'][0]['1st innings']['deliveries'])):
            ball_number = list(data['innings'][0]['1st innings']['deliveries'][ball].keys())[0]
            if 'extras' in (data['innings'][0]['1st innings']['deliveries'][ball][ball_number].keys()):
                extras1 = extras1 + 1
    

    difference = extras2 - extras1


    return difference








