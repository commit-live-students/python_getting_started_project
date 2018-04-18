# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    del_list = []
    del_list = data['innings'][0]['1st innings']['deliveries']
    count = 0
    del_dict = {}
    for i in del_list:
        del_dict = i
        for key, value in del_dict.items():
            if(value['batsman'] == 'RT Ponting'):
                count += 1
    return count


