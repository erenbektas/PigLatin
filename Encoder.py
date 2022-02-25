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
                if n[1] in puncs:
                    newword = n[0] + "ay" + n[1]
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

    raw_input_list = x.split() #list of words in input
    for n in raw_input_list:
        pos_n = raw_input_list.index(n) #for position of each words of the input
        if n[0] in string.ascii_uppercase: #if the first letter of that word is uppercase in input
            newsent[pos_n] = newsent[pos_n].capitalize() #first letter of the corresponding element will also start with an uppercase

    final = " ".join(newsent)
    print(newsent)
    return final
