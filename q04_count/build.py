# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    key_list=[]
    abc=[]
    for i in range(0,124,1):
        abc=[]
        abc =list(data['innings'][0]['1st innings']['deliveries'][i].keys())
        key_list.append(abc[0])
    
    for i in range(0,124,1):
        if(str(data['innings'][0]['1st innings']['deliveries'][i][key_list[i]]['batsman'])=='RT Ponting'):
            count+=1

    return count


