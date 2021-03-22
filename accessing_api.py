# we can use the requests library to access end-point APIs
import requests
import json

def main():
    # we can ask for user input
    id = input('which user id? ')
    category = input('which category (users, photos, albums or posts)')

    if category not in ('users', 'photos', 'albums', 'posts'):
        category = 'users'

    # we need a URL
    url = 'http://jsonplaceholder.typicode.com/{}/{}'.format(category, id)
    # we can make a get request to this url
    response = requests.get(url) # the entire response is returned
    # we can convert the returned json to a Python dictionary
    print(response.text) # we usually only want the returned text
    d = json.loads(response.text) # or response.json or response.html
    print(d) # we now have a dictionary

if __name__ == '__main__':
    main()