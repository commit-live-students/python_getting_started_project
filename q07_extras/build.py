# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def extras_runs(data=data):
    extras_1st,extras_2nd=[],[]
    count1,count2=0,0

    deliveries_1=data['innings'][0]['1st innings']['deliveries']

    for deliveries in deliveries_1:
        for rounds in deliveries:
            if deliveries[rounds]['runs']['extras'] != 0:
                e1=deliveries[rounds]['runs']['extras']
                count1 += 1
                extras_1st.append(e1)

    deliveries_2=data['innings'][1]['2nd innings']['deliveries']
    for deliveries in deliveries_2:
        for rounds in deliveries:
            if deliveries[rounds]['runs']['extras'] !=0:
                e2=deliveries[rounds]['runs']['extras']
                count2 += 1
                extras_2nd.append(e2)

    difference = count2-count1
    return difference
