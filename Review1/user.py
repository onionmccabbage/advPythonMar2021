from address import Address
from company import Company

import my_meta

class User(metaclass=my_meta.DocChecker):
    '''
    User class
    id is read-only (once initialized)
    name must be a non-empty string
    address and company are instances of the Address and Company classes
    '''
    def __init__(self, id, name, address, company ):
        self.__id = id
        self.__name = name
        self.__address = address
        self.__company = company
    def __str__(self):
        t = 'id: {} Name: {}\n'.format(str(self.__id), self.__name)
        t += "{}{}\n".format( self.__address.__str__(), self.__company.__str__() )
        return t
    
    @property
    def id(self):
        return self.__id
    # @id.setter # leave this out for a read-only ID
    # def id(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError("id must be an integer")
    #     if value <0:
    #         raise TypeError('id cannot be negative')
    #     self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == '':
            raise TypeError('Name cannot be an empty string')
        self.__name = value
    
if __name__ == '__main__':
    a = Address('Main Street', 'Athlone', '123-456')
    c = Company('Mega Corp','Always there for you')
    u1  = User(id=1, name='Ada', address=a, company=c)
    u2 = User(2, 'Timnit', a, c) # these are ordinal parameters
    # we cannot change an id
    # u1.id = 99 # fails
    print(u1, u2)