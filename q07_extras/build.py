# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_first_innings=[]
    extras_second_innings=[]
    new1=[]
    new2=[]
    for balls in data['innings'][0]['1st innings']['deliveries']:
        for key,values in balls.items():
            try:
                new_value = values['extras']
                extras_first_innings.append(list(new_value.values()))
                #print (extras_first_innings)
            except KeyError:
        # Key is not present
                pass
    for i in extras_first_innings:
        new1.append (i[0])

    for balls in data['innings'][1]['2nd innings']['deliveries']:
        for key,values in balls.items():
            try:
                new_value = values['extras']
                list(new_value.values())
                extras_second_innings.append(list(new_value.values()))
            except KeyError:
        # Key is not present
                pass

    for i in extras_second_innings:
        new2.append (i[0])



    difference =abs(len(new1)-len(new2))


    return difference
