import string
vowels = "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"

def pigger(x):
    newsent = []     #list of piglatin words

    low = x.lower()
    lowlist = low.split()
    for n in lowlist:
        if len(n) > 1:
            if n[0] in vowels:
                newword = n + "yay"
                newsent.append(newword)
            elif n[1] in vowels:
                newword = n[1:] + n[0] + "ay"
                newsent.append(newword)
            else:
                newword = n[2:] + n[0:2] + "ay"
                newsent.append(newword)
        else:
            if n[0] not in vowels:
                newword = n + "ay"
                newsent.append(newword)
            else:
                newword = n + "yay"
                newsent.append(newword)
    if x[0][0] in string.ascii_uppercase:
        first = newsent[0] + " "
        final = " ".join(newsent[1:])
        return first.capitalize() + final
    else:
        final = " ".join(newsent)
        return final