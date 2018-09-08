# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
#ing=data.get('innings')
#firsting=ing[0]
#print(firsting.get('1st innings').get('deliveries')[0].get(0.1).get('batsman'))


#print(ing)

# Your Solution
def first_batsman(data=data):
    ing=data.get('innings')
    firsting=ing[0]
    name=firsting.get('1st innings').get('deliveries')[0].get(0.1).get('batsman')

    # Write your code here




    return name

first_batsman(data)


