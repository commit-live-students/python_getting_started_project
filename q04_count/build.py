# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def deliveries_count(data=data):
    # Your code here
    count = 0
    deliveries_faced = data['innings'][0]['1st innings']['deliveries']
    for ele in deliveries_faced:
        for key, value in ele.items():
            batsman_name = value['batsman']
            print (batsman_name)
            if (batsman_name == 'RT Ponting'):
                count = count+1
    return count

deliveries_count(data)





