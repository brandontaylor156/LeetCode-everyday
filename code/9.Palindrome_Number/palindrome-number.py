def isPalindrome(x):
    listNums = []
    output = False

    if x < 0:
        return output
    elif x >= 0 and x < 10:
        output = True
        return output

    while x / 10 != 0:
        listNums.append(x % 10)
        x = int(x / 10)
        
    for num in range(int(len(listNums)/2)):
        if listNums[num] == listNums[len(listNums)-1-num]:
            output = True
        else:
            output = False
            return output
    return output

print(isPalindrome(1000021))