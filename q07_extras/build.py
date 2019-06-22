import yaml as ym
import os as sys

def read_data():
    fName='data/ipl_match.yaml'
    dict = ym.load(open(fName))
    return dict

def teams(ipl_dict):
    lst = (ipl_dict['info']['teams'])
    return lst

def first_batsman (ipl_dict):
    innings_dict=(ipl_dict['innings'][0])
    over_dict=(innings_dict['1st innings']['deliveries'][0])
    return (over_dict[0.1]['batsman'])

def deliveries_count (ipl_dict):
    int_deliveries_played=0
    innings_dict=(ipl_dict['innings'][0])
    lst_overs=(innings_dict['1st innings']['deliveries'])
    for index, x in enumerate(lst_overs):
        dict_overs=lst_overs[index]
        for key,value in dict_overs.items():
            if dict_overs[key]['batsman'] == 'RT Ponting':
                int_deliveries_played+=1
    return int_deliveries_played


def BC_runs(ipl_dict):
    int_runs_scored=0
    innings_dict=(ipl_dict['innings'][0])
    lst_overs=(innings_dict['1st innings']['deliveries'])
    for index, x in enumerate(lst_overs):
        dict_overs=lst_overs[index]
        for key,value in dict_overs.items():
            if dict_overs[key]['batsman'] == 'BB McCullum':
                int_runs_scored +=dict_overs[key]['runs']['batsman']
    return int_runs_scored

def bowled_out(ipl_dict):
    lst_bowled=[]
    innings_dict=(ipl_dict['innings'][1])
    lst_overs=(innings_dict['2nd innings']['deliveries'])
    for index, x in enumerate(lst_overs):
        dict_overs=lst_overs[index]
        for key,value in dict_overs.items():
            if 'wicket' in dict_overs[key]:
                if dict_overs[key]['wicket']['kind'] == 'bowled':
                    lst_bowled.append(dict_overs[key]['wicket']['player_out'])
    return lst_bowled

def extras_runs(ipl_dict):
    lst_1st_innnings_extras=[]
    lst_2nd_innnings_extras=[]
    int_1st_innnings_extras=0
    int_2nd_innnings_extras=0
    bln_1st_innings = True
    lst_innings=ipl_dict['innings']
    for inn_index, inn_x in enumerate(lst_innings):
        if '2nd innings' in lst_innings[inn_index]:
            bln_1st_innings = False
        dict_overs=lst_innings[inn_index]
        for key,value in dict_overs.items():
            lst_deliveries = dict_overs[key]['deliveries']
            for index, x in enumerate(lst_deliveries):
                dict_deliveries=lst_deliveries[index]
                for over_key,value in dict_deliveries.items():
                    if dict_deliveries[over_key]['runs']['extras']>0:
                        if bln_1st_innings:
                            lst_1st_innnings_extras.append(dict_deliveries[over_key]['runs']['extras'])
                            int_1st_innnings_extras+=1
                        else:
                            lst_2nd_innnings_extras.append(dict_deliveries[over_key]['runs']['extras'])
                            int_2nd_innnings_extras+=1
    return int_2nd_innnings_extras - int_1st_innnings_extras 


print('current dir : ' , sys.getcwd())
#fName='data/ipl_match.yaml'
dict_ipl=read_data()
lst_ipl_teams=teams(dict_ipl)
v_team1=lst_ipl_teams[0]
v_team2=lst_ipl_teams[1]
print ('Team 1 : ', v_team1)
print ('Team 2 : ', v_team2)

str_first_batsman = first_batsman(dict_ipl)
#str_first_batsman = lst_first_batsman [0]
print('First batsman : ',str_first_batsman)
int_total_deliveries_played = deliveries_count (dict_ipl)
print ('int_total_deliveries_played : ' , int_total_deliveries_played )
int_total_runs_scored = BC_runs (dict_ipl)
print ('int_total_runs_scored : ' , int_total_runs_scored )
lst_bowled_players=bowled_out(dict_ipl)
print ('Players Bowled : ',lst_bowled_players)
lst_difference=extras_runs(dict_ipl)
print('Difference  : ',lst_difference)



