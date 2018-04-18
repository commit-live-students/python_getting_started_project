# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    
    del_list = []
    del_list2 = []
    del_list = data['innings'][0]['1st innings']['deliveries']
    del_list2 = data['innings'][1]['2nd innings']['deliveries']
    extras_1 = 0
    extras_2 = 0
    del_dict = {}
    del_dict2 = {}
    check_dict = {}
    for i in del_list:
        del_dict = i
        for key, value in del_dict.items():
                check_dict = value
                if('extras' in check_dict.keys()):
                    extras_1 += 1
            
    for i in del_list2:
        del_dict2 = i
        for key, value in del_dict2.items():
            check_dict = value
            if('extras' in check_dict.keys()):
                extras_2 += 1   
    
    difference = extras_2 - extras_1
    return abs(difference)



