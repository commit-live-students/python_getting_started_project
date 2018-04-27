# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1st=[]
    extras_2nd=[]
    deliveries_1= data['innings'][0]['1st innings']['deliveries']
    deliveries_2= data['innings'][1]['2nd innings']['deliveries']
#     print(deliveries)
    #for 1st innings
    for a in (deliveries_1):
        data1=list(a.values())
        if 'extras' in data1[0].keys():
           # print(data1[0])
            extras_1st.append(data1[0]['runs']['extras'])
    x=len(extras_1st)
    print(x)
   #for 2nd innungs 
    for b in (deliveries_2):
        data2=list(b.values())
        if 'extras' in data2[0].keys():
            #print(data2[0])
            extras_2nd.append(data2[0]['runs']['extras'])
    y=len(extras_2nd)
    print(y)
    difference = y - x 

    return difference
extras_runs()


