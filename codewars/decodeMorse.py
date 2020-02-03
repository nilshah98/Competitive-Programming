MORSE_CODE={'...':'A', '..-':'B', '.--':'C'}
def decodeMorse(morseCode):
    answer=''
    decoded=''
    morseCode=morseCode.replace('   ','x')
    for i in morseCode:
        if i != ' ' and i != 'x':
            answer+=i
        elif i == ' ' and answer != '':
            decoded+=MORSE_CODE[answer]
            answer=''
        elif i=='x' and answer!= '':
            decoded+=MORSE_CODE[answer]
            decoded+=' '
            answer=''
    if answer != '':
        decoded+=MORSE_CODE[answer]
    return decoded

def decodeMorse1(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))