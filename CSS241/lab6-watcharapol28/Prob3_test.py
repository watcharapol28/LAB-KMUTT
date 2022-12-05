import Prob3 as p3;
import math

def test_1():
    eps =1e-4
    ans = 0.7468071
    f = lambda x: math.exp(-(x**2))
    assert ans-eps <= p3.adaptive_simpson(f,0,1,eps,1,7)<= ans+eps
