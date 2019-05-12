# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    data1=data['innings'][0]['1st innings']['deliveries']
    for i in data1:
        temp1=str(i.keys())
        temp=temp1[11:14]
        if (float(temp)>=10.0):
            temp=temp1[11:15]
        if 'RT Ponting' in i[float(temp)]['batsman']:
            count=count+1
    return count


