# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    difference =0
    # Write your code here
    e1=[]
    data0=(data['innings'][0]['1st innings']['deliveries'])
    for a in data0:
        for b in a:
            if 'extras' in (a[b].keys()):
                if 'legbyes' in a[b]['extras']:
                    e1.append(a[b]['extras']['legbyes'])
                if 'wides' in a[b]['extras']:
                    e1.append(a[b]['extras']['wides'])
    #print(e1)

    e2=[]
    data1=(data['innings'][1]['2nd innings']['deliveries'])
    for a in data1:
        for b in a:
            if 'extras' in (a[b].keys()):
                if 'legbyes' in a[b]['extras']:
                    e2.append(a[b]['extras']['legbyes'])
                if 'wides' in a[b]['extras']:
                    e2.append(a[b]['extras']['wides'])
    #print(e2)
    difference=sum(e2)-sum(e1)
    return difference
#print(extras_runs(data))
