import sys
from math import gcd
 
def rooted(a, b, k, cap):
    if k % a: return 0
    z = k // a
    cnt = 1
    while cnt < cap:
        r = k - b * z
        if r < 0 or r % a: break
        z = r // a
        cnt += 1
    return cnt
 
def longest_free(aa, bb, k):
 
    s = aa + bb
    lim = k // bb
    R = 1
    apw = 1
    bpw = 1
    L = 0
    for m in range(1, 70):
        apw *= aa            # aa^m
        if m > 1: bpw *= bb  # bb^(m-1)
        term = apw // gcd(apw, bpw)
        R = R * (term // gcd(R, term))
        d = gcd(s, R)
        if k % d: break
        Rd = R // d
        z = 0 if Rd == 1 else (k // d) % Rd * pow((s // d) % Rd, -1, Rd) % Rd
        if z > lim: break
        L = m
    return L
 
def solve(n, a, b, k):
    
    if a == b:
        
        return n if k % a == 0 else 0
    L0 = rooted(a, b, k, min(n, 300))
    if L0 >= n:
        return n
    p = L0
    if k % (a + b) == 0:
        
        return n - 1
    aa, bb = (a, b) if a > b else (b, a)   
    L = longest_free(aa, bb, k)
    
    m = n - p - 1
    return p + m - m // (L + 1)
 
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); i = 1; out = []
    for _ in range(t):
        n, a, b, k = int(data[i]), int(data[i+1]), int(data[i+2]), int(data[i+3]); i += 4
        out.append(str(solve(n, a, b, k)))
    sys.stdout.write('
'.join(out) + '
')
 
main()