import Prob1 as p1
import numpy as np


def test_1():
    t=(-4,1,2,3,5.0)
    y = (1182,2,48,272,2262)
    xtest = list(range(-4,5))
    ytesting = [p1.Problem1(i,t,y) for i in xtest ]
    y_correct_ans = [1182.0, 1134.8, 993.2, 757.2, 426.7999999999, 2.0, 48.0, 272.0, 711.5]
    assert all(list(map(lambda x,y: abs(x-y)<1e-8, ytesting,y_correct_ans)))


def test_2():
    t=(-1,0,0.5,1,2,5/2)
    y = (2,1,0,1,2,3)
    xtest = list(range(-1,2))
    ytesting = [p1.Problem1(i,t,y) for i in xtest ]
    y_correct_ans = [2,1,1]
    assert all(list(map(lambda x,y: abs(x-y)<1e-8, ytesting,y_correct_ans)))
