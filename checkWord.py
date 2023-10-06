def checkWord(s,word):
    if word in s:
        return True
    return False
s=input()
word=input()
print(checkWord(s,word))