# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries'] # deliveries is a list
    runs = 0

    for delivery in deliveries:#delivery is a dictionary
        for deliv in delivery:
            dell = delivery[deliv]
            if (dell['batsman'] == 'BB McCullum'):
                runs_dict = dell['runs']
                runs += runs_dict['batsman'] # batsman - 158, total - 169, testcase is validatingfor 158
                #print dell

    #print 'Runs : ', runs
    return(runs)
#BC_runs(data)
