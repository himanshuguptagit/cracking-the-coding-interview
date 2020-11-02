
testcases = [
    ["hello", "helo"],
    ["hello", "hellow"],
    ["hello", "hlleo"],
    ["hello", "hellw"],
    ["hello", "wello"],
    ["hello", "hexco"],
]


# Function to find if strings are permutation of each other
def isPermutation(str1, str2):

    if(len(str1) != len(str2)):
        return False

    if(''.join(sorted(str1)) == ''.join(sorted(str2))):
        return True

    return False


print("Is Permutations ")
for t in testcases:
    result = isPermutation(t[0], t[1])       
    print(f"{t[0]}, {t[1]}: {result}")

