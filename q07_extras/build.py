from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
deliv1 =  data['innings'][0]['1st innings']['deliveries']
deliv2 =  data['innings'][1]['2nd innings']['deliveries']
def extras_runs(data=data):
    xtras1 = 0
    xtras2 = 0
    for balls in deliv1:
        extras1 = balls.values()[0]['runs']['extras']
        if extras1 != 0:
            xtras1 = xtras1 + 1
    for balls in deliv2:
        extras1 = balls.values()[0]['runs']['extras']
        if extras1 != 0:
            xtras2 = xtras2 + 1
    extras = xtras2 - xtras1
    return extras
