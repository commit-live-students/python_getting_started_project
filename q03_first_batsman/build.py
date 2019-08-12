# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
    # Write your code here
def first_batsman(data=data):
    data1=data['innings'][0]['1st innings']['deliveries']
    #data2=data1['1st innings']['deliveries']
    data3=data1[0].items()
    for n in data3:
        return data3[0][1]['batsman']
    # Write your code here
first_batsman(data)



    #return name
