# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here


    difference = 0
    for i in range(len(data['innings'])):
        for x in (data['innings'][i]):
            for deli in (data['innings'][i][x]['deliveries']):
                for ball in deli:
                    if 'extras' in deli[ball]:
                        if (i%2 == 0):
                            difference += 1
                        else:
                            difference -= 1
    return abs(difference)


difference
data['innings'][0]['1st innings']['deliveries'][0][0.1]['extras']        
for i in range(len(data['innings'])):
        for x in (data['innings'][i]):
            for deli in (data['innings'][i][x]['deliveries']):
                for ball in deli:
                    if 'extras' in deli[ball]:
                        if (i%2 == 0):
                            difference += 1
                        else:
                            difference -= 1

difference


