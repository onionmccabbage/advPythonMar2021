import my_concrete

# declare our own meta class
class DocChecker(type):
    ''' check that classes do have docstring'''
    def __init__(cls, name, bases, dic):
        type.__init__(cls, name, bases, dic)
        try:
            if not cls.__doc__:
                raise TypeError('no help available')
        except Exception:
            print('no docstring available')

# use the meta class
class MyType(metaclass=DocChecker):
    '''here is some documentation'''
    pass

class MyType2(metaclass=DocChecker):
    pass