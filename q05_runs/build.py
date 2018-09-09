from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def BC_runs(data):
    runs = 0
    d = list(data['innings'][0]['1st innings']['deliveries'])
    for index, value in enumerate(d):
        for key in value:
            if value[key]['batsman'] == 'BB McCullum':
                runs += value[key]['runs']['batsman']
            else:
                break
                 
    


    return(runs)

data = read_data()
runs = 0
d = list(data['innings'][0]['1st innings']['deliveries'])
for index, value in enumerate(d):
    for key in value:
        if value[key]['batsman'] == 'BB McCullum':
            runs += value[key]['runs']['batsman']
        else:
            break
                
print (runs)


