def convert(s, numRows):
    line = 0
    # direction 1 goes down, direction -1 goes up at zig zag angle
    lineDirection = 1
    output = [""] * numRows
    for i in range(len(s)):
        output[line] += s[i]
        if numRows > 1:
            line += lineDirection
            # if line reaches last row index in given direction, switch directions
            if line == 0 or line == numRows-1:
                lineDirection *= -1
    print(output)
    outputStr = ""
    for j in range(numRows):
        outputStr+=output[j]
    return outputStr

s = "abcdefghijklmnop"
numRows = 9
print(convert(s, numRows))

