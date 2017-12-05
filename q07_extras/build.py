# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1st = []
    extras_2nd = []
    difference = 0
    data = data['innings']

    def extra(data):
        extra_innings_run = []
        for i in data:
            if 'deliveries' in i:
                for l in data[i]:
                    for j in l:
                        for k in l[j]:
                            if k == 'extras':
                                extra_innings_run.append(l[j]['runs']['extras'])


        return extra_innings_run

    for i in data:
        if '1st innings' in i:
            extras_1st = extra(i['1st innings'])
            print extras_1st
        if '2nd innings' in i:
            extras_2nd = extra(i['2nd innings'])
            print extras_2nd


    difference = len(extras_2nd) - len(extras_1st)

       
    return difference
