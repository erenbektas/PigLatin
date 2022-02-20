import string

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def pigger(x):

    sentence = x.split()
    leng = len(sentence)
    if leng == 1:

        if x[0] in vowels:
            return x + "yay"
        else:
            if len(x) > 1:
                if x[1] in vowels:
                    return x[1:] + x[0] + "ay"
                else:
                    return x[2:] + x[0:2] + "ay"
            else:
                return x + "ay"

    else:
        newsent = []
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
                newword = n + "ay"
                newsent.append(newword)
        return newsent