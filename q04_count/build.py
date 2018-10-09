# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
#       dict     lst dict            dict        v_lst v_dict dict
#x=data['innings'][0]['1st innings']['deliveries'][0]['0.1']['batsman']
x=data['innings'][0]['1st innings']['deliveries']
#print(type(x))
#print(x)


# Your Solution Here
def deliveries_count(data):
    
    # Your code here
    count=0

    for i,v in enumerate(x):
        y=x[i]
        #print(type(y))
        for k,v in y.items():
            if y[k]['batsman']=='RT Ponting':
                count += 1
            
    
    

    return count
    
deliveries_count(data)






    





