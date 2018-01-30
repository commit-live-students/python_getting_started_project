# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):

    # write your code here
    for datakeys in data:
        #print key
        if datakeys == 'info':
            #print data[key]
            infokeys = data[datakeys]
            for ik in infokeys:
                #print ik
                if ik == 'teams':
                    #print info_keys[ik]
                    teamsDict = infokeys[ik]

    teams = list(teamsDict)
    #print teamsDict
    #print type(teamsDict)

    return teams
