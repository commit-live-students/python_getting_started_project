# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    list1extras=0
    list2extras=0
    list1= data['innings'][0]['1st innings']['deliveries']
    list2= data['innings'][1]['2nd innings']['deliveries']
    for a in list1:
        for b in a:
            var1=a[b]
            for c in var1:
                if c == 'extras':
                    var2 = var1[c]
                    for d in var2:
                        list1extras = list1extras + 1
    for e in list2:
        for f in e:
            var3=e[f]
            # print(var1)
            for g in var3:
                if g == 'extras':
                    var4 = var3[g]
                    for h in var4:
                        list2extras= list2extras + 1
    difference = list2extras - list1extras
    return difference



