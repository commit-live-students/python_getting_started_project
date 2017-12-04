from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
    count = 0
    Mcc = data['innings'][0]['1st innings']['deliveries']
    run = 0
    for b in range(len(Mcc)):
        dely = data['innings'][0]['1st innings']['deliveries'][run].keys()
        batsmans = data['innings'][0]['1st innings']['deliveries'][run][dely[0]]['batsman']
        if batsmans == 'BB McCullum':
            batsmans = data['innings'][0]['1st innings']['deliveries'][run][dely[0]]['runs']['batsman']
            #print batsmans
            count += batsmans
        run += 1

        #bats = data['innings'][0]['1st innings']['deliveries'][balls][dely[0]]['batsman']
        #if bats == 'RT Ponting':
    return count



    #return(runs)
print BC_runs()
