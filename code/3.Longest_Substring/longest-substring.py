s = "abcdefgggabcdefghijklmnop"

startIndex = 0
substringLength = 1
max = 1

for character in range(1, len(s)):
    substringLength += 1
    for i in range(startIndex, character+1):
        if (s[i] == s[character] and i != character):
            if substringLength > max:
                max = substringLength
            substringLength = 1
            startIndex += 1

print(max)