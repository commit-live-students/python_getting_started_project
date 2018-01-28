# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    inning1,inning2 = [],[]
    b = data['innings'][0]['1st innings']['deliveries']
    for i in range(len(b)):
        for j in b[i]:
            for k in b[i][j]:
                if k == 'extras':
                    for x in b[i][j][k]:
                         inning1 += [b[i][j][k][x]]
    b = data['innings'][1]['2nd innings']['deliveries']
    for i in range(len(b)):
        for j in b[i]:
            for k in b[i][j]:
                if k == 'extras':
                    inning2 +=[1]
                    
    difference = 6

    # Write your code here



    return difference
