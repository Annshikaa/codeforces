import sys
 
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]; idx += n
        s = 0
        best = float('inf')
        res = []
        for j in range(1, n+1):
            s += int(a[j-1])
            cur = s // j
            if cur < best:
                best = cur
            res.append(best)
        out.append(' '.join(map(str, res)))
    sys.stdout.write('
'.join(out) + '
')
 
main()