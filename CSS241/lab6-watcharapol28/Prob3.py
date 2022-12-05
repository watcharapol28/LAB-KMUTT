def adaptive_simpson(f,a,b,eps,level, level_max):
    level = level + 1
    h = b -a
    c = (a + b)/2
    simp1 = h * (f(a) + 4*f(c) + f(b))/6
    d = (a + c)/2
    e = (c  + b)/2
    simp2 = h * (f(a) + 4*f(d) + 2*f(c) + 4*f(e) + f(b))/12
    if level >= level_max:
        ans = simp2
    else:
        if abs(simp2 - simp1) < 15 * eps:
            ans = simp2 + (simp2 - simp1)/15
        else:
            leftsimp = adaptive_simpson(f,a,c,eps/2,level, level_max)
            rightsimp = adaptive_simpson(f,a,b,eps/2,level, level_max)
            ans = (leftsimp + rightsimp)
    return ans
