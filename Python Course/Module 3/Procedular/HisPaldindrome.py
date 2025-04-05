

def isPaldindrome(str):
    startIndex = 0
    endIndex = len(str) -1
    for x in str:
        if str[startIndex] != str[endIndex]:
            startIndex +=1
            endIndex -=1
            return False
    return True
print(isPaldindrome('racecar'))