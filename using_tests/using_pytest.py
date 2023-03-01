# to invoke pytest we do the following
# python -m pytest using_pytest.py 
from collections import namedtuple
t = namedtuple('Tasks', ['summary', 'owner', 'done', 'id'])
t.__new__.__defaults__ = (None, None, False, None)

def test_default(): # here are some PyTest tests
    '''using no parameters should invoke defaults'''
    t1 = t()
    t2 = t(None, None, False, None)
    assert t1 == t2 # I assert they will be the same

def test_member_access():
    '''accessing with dot notation should return values'''
    t2 = t('Learn Python', 'Ethel') 
    # one test in one function - here we are testing ONe thing, the dot-member access of t2
    assert t2.summary == 'Learn Python'
    assert t2.owner   == 'Ethel'
    assert (t2.done, t2.id) == (False, None)

if __name__ == '__main__':
    t1 = t() # an instance of my named tuple, using the defaults
    t2 = t('Learn Python', 'Ethel') # remaining valueswill be defaults
    print(t1, t2)