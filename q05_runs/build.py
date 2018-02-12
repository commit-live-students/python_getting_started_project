# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



def BC_runs(data):
    McCullum_runs =0
    deliveries=data['innings'][0]['1st innings']['deliveries']

    for deliveries in deliveries:
        for rounds in deliveries:
            if deliveries[rounds].get('batsman')== 'BB McCullum':
                batsman=deliveries[rounds].get('batsman')
                runs=deliveries[rounds].get('runs')
                McCullum_runs += runs[runs.keys()[0]]
    print McCullum_runs

    return(McCullum_runs)
