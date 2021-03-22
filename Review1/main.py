import requests
import json
from address import Address
from company import Company
from user import User

def main():
    # get a number from the user
    n = ''
    while not n.isdigit():
        n = input('which user would you like to access?')
        # if int(n)>10:
        #     n=''
    urlStub = 'https://jsonplaceholder.typicode.com/users/'
    try:
        res = requests.get(urlStub + n)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        userDict = res.json()
        # print(userDict['company']['name']) # check we have some data
        # populate instances of Company, Address and User
        co_name = userDict['company']['name']
        co_catch = userDict['company']['catchPhrase']
        co_bs = userDict['company']['bs']
        user_co = Company(name=co_name, catchPhrase=co_catch, bs=co_bs)
        
        add_street = userDict['address']['street']
        add_city = userDict['address']['city']
        add_zip = userDict['address']['zipcode']
        user_address = Address(street=add_street, city=add_city, zipcode=add_zip)
        
        user = User(id=userDict['id'], name=userDict['name'], address=user_address, company=user_co)
        print(user)

if __name__ == '__main__':
    main()