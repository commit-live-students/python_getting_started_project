# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    data = data['innings']

    data = [i['1st innings'] for i in data if '1st innings' in i]

    data = [i['deliveries'] for i in data if 'deliveries' in i]

    name = data[0][0][0.1]['batsman']

    return name
