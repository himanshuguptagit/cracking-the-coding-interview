
testcases = [
    ["waterbottle", "erbottlewat"],
    ["waterbottle", "erbottlewate"],
    ["waterbottle", "erbottlewaa"],
]

# function to check rotation
def isRotation(str1, str2):

    if(len(str1)!= len(str2)):
        return False

    temp = str1 + str1
    if(temp.find(str2) > -1):
        return True
    
    return False

print("Is rotation: ")
for t in testcases:
    result = isRotation(t[0], t[1])       
    print(f"{t[0]}, {t[1]} : {result}")

