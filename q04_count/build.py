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
            #print('Key : ', key , '  ----> Value  : ', value)
            if dict_overs[key]['batsman'] == 'RT Ponting':
                int_deliveries_played+=1
    return int_deliveries_played


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


