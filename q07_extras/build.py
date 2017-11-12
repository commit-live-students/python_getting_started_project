# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here


    difference = 0
    d = data['innings']
    for i in range(len(d)):
        for key in d[i]:
            for deliv in d[i][key]['deliveries']:
                if 'extras' in deliv.values()[0]:
                    if i % 2 == 0:
                        difference += 1
                    else:
                        difference -= 1
    return abs(difference)
