# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    deliveries_1st = data['innings'][0]['1st innings']['deliveries']
    deliveries_2nd = data['innings'][1]['2nd innings']['deliveries']
    list1 = []
    list2=[]
    
    for i in deliveries_1st:   
        for key in i:
            #print(i[key])
            if('extras' in i[key]):
                #print(i[key]['extras'])
                extras_dict = i[key]['extras']

                for extras in extras_dict.values():
                    list1.append(extras)
        #count1+=i[key]['runs']['extras']    
    #print('\n')
    for i in deliveries_2nd:   
        for key in i:
            #print(i[key])
            if('extras' in i[key]):
                #print(i[key]['extras'])
                extras_dict = i[key]['extras']
                for extras in extras_dict.values():
                    list2.append(extras)
        #count2+=i[key]['runs']['extras']
 
    
    #print(len(list1))
    #print(len(list2))
    difference = len(list2) - len(list1)
    return difference
    
extras_runs(data)  


