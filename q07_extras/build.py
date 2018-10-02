# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    
    l=(data['innings'][0]['1st innings']['deliveries'])
    e1=[0,0,0]
    c=0
    for x in l:
        for y in x:
            if 'extras' in x[y].keys():
                c+=1
                if 'wides' in x[y]['extras'].keys():
                    e1[0]+=1

                elif 'legbyes' in x[y]['extras'].keys():
                    e1[1]+=1
                else:
                    e1[2]+=1
    
    
    l2=(data['innings'][1]['2nd innings']['deliveries'])
    e1=[0,0,0]
    c1=0
    for x in l2:
        for y in x:
            if 'extras' in x[y].keys():
                c2+=1
                if 'wides' in x[y]['extras'].keys():
                    e1[0]+=1

                elif 'legbyes' in x[y]['extras'].keys():
                    e1[1]+=1
                else:
                    e1[2]+=1
    
    

    difference =c2-c


    return difference

l2=(data['innings'][1]['2nd innings']['deliveries'])
e1=[0,0,0]
c=0
for x in l2:
    for y in x:
        if 'extras' in x[y].keys():
            c+=1
            if 'wides' in x[y]['extras'].keys():
                e1[0]+=1
                
            elif 'legbyes' in x[y]['extras'].keys():
                e1[1]+=1
            else:
                e1[2]+=1
print(e1)
print(c)
(data['innings'][1]['2nd innings']['deliveries'][1][0.2]['extras'])

l2=(data['innings'][0]['1st innings']['deliveries'])
e1=[0,0,0]
c=0
for x in l2:
    for y in x:
        if 'extras' in x[y].keys():
                c+=1
                if 'wides' in x[y]['extras'].keys():
                    e1[0]+=1

                elif 'legbyes' in x[y]['extras'].keys():
                    e1[1]+=1
                else:
                    e1[2]+=1

