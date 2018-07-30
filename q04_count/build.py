# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    my='RT Ponting'
    innings=data['innings']
    first=innings[0]
   

    final_inning_list=first['1st innings']['deliveries']
    #print(type(final_inning_list))
   
    #print(final_inning_list)
    for x in final_inning_list:
        for key,value in x.items():
            final=value
            #print(final)
            for k,v in final.items():
                if my in v:
                    count += 1
                              
          
    return count


deliveries_count()


