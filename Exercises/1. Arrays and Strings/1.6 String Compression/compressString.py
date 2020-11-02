
testcases = [
    "aabcccccaaa",
    "abc"
]


# function to compress tring
def compressString(str1):
    
    compressed = ""
    i=0

    selected = str1[i]
    compressed+= selected
    count = 1

    while(i < len(str1)):
        if(str1[i] == selected):
            count += 1
        else:
            compressed += str(count)
            selected = str1[i]
            compressed+= selected
            count = 1
        i += 1
    compressed += str(count)


    if(len(compressed) < len(str1)):
        return compressed
    else: 
        return str1

  
print("Compressed: ")
for t in testcases:
    result = compressString(t)       
    print(f"{t} : {result}")

