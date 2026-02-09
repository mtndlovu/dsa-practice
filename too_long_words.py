n = int(input())
for _ in range(n):
    word = input()
    word_length = len(word)
    
    if word_length > 10:
        print(word[0] + str(word_length - 2) + word[-1])
    else:
        print(word)