import pytest

@pytest.mark.log

def test_a1():
    print("access the folder")
    assert True

@pytest.mark.out
def test_a2():
    print("folder open")
    assert False