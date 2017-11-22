# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    count_1st=0
    count_2nd=0
    item = data['innings'][0]['1st innings']['deliveries']
    for i in range(0,len(item)):
        key1 = item[i].keys()[0]
        key2 = item[i][key1].keys()[3]
        if( key2 == 'extras'):
            key3 = item[i][key1][key2].keys()[0]
            statment = item[i][key1][key2][key3]

            if( key3 == 'legbyes' ):
                extra_run = int( statment )
                count_1st = count_1st + extra_run
            elif( key3 == 'wides' ):
                extra_run = int( statment )
                count_1st = count_1st + extra_run

    item = data['innings'][1]['2nd innings']['deliveries']
    for i in range(0,len(item)):
        key1 = item[i].keys()[0]
        key2 = item[i][key1].keys()[3]
        if( key2 == 'extras'):
            key3 = item[i][key1][key2].keys()[0]
            statment = item[i][key1][key2][key3]

            if( key3 == 'legbyes' ):
                extra_run = int( statment )
                count_2nd = count_2nd + extra_run
            elif( key3 == 'wides' ):
                extra_run = int( statment )
                count_2nd = count_2nd + extra_run

    difference =count_2nd-count_1st
    return difference
