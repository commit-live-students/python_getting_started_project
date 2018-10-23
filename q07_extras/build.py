# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    
    l=(data['innings'][0]['1st innings']['deliveries'])
    E1=[0,0,0]
    x=0
    for a in l:
        for b in a:
            if 'extras' in a[b].keys():
                x+=1
                if 'wides' in a[b]['extras'].keys():
                    E1[0]+=1

                elif 'legbyes' in a[b]['extras'].keys():
                    E1[1]+=1
                else:
                    E1[2]+=1
    
    l2=(data['innings'][1]['2nd innings']['deliveries'])
    E1=[0,0,0]
    y=0
    for a in l2:
        for b in a:
            if 'extras' in a[b].keys():
                y+=1
                if 'wides' in a[b]['extras'].keys():
                    E1[0]+=1

                elif 'legbyes' in a[b]['extras'].keys():
                    E1[1]+=1
                else:
                    E1[2]+=1

    difference = y-x

    return difference

l2=(data['innings'][1]['2nd innings']['deliveries'])
E1=[0,0,0]
x=0
for a in l2:
    for b in a:
        if 'extras' in a[b].keys():
            x+=1
            if 'wides' in a[b]['extras'].keys():
                E1[0]+=1
                
            elif 'legbyes' in a[b]['extras'].keys():
                E1[1]+=1
            else:
                E1[2]+=1
print(E1)
print(x)
(data['innings'][1]['2nd innings']['deliveries'][1][0.2]['extras'])

l2=(data['innings'][0]['1st innings']['deliveries'])
E1=[0,0,0]
x=0
for a in l2:
    for b in a:
        if 'extras' in a[b].keys():
                x+=1
                if 'wides' in a[b]['extras'].keys():
                    E1[0]+=1

                elif 'legbyes' in a[b]['extras'].keys():
                    E1[1]+=1
                else:
                    E1[2]+=1

h = extras_runs()
h


