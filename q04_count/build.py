             
   # %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



# Your Solution Here
def deliveries_count(data=data):
    count=0
    innings=data['innings']
    first=innings[0]
    final_inning_list=first['1st innings']['deliveries']
    for x in final_inning_list:
        for key,value in x.items():
            #print('key',key,'value',value)
            if(value['batsman']=='RT Ponting'):
                            count=count+1
    
    # Your code here
    
    return count


deliveries_count()
           

