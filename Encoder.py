import string
vowels = "a", "e", "i", "o", "u", "ü", "ö", "ı" "A", "E", "I", "O", "U", "Ü", "Ö", "İ"
puncs = "!", ".", ",", ":", ";", "?"

def pigger(x):
    newsent = []     #list of piglatin words

    low = x.lower()
    lowlist = low.split()
    for n in lowlist:

        if n[-1] in puncs:     #if any of the words is ending with a "puncs" list element
            if n[0] in vowels:
                newword = n[:-1] + "yay" + n[-1]
                newsent.append(newword)
            elif len(n) > 1 and n[1] in vowels:
                newword = n[1:-1] + n[0] + "ay" + n[-1]
                newsent.append(newword)
            else:
                newword = n[2:-1] + n[0:2] + "ay" + n[-1]
                newsent.append(newword)

        else:                  #if any of the words is not ending with a "puncs" list element
            if n[0] in vowels:
                newword = n + "yay"
                newsent.append(newword)
            elif len(n) > 1 and n[1] in vowels:
                newword = n[1:] + n[0] + "ay"
                newsent.append(newword)
            else:
                newword = n[2:] + n[0:2] + "ay"
                newsent.append(newword)

    if x[0][0] in string.ascii_uppercase:
        first = newsent[0] + " "
        final = " ".join(newsent[1:])
        return first.capitalize() + final
    else:
        final = " ".join(newsent)
        return final