genome = "ACTG"
n = int(input())
s = input()
min_diff = 104
left, right = 0, 3

while right < len(s):
    substring = s[left:right+1]
    diff = 0
    for i in range(4):
        tmp = abs(ord(genome[i]) - ord(substring[i]))
        diff += min(tmp, 26 - tmp)

    if diff < min_diff:
        min_diff = diff
    left += 1
    right += 1

print(min_diff)