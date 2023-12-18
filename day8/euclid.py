# Stolen from https://brilliant.org/wiki/extended-euclidean-algorithm/
# I didn't actually need this because all
# the phase offsets in the problem == period
# but might come in handy
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y