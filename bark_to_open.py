n = int(input())
cards = list(map(int, input().split(" ")))
sereja, dima = 0, 0
left, right = 0, n - 1

for i in range(n):
    if cards[left] > cards[right]:
        points = cards[left]
        left += 1
    else:
        points = cards[right]
        right -= 1
    
    if i % 2 == 0:
        sereja += points
    else:
        dima += points

print(f"{sereja} {dima}")


# bark to open - correct
password = input()
n = int(input())
p0_found, p1_found = False, False
 
for _ in range(n):
    bark = input()
    
    if bark == password:
        break
    
    if bark[0] == password[1]:
        p1_found = True
    if bark[1] == password[0]:
        p0_found = True
        
    if p1_found and p0_found:
        break
 
if bark == password or (p1_found and p0_found):
    print("YES")
else:
    print("NO")


# bark to open  wrong
password = input()
n = int(input())
words = [input() for _ in range(n)]
trial = words[0] + words[0]
left, right = 0, 1
while left < n and right < n:
    trial = words[left] + words[left] + words[right] + words[left]
    if password in trial:
        break
    elif right == n:
        left += 1
        right = left + 1
    else:
        right += 1
if password in trial:
    print("YES")
else:
    print("NO")