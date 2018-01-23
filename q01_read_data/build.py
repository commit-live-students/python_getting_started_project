import yaml

#def read_data(path='C:\Users\Madhav.Mishra\.atom\.commit-live\code\python_getting_started_project\data\ipl_match.yaml'):
def read_data(path='./data/ipl_match.yaml'):
    with open(path, 'r') as f:
        data=yaml.load(f)
    return data


    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    #data =yaml.load(f)

    # return data variable
    #return data
