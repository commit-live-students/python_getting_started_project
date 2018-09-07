import yaml
def teams(data):
    info = data['info']
    team = info['teams']
    return team

with open('data/ipl_match.yaml','r') as stream:
    data = yaml.load(stream)
    
teams(data)

