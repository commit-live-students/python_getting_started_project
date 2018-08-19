# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data):

    extra1 = 0
    extra2 = 0
    one_inning=data['innings'][0]['1st innings']['deliveries']
    for key in one_inning:
        for key1,value1 in key.items():
            for key2,value2 in value1.items():
                if key2== 'extras':
                    for key3, value3 in value2.items():
                        extra1 = extra1 + 1
                        #print(extra1)
#                 extra1 = extra1 + value2['extras']
    
    two_inning = data['innings'][1]['2nd innings']['deliveries']
    for key in two_inning:
        for key1,value1 in key.items():
            for key2,value2 in value1.items():
                if key2== 'extras':
                     for key3, value3 in value2.items():
                            extra2 = extra2 + 1
#                             print(extra2)


    difference = extra1 - extra2
    if difference < 0:
        difference = difference* -1
    #print(extra1)
    #print(extra2)
    #print(difference)
    return difference

extras_runs(data)


