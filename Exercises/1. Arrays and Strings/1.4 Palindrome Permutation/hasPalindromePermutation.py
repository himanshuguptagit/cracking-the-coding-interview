
testcases = [
    "tactcoa",
    "tactcoaa",

    "aab",
    "aabb",

]


# function to find if string has a Palindrome Permutation
def hasPalindromPermutation(str):

    noOfAllowedOdds = 0
    isOdd = len(str)%2

    if(isOdd):
        noOfAllowedOdds = 1

    charIsOdd= { }
    oddCount = 0

    for i in range(0, len(str)):
        
        if(str[i] not in charIsOdd.keys()):
            charIsOdd[str[i]] = 1
        else:
            charIsOdd[str[i]] = 1 - charIsOdd[str[i]] 
    
    
    for value in charIsOdd.values(): 
        oddCount += value

    if(oddCount == noOfAllowedOdds):
        return True

    return False
  
print("hasPalindromPermutation ")
for t in testcases:
    result = hasPalindromPermutation(t)       
    print(f"{t}: {result}")

