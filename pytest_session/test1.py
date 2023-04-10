
import pytest

@pytest.mark.log
def test_m1():
    print("login system")
    a=10
    b=20
    assert a==b

@pytest.mark.log
def test_m2():
    print("enter the name")
    assert True

@pytest.mark.out
def test_m3():
    print("enter the password")
    assert False

@pytest.mark.out
def test_m4():
    print("enter the captcha")
    assert 12!=10