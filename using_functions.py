# args and kwargs allow handling function parameters
# we use args for positionl/ordinal arguments and kwargs for keyword arguments
def myFn(*args): # *args will make a tuple containing zero or more arguments passed in
    # one-arg outcome
    if(len(args)== 1):
        return 'one argument: {}'.format(args[0])
    # two-arg outcome
    if(len(args)== 2):
        return 'two arguments: {} {}'.format(args[0], args[1])
    # else
    return 'more than two arguments: {}'.format(args)

def otherFn(*args, **kwargs): # the keyword arguments will be in a dictionary called kwargs
    print(args)  # see the tuple
    print(kwargs)# see the dict

if __name__ == '__main__':
    print( myFn('weeble') )
    print( myFn('weeble', 'wooble') )
    print( myFn('weeble', True, False, [4,3,2], {'name':'value'}) )
    otherFn('a', False, [], k=(1,), n={})
    otherFn(n=True, x=4, diddledoo=True, result=myFn('coffee'))