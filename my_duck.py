# we do not have to use @property decorators for getter/setter methods

class Duck():
    # class property
    count = 0
    def __init__(self, name):
        self.__name = name
        Duck.count += 1
    # we can declare class methods
    @classmethod
    def how_many(cls):
        print('Duck class has {} instances'.format(cls.count))
    @staticmethod
    def info(): # NOTE static methods do NOT need 'self'
        print('this is the Duck class')
    def get_name(self):
        return self.__name
    def set_name(self, newName):
        self.__name = newName
    name = property(get_name, set_name)

if __name__ == '__main__':
    d = Duck('Donald')
    d2 = Duck('Mallard')
    d.name = 'Howard' # if we DON'T have a name property, this just creates a new property called .name
    print(d.get_name())
    Duck.info() # 
    print(Duck.how_many()) # calls the class method