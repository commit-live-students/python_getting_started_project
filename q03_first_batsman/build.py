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



