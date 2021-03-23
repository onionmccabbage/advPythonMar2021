class Company:
    '''
    Company class
    name and catchPhrase must be non-empty strings
    '''
    def __init__(self, name='', catchPhrase=''):
        self.__name = name # __ does name mangling - prevents direct access
        self.__catchPhrase = catchPhrase
    def __str__(self):
        return 'Name: {} Catch: {}\n'.format(self.__name, self.__catchPhrase)
        
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

    @property
    def catchPhrase(self):
        return self.__catchPhrase
    @catchPhrase.setter
    def catchPhrase(self, value):
        if not isinstance(value, str):
            raise TypeError("Catch Phrase must be a string")
        if value == '':
            raise TypeError('Catch Phrase cannot be an empty string')
        self.__catchPhrase = value

if __name__ == '__main__':
    c = Company('Mega Corp','Always there for you')
    print(c)
    # try to set and get the name
    print(c.name) # use the accessor
    c.name = 'changed' # use the mutator
    print(c.name)
