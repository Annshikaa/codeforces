import sys
 
def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(data[pos]); pos += 1
        vals = [int(x) for x in data[pos:pos+n]]; pos += n
 
        # Candidate targets = reachable set of one element (any works; use min for short chain).
        # Valid because a common target must lie in every element's reachable set.
        cx = min(vals)
        cand = {}
        v = cx; c = 0
        while v not in cand:
            cand[v] = c
            v = v + 1 if (v & 1) else v >> 1
            c += 1
        idxof = {g: i for i, g in enumerate(cand)}
 
        totals = [0] * len(cand)
        counts = [0] * len(cand)
 
        for x in vals:
            v = x; c = 0
            local_seen = set()
            while v not in local_seen:
                local_seen.add(v)
                j = idxof.get(v)
                if j is not None:
                    totals[j] += c
                    counts[j] += 1
                v = v + 1 if (v & 1) else v >> 1
                c += 1
 
        best = 1 << 62
        for i in range(len(cand)):
            if counts[i] == n and totals[i] < best:
                best = totals[i]
        out.append(str(best))
    sys.stdout.write('
'.join(out) + '
')
 
main()