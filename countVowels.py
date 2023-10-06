#Given a string, find the total count of vowels present the string
def countVowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count
s=input()
print(countVowels(s))