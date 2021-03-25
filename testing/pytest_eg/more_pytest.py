from collections import namedtuple

# we can declare a 'Task' named tuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

# write some pytest tests to exercise the named tuple
# invoke pytest like this: pytest -v more_pytest.py
def test_default():
    '''using no parameters should invoke the defaults'''
    t1 = Task() # invoke defaults
    t2 = Task(None, None, False, None) # explcitly setting values
    assert t1 == t2

def test_member_access():
    '''Check the dot-notation access to members of the named tuple'''
    t = Task('buy milk', 'Becky')
    assert t.summary == 'buy milk'
    assert t.owner == 'Becky'
    assert (t.done, t.id) == (False, None)
