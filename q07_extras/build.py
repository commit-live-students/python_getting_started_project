# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    

    # Write your code here
    firstExtras=[]
    secondExtras=[]
    ex=data['innings'][0]['1st innings']['deliveries']
    for element in ex:
        #print(type(element))
        for k,e in element.items():
            try:
                #print(e['extras'])
                for k1,e1 in e['extras'].items():
                    #print(k1,':',e1)
                    firstExtras.append(k1)
                    #print(firstExtras)
            except:
                break
    ex=data['innings'][1]['2nd innings']['deliveries']
    for element in ex:
        #print(type(element))
        for k,e in element.items():
            try:
                #print(e['extras'])
                for k1,e1 in e['extras'].items():
                    #print(k1,':',e1)
                    secondExtras.append(k1)
                    #print(secondExtras)
            except:
                break
    if len(firstExtras)>len(secondExtras):
        extra_balls=len(firstExtras)-len(secondExtras)
    else:
        extra_balls=-len(firstExtras)+len(secondExtras)
        #print(extra_balls)
            


    difference =extra_balls


    return difference



