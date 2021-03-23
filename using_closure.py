# closure refers to the moment we ctually choose to invoke a function

def minions(saying):
    def inner():
        return 'Minions say {}'.format(saying)
    return inner

if __name__ == '__main__':
    a = minions('heheeehee')
    b = minions('hahahaaaa')

    # what have we got?
    print(a, b)

    # # we can call these closures
    print( a() )
    print( b() )
