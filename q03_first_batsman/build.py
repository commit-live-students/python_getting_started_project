# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data):
    name = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return name
