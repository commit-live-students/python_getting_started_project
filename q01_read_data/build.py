import yaml
def read_data():
    data_path = './data/ipl_match.json'
    ip_data= open(data_path,'r')
    d1=yaml.load(ip_data)
    return d1
