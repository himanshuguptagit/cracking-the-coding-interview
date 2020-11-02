
testcases = [
    ["pale","ple"],
    ["pales","pale"],
    ["pale","bale"],
    ["pale","bae"],

]

def stringMismatchCount(str1, str2):
    mismatchCount = 0
    for i in range(0, len(str1)):
        if(str1[i] != str2[i]):
            mismatchCount += 1
    
    return mismatchCount

def unevenStringMismatchCount(str1, str2):
    #len str1 < len str2
    mismatchCount =0
    i, j = 0,0

    while(i < len(str1) and j < len(str2)):
        if(str1[i] == str2[j]):
            i+=1
            j+=1
        else:
            mismatchCount +=1
            j+=1

    
    return mismatchCount
    

# function to find if string has a Palindrome Permutation
def isOneAway(str1, str2):

    res = False
    count = 0

    if(len(str1) == len(str2)):
        count = stringMismatchCount(str1, str2)

    elif( ((len(str1) - len(str2)) == 1) or ((len(str1) - len(str2)) == -1) ):
        if(len(str1)< len(str2)):
            count = unevenStringMismatchCount(str1, str2)
        else:
            count = unevenStringMismatchCount(str2, str1)

    if(count<=1):
        res = True
    return res
  
print("IS One away: ")
for t in testcases:
    result = isOneAway(t[0], t[1])       
    print(f"{t[0]}, {t[1]}: {result}")

