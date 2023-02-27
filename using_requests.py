import requests

def getData(whichId=1):
    url = f'http://jsonplaceholder.typicode.com/users/{whichId}'
    r = requests.get(url)
    r_dict = r.json() # convert the returned data to a dictionary
    return r_dict

if __name__ == '__main__':
    q = input('please enter 1-10')
    users = getData(q)
    print(users)