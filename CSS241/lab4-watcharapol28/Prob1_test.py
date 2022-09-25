import Prob1 as p1;

def test_1():
    eps =1e-6
    ans = 192.0
    x = 2
    assert ans-eps <= p1.richardson_diff(x) <= ans+eps

def test_2():
    eps =1e-6
    ans = 1458.0
    x = 3
    assert ans-eps <= p1.richardson_diff(x)  <= ans+eps
