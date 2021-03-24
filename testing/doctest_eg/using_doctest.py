import doctest

def cube(x):
    '''
    This function returns the cube of any number
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    '''
    return x*x*x

def squares(a,b):
    '''
    Returns a list of all the squares in range a...b inclusive
    >>> squares(1,10) # doctest:+ELLIPSIS
    [1, 4, ..., 100]
    '''
    answer = []
    for i in range(a,b+1):
        answer.append(i*i)
    return answer

def square_it(x):
    '''
    return the square of any number less than ten
    >>> square_it(3)
    9
    >>> square_it(16) # we expect an exception
    Traceback (most recent call last):
    ...
    ValueError: input too large
    '''
    if x>9:
        raise ValueError('input too large')
    else:
        return x*x

if __name__ == '__main__':
    # exercise the code
    cube(3) # 27
    # doctest.testmod(verbose=True) # verbose will show the details
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True)