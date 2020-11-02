
testcases = [
    ["Mr John Smith    ", 13],
]


# string to replace white space in betwwen words with %20 using extra spaces at end
def urlify(str, stringLength):
    fillPointer = len(str)-1
    pointer = stringLength-1
    arr = list(str)

    for i in range(pointer,-1,-1):

        if(arr[i] == ' '):
            arr[fillPointer] = "0"
            arr[fillPointer-1] = "2"
            arr[fillPointer-2] = "%"
            fillPointer-=3
        else:
            arr[fillPointer] = arr[i]
            fillPointer -= 1

    return "".join(arr)


print("Urlify ")
for t in testcases:
    result = urlify(t[0], t[1])       
    print(f"{t[0]}: {result}")

