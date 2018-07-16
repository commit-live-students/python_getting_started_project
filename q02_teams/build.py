import yaml as ym
import os as sys

def read_data():
    fName='data/ipl_match.yaml'
    dict = ym.load(open(fName))
    return dict

def teams(ipl_dict):
    lst = (dict_ipl['info']['teams'])
    return lst

print('current dir : ' , sys.getcwd())
#fName='data/ipl_match.yaml'
dict_ipl=read_data()
lst_ipl_teams=teams(dict_ipl)
v_team1=lst_ipl_teams[0]
v_team2=lst_ipl_teams[1]
print ('Team 1 : ', v_team1)
print ('Team 2 : ', v_team2)


