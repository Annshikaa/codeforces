import sys
 
def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    rounds = []
    final_scores = {}
 
    for i in range(1, n + 1):
        name, score_str = input_data[i].split()
        score = int(score_str)
        rounds.append((name, score))
        final_scores[name] = final_scores.get(name, 0) + score
    max_score = max(final_scores.values())
    candidates = {name for name, score in final_scores.items() if score == max_score}
    running_scores = {}
    for name, score in rounds:
        running_scores[name] = running_scores.get(name, 0) + score
        if name in candidates and running_scores[name] >= max_score:
            print(name)
            return
 
if __name__ == '__main__':
    solve()