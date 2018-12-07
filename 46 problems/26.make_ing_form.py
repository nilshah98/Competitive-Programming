
#Q26
def make_ing_form(phrase):
    vowel=['a','e','i','o','u']
    exception=['be','see','flee','knee']
    x=len(phrase)
    if phrase[x-3] not in vowel and phrase[x-2] in vowel and phrase[x-1] not in vowel:
        phrase=phrase+phrase[x-1]+'ing'
    elif phrase[x - 2] + phrase[x - 1] == 'ie' and phrase not in exception:
        phrase=phrase+'1'
        phrase=phrase.replace('ie1','ying')
    elif phrase[x-1]=='e' and phrase not in exception:
        phrase=phrase+'2'
        phrase=phrase.replace('e2','ing')
    else:
        phrase=phrase+'ing'
    return phrase
