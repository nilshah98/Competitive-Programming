
#Q25
def make_3sg_form(phrase):
    x=len(phrase)
    esform=['o','ch','s','sh','x','z']
    if phrase[x-1]=='y':
        phrase=phrase.replace(phrase[x-1],'ies')
    elif phrase[x-1] in esform:
        phrase=phrase+'es'
    elif phrase[x-2]+phrase[x-1] in esform:
        phrase = phrase + 'es'
    else:
        phrase=phrase+'s'
    return phrase
