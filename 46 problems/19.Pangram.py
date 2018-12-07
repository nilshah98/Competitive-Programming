#Q19 Pangram
def is_pangram(phrase):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    phrase=phrase.lower()
    for i in alphabets:
        if i not in phrase:
            return i, False
    else:
        return True