word = "wateftruck"

## Either
''''
a1= word[0] == word[6]
a2=word[1] == word[5]
a3=word[2] == word[4]
print(a1,a2,a3)'
'''
## etc
## Or use procedular steps to break it down into smaller steps
def isPalindrome(checkable_word):
    start_index = 0
    end_index = len(checkable_word) -1
    while start_index != end_index:
        if checkable_word[start_index] == checkable_word[end_index]:
            start_index+=1
            end_index-=1
        else:
            #raise Exception("Is not a Palindrome")
            #print("Is not a Palindrome")
            #exit()
            return False
    return True
print(isPalindrome(word))