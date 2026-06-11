import sys
 
def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        out.append(' '.join(str(n + k) for k in range(1, n + 1)))
    sys.stdout.write('
'.join(out) + '
')
 
main()