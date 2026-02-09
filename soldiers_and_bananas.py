k, n, w = map(int, input().split())
for i in range(1, w + 1):
    n -= i * k
 
if n < 0:
    print(-1 * n)
else:
    print(0)