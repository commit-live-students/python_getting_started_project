# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    firstInningsExtras = 0
    secondInningsExtras = 0
    for balls in data['innings'][0]['1st innings']['deliveries']:
        #print(balls[list(balls.keys())[0]]['runs']['extras'])
        if 'extras' in balls[list(balls.keys())[0]]:
            firstInningsExtras += 1

    for balls in data['innings'][1]['2nd innings']['deliveries']:
        #print(balls[list(balls.keys())[0]]['runs']['extras'])
        if 'extras' in balls[list(balls.keys())[0]]:
            secondInningsExtras += 1

    
    difference = secondInningsExtras - firstInningsExtras


    return difference
extras_runs(data)

