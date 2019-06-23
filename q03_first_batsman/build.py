# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    name = str(data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])
    return name

if __name__ == '__main__':
    first_batsman()
    print(first_batsman())


