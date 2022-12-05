import Prob2 as p2;
import math

def test_1():
    eps =1e-4
    ans = 0.7468071
    f = lambda x: math.exp(-(x**2))
    assert ans-eps <= p2.romberg(f,0,1,5)<= ans+eps
