# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    name = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return name

from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

piq = first_batsman()
type(piq)
type(data)
for i in data: print(i)
for i in data.values(): crass = i
type(data['innings'][0])
data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
data['innings'][0]['1st innings']['deliveries'][0][0.1]
type(crass[0])
indict = crass[0]
for i in indict.values(): 
    print(i)
type(indict)
for x,y in indict.items():
    #print(type(x))
    #print(type(y))
    indict2=y
    #print('the key is :'+x+' while the value is '+str(y))
type(indict)
type(indict2)
for i in indict2.values(): inlist2 = i
type(inlist2)
for i,j in indict2.items(): print('the key is '+i+' while the value is '+str(j))
type(inlist2[0])
type(inlist2[0][0.1])
inlist2[0][0.1]['batsman']


