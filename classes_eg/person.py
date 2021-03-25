# we can capture any structure we like as a class

class Person():
    __slots__ = ('name', 'email', '__longevity')
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        # self.__longevity = age
        self.achievement = age # call the setter
    # methods for this class
    @property
    def achievement(self):
        return self.__longevity
    @achievement.setter
    def achievement(self, updatedAge):
        if type(updatedAge) == int:
            self.__longevity = updatedAge
        else:
            self.__longevity = 42 # we have a default value

if __name__ == '__main__':
    ada = Person('Ada', 'a@b.ie', False)
    ada.name = True
    # ada.__longevity = {} # fails!
    ada.achievement = 121
    print( ada.achievement ) # __ mangles the name so it cannot be directly accessed
    # we can still access mangled names
    # ada._Person__longevity = False
    # print( ada._Person__longevity )
