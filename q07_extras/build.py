# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    difference = 0
    for i in range(len(data['innings'])):
        for key in data['innings'][i]:
            for delivery_number in data['innings'][i][key]['deliveries']:
                for num in delivery_number:
                    if 'extras' in delivery_number[num]:
                        if(i % 2 == 0):
                            difference +=1
                        else:
                            difference -= 1
    return abs(difference)



