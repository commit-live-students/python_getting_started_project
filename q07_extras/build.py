# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    firstextra = 0
    secondextra = 0
    y=data['innings'][0]['1st innings']['deliveries']
    for a in y:
            for i in a:
                if 'extras' in a[i]:
                        firstextra +=1

    #print firstextra
    x=data['innings'][1]['2nd innings']['deliveries']
    for a in x:
            for i in a:
                if 'extras' in a[i]:
                        secondextra +=1
    #print secondextra
    #d=secondextra - firstextra
    if (secondextra - firstextra) > 0:
        difference = (secondextra - firstextra)
    else:
        difference = (firstextra - secondextra)


    return difference

extras_runs()
