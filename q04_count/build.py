# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    
    deliveries_1st = data['innings'][0]['1st innings']['deliveries']
    for i in deliveries_1st:   
        for key in i:
            if(i[key]['batsman']=='RT Ponting'):
                count+=1
                #print(i[key]['batsman'])

    #print(count)
            
    
    return count

deliveries_count()



