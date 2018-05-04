
import yaml

def read_data():

    # import the csv file into  variable
    # path to access the CSV file: '../data/ipl_match.yaml'
    
    with open('./data/ipl_match.yaml', 'r') as infile:
        try:
            data = yaml.load(infile)
        except yaml.YAMLError as exc:
            print ('scanner error 1')
    print(data)
    # return data variable
    return data

read_data()


