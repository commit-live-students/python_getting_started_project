# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()
teams = teams(data)
                  
# solution
def teams(data=data):
    ipl=[]
    # write your code here
    header=tuple(ipl[0])

#set team1
    team_1 =[x[3] for x in ipl[1:]] 
    team_1=[]
    for x in ipl[1:]:
        team_1.append(x[3])
    
    #set team 2
    team_2=[x[4] for x in ipl[1:]]
    #change the list s to set for team_1 and team_2
    team_1=set(team_1) 
    team_2=set(team_2)

#retrive the unique values from the set
    teams=list(team_1.union(team_2))
    #teams =
    print(teams)



