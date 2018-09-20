# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    innings1,innings2 = 0,0
    extra1 = data['innings'][0]['1st innings']['deliveries']
    for m in extra1:
        for x, y in m.items():
            if 'extras' in y:
                if 'wides' in y['extras']:
                    innings1 += y['extras']['wides']
                elif 'legbyes' in y['extras']:
                    innings1 += y['extras']['legbyes']
                    
    extra2 = data['innings'][1]['2nd innings']['deliveries']
    for m in extra2:
        for x, y in m.items():
            if 'extras' in y:
                if 'wides' in y['extras']:
                    innings2 += y['extras']['wides']
                elif 'legbyes' in y['extras']:
                    innings2 += y['extras']['legbyes']
    
    print(innings2)
    print(innings1)
    difference = innings2-innings1


    return difference
extras_runs()

