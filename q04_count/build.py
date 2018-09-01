# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data['innings'][0]['1st innings']['deliveries']#[1][0.2]['batsman']
a = data['innings'][0]['1st innings']['deliveries']#[2]#.key()#['batsman']
a
#len(a)

keyss = []
for i in a:
    k = next(iter(i))
    keyss.append(k)
#print(keyss)

#type(keyss[0])
    
#print(len(keyss))

# for j in keyss:
#     print(j)

# # # for i in a:
# # #    #if(i.keys()) == 0.1
# # #    print(next(iter(i))) 
    

# count = 0
# for i in range(124):
#     #print(i)
#     for j in keyss:
#         print(data['innings'][0]['1st innings']['deliveries'][i][j]['batsman'])
#         if(data['innings'][0]['1st innings']['deliveries'][i][j]['batsman'] == 'RT Pointing'):
        
#             count = count + 1  
        
# count

# count = 0
# for i,j in zip(range(124),keyss):
#     #print(data['innings'][0]['1st innings']['deliveries'][i][j]['batsman'])
#     if((data['innings'][0]['1st innings']['deliveries'][i][j]['batsman']) == 'RT Ponting'):
        
#         count += 1          
# count

# for i,j in zip(range(124),keyss):
#     print(i,j)
#if()

# Your Solution Here
def deliveries_count(data=data):
    
#     # Your code here
    count = 0
    for i,j in zip(range(124),keyss):
        if((data['innings'][0]['1st innings']['deliveries'][i][j]['batsman']) == 'RT Ponting'):
        
            count += 1  
        

    return count

# c = deliveries_count()
# c




