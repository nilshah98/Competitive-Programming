#Palindrome Q18
def palindrome(phrase):
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", " "]
    for i in punctuation:
        phrase=phrase.replace(i,'')
    x=''
    for i in range(len(phrase),0,-1):
        x+=phrase[i-1]
    if x==phrase:
        return True
    else:
        return False