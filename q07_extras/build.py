# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extra1=0
    extra2=0
    for a in data['innings'][0]['1st innings']['deliveries']:
        for b in a.items():
            if len(b[1])==5:
                for z in b[1].items():
                    if isinstance(z[1],dict):
                        if len(z[1])==1:
                            for me in z[1].values():
                            #print(me)
                                extra1=extra1+1
                            #print(extra1) 
                                
    for p in data['innings'][1]['2nd innings']['deliveries']:
        for q in p.items():
            if len(q[1])==5:
                for h in q[1].items():
                    if isinstance(h[1],dict):
                        if len(h[1])==1:
                            for me1 in h[1].values():
                            #print(me1)
                                extra2=extra2+1
                            #print(extra2)
                            #print(extra1)
                            #print(extra2)
                                difference =extra2-extra1
                            #print(difference)
    return difference


