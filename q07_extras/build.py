# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def check_extrs_innings(extrs_innings, deliveries):
    for eachdel in deliveries:
        for checkextrs in eachdel:
            each_bowlinfo = eachdel[checkextrs]
            #print each_bowlinfo
            for eachd in each_bowlinfo:
                if eachd == 'extras':
                    get_extrsinfo = each_bowlinfo[eachd]
                    extrs_innings.append(get_extrsinfo)
    return
# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_inn_extrs = []
    deliveries = data['innings'][0]['1st innings']['deliveries'] # deliveries is a list
    check_extrs_innings(first_inn_extrs, deliveries)

    second_inn_extrs = []
    deliveries = data['innings'][1]['2nd innings']['deliveries'] # deliveries is a list
    check_extrs_innings(second_inn_extrs, deliveries)

    difference = abs(len(first_inn_extrs) - len(second_inn_extrs))

    #print difference
    return difference

#extras_runs(data)
