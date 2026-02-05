
from collections import defaultdict
 
t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    
    dist_health = defaultdict(int)
    for i, d in enumerate(x):
        dist_health[abs(d)] += a[i]
    
    sorted_dist = sorted(dist_health)
    accumulated_health, possible = 0, True
    for d in sorted_dist:
        accumulated_health += dist_health[d]
 
        if k * d < accumulated_health:
            print("NO")
            possible = False
            break
    if possible:
        print("YES")