from functions import f

def test_f_of_6_equals_7():
    assert f(6) == 7

def test_f_of_41_equals_42():
    assert f(41) == 42

def test_f_of_neg1_equals_0():
    assert f(-1) == 0
