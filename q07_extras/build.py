

from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data1=data['innings'][0]['1st innings']['deliveries']
data2=data['innings'][1]['2nd innings']['deliveries']

def extra_runs(data=data):
    count = 0
    for x in data1:
        for a,b in x.items():
            for p,q in b.items():
                if p == 'runs':
                    for c,d in q.items():
                        if c == 'extras' and d != 0:
                            count+=1
    count1 = 0

    for x in data2:
        for a,b in x.items():
            for p,q in b.items():
                if p == 'runs':
                    for c,d in q.items():
                        if c == 'extras' and d != 0:
                            count1+=1
    count=count1-count
    
    return count


