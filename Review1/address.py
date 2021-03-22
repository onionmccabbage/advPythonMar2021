class Address:
    '''Address class
       street, city and zipcode must all be non-emoty strings
    '''
    def __init__(self, street, city, zipcode, geo={'lat':53.43333, 'lon':-7.95}):
        self.__street = street
        self.__city = city
        self.__zipcode = zipcode
        self.__geo = geo
    def __str__(self):
        return 'Street: {} City: {} zip: {} geo: {}\n'.format(self.__street, self.__city, self.__zipcode, self.__geo)
    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, value):
        if not isinstance(value, str):
            raise TypeError("Street must be a string")
        if value == '':
            raise TypeError('Street cannot be an empty string')
        self.__street = value

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError("City must be a string")
        if value == '':
            raise TypeError('City cannot be an empty string')
        self.__city = value
    
    @property
    def zipcode(self):
        return self.__zipcode
    @zipcode.setter
    def zipcode(self, value):
        if not isinstance(value, str):
            raise TypeError("zipcode must be a string")
        if value == '':
            raise TypeError('zipcode cannot be an empty string')
        self.__zipcode = value
    @property
    def geo(self):
        return self.__geo
    @geo.setter
    def street(self, geo):
        if not isinstance(geo, dict):
            raise TypeError("Geo must be a dictionary")
        if geo == {}:
            raise TypeError('Street cannot be an empty dictionary')
        self.__geo = geo

if __name__ == '__main__':
    a = Address('Main Street', 'Athlone', '123-456', )
    print(a)