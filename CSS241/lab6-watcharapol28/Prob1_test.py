import Prob1 as p1;
import math

def test_1():
    eps =1e-4
    ans = 0.7468071
    f = lambda x: math.exp(-(x**2))
    assert ans-eps <= p1.recursive_trapezoid(f,0,1,5)<= ans+eps


