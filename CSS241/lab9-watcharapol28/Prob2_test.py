import Prob2 as p2
import numpy as np

def test_1():
    t=(-4,1,2,3,5.0)
    y = (1182,2,48,272,2262)
    xtest = list(range(-4,5))
    ytesting = [p2.Problem2(i,t,y) for i in xtest ]
    y_correct_ans = [1182.0, 835.9733333333334, 517.4533333333334, 253.9466666666667, 72.96000000000001, 2.0, 48.0, 272.0, 1075.9833333333333]
    assert all(list(map(lambda x,y: x-y<1e-8, ytesting,y_correct_ans)))


def test_2():
    t=(-1,0,1)
    y= (1,2,-1)
    xtest = np.arange(-1,1,0.5)
    ytesting = [p2.Problem2(i,t,y) for i in xtest ]
    y_correct_ans = [1.0, 1.875, 2.0, 0.875]
    assert all(list(map(lambda x,y: x-y<1e-8, ytesting,y_correct_ans)))
