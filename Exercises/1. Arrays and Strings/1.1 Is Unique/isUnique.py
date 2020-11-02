
testcases = [
    "Hello World",
    "Lorem",
    "Loremm",
    "LLorem",
]


# Function to find if string contains all unique characters without Any data strucuture
# Time: O(n2) Space: O(1)
def isUnique(str):
    for i in range(0,len(str)-1):
        for j in range(i+1, len(str)):
            if(str[i] == str[j]):
                return False

    return True


print("Is Unique ")
for t in testcases:
    result = isUnique(t)        
    print(f"{t}: {result}")

