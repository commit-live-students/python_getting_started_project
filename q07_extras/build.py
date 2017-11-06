# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_innings = data['innings'][0]['1st innings']['deliveries']
    second_innings = data['innings'][1]['2nd innings']['deliveries']

    first_innigs_extras = [d.values()[0]['runs']['extras'] for d in first_innings]
    second_innings_extras = [d.values()[0]['runs']['extras'] for d in second_innings]

    extra1= len([extras for extras in first_innigs_extras if extras > 0])
    extra2= len([extras for extras in second_innings_extras if extras > 0])

    difference = extra2 - extra1
    return difference
