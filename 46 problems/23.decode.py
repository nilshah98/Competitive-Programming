#Q23
def decode(phrase):
    cipher_key={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y' ,'m':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
    decoded=''
    phrase= phrase.lower()
    for i in phrase:
        if i in cipher_key:
            decoded= decoded + cipher_key[i]
        else:
            decoded= decoded + i
    return decoded