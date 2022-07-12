def convert(s, numRows):
    line = 0
    pl = 1
    output = [""] * numRows
    for i in range(len(s)):
        output[line] += s[i]
        if numRows > 1:
            line += pl
            if line == 0 or line == numRows-1:
                pl *= -1
    outputStr = ""
    for j in range(numRows):
        outputStr+=output[j]
    return outputStr

s = "abcdefghijklmnop"
numRows = 3
print(convert(s, numRows))

