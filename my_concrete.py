from my_abstract import Shape

class Circle(Shape):
    def __init__(self, name):
        self.__name = name # __ is mangling the property - cannot easily be seen outside the class
    def display(self):
        print('Circle', self.name)
    @property
    def name(self): # a getter mehod
        return self.__name # we must implement these methods
    @name.setter # a setter method
    def name(self, newName):
        self.__name = newName

if __name__ == '__main__':
    c = Circle('my_circle')
    c.__name = 'altered' # does NOT alter the name property
    c.name = 'changed'
    c.display()