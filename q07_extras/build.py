# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data['innings']#[0]['1st innings']
# Your Solution

def extras_runs(data=data):
    # Write your code here
    extra1 = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for lst in deliveries:
        for overs in lst:
            if lst[overs]['runs']['extras']!=0:
                extra1 += 1 #list[overs]['runs']['extras']

# Your Solution
    extra2 = 0
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for lst in deliveries:
        for overs in lst:
            if lst[overs]['runs']['extras']!=0:
                extra2 += 1 #list[overs]['runs']['extras']

    #print second_inn_extras
    difference = extra2 - extra1
    print(extra2)
    print(extra1)
    print(difference)
    return difference
extras_runs()
data['innings'][0][next(iter(data['innings'][0]))]['deliveries'][1][0.2]['runs']['extras']
#data['innings'][0][next(iter(data['innings'][0]))]['deliveries'][0][next(iter(data['innings'][0][next(iter(data['innings'][0]))]['deliveries'][0]))]['runs']['extras']
#data['innings']

# for a in data['innings'][0]['1st innings']['deliveries']:
#     for b in a:
#         print(b)

print(data['innings'][0]['1st innings']['deliveries'][0])#[0]

data
data['innings']#[0]['1st innings']
# Your Solution

def extras_runs(data=data):
    extra1 = []
    extra2 = []

#     # Write your code here
    for innings in data['innings']:
        for delivery in innings[next(iter(innings))]['deliveries']:
            if(next(iter(innings)) == '1st innings'):
                if(delivery[next(iter(delivery))]['runs']['extras'] != 0):
                    extra1.append(delivery[next(iter(delivery))]['runs']['extras'])
            if(next(iter(innings)) == '2nd innings'):
                if(delivery[next(iter(delivery))]['runs']['extras'] != 0):#to remove 0s from output
                    extra2.append(delivery[next(iter(delivery))]['runs']['extras'])
    
#     sum1,sum2=0
#     difference = map(lambda x:(sum1 += x), extra1) - map(lambda x : (sum2 += x), extra2)
#     if(sum(extra1) >= sum(extra2)):
#         difference = sum(extra1) - sum(extra2)
#     else:
#         difference = sum(extra2) - sum(extra1)

    print(extra1)
    print(extra2)


    difference = len(extra2) - len(extra1)
 

    return difference
extras_runs()


