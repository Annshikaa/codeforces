import sys
 
input = sys.stdin.readline
 
t = int(input())
answers = []
 
for _ in range(t):
    s = input().strip()
    n = len(s)
 
    # suffix count of 1s and 3s
    suffix13 = [0] * (n + 1)
 
    for i in range(n - 1, -1, -1):
        suffix13[i] = suffix13[i + 1]
        if s[i] == '1' or s[i] == '3':
            suffix13[i] += 1
 
    prefix2 = 0
    max_keep = 0
 
    for i in range(n + 1):
        max_keep = max(max_keep, prefix2 + suffix13[i])
 
        if i < n and s[i] == '2':
            prefix2 += 1
 
    answers.append(str(n - max_keep))
 
print("
".join(answers))