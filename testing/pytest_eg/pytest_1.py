# we might need to pip install pytest

def test_passing():
    assert (1,2,3) == (1,2,3) # same ordinal values

# def test_failing():
#     assert (1,2,3) == (3,2,1) # different ordinal values

def test_true():
    x = 'this is truly truthful'
    y = ''
    assert x
    assert not y # or assert y == False