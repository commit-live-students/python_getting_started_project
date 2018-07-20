
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
delv1 = data['innings'][0]['1st innings']['deliveries']
delv2 = data['innings'][1]['2nd innings']['deliveries']
list1 =[]
list2 =[]
def extras_runs(data):
    delv1 = data['innings'][0]['1st innings']['deliveries']
    delv2 = data['innings'][1]['2nd innings']['deliveries']
    list1 = 0
    list2 = 0
    for i1 in delv1:
        for a1 in i1.items():
            if 'extras' in a1[1].keys():
                list1+=1
    for i2 in delv2:
            for a2 in i2.items():
                if 'extras' in a2[1].keys():
                    list2+=1
    difference = abs(list1-list2)
    return difference
extras_runs(data)






