def firstUniqChar(s):
    char_count={}
    for char in s:
        char_count[char]=char_count.get(char, 0)+ 1
    for i in range(len(s)):
        if char_count[s[i]]==1:
            return i
    return -1
s= str(input("please enter input: "))    
print(firstUniqChar(s))    