vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def pigger(x):
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