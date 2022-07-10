def isPalindrome(self, x: int) -> bool:
    listNums = []
    output = False
    while x % 10 != 0:
        listNums.append(x % 10)
        x = int(x / 10)
    for num in range(int(len(listNums)/2)):
        if listNums[num] == listNums[len(listNums)-1-num]:
            output = True
        else:
            output = False
    return output
