import pytest



def test_case01(login):
    print("test_cese1, 要登陆")
    pass



def test_cese02():
    print("test_case2， 不需要登陆")
    pass

def test_cese03():
    print("test_case3， 不需要登陆")
    pass

def test_case04(login):
    print("test_cese4, 要登陆")
    pass

if __name__ == '__main__':
    pytest.main()