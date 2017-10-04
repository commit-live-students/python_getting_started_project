from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    # Your code here
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        for key, val in delivery.items():
            if(val['batsman'] == 'BB McCullum'):
                runs = runs + val['runs']['batsman']
    return(runs)

BC_runs(data)
