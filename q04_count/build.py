# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    total_del_1st_innings=len(data['innings'][0]['1st innings']['deliveries'])
    lst=data['innings'][0]['1st innings']['deliveries']
    for i in range(total_del_1st_innings):
        for x,y in lst[i].items():
             if (lst[i][x]['batsman']=='RT Ponting'):
                    count+=1
        

    return count
deliveries_count()

