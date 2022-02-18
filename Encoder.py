vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def pigger(x):
        if x[0] in vowels:
            print(x + "yay")
        else:
            if x[1] in vowels:
                print(x[1:] + x[0] + "ay")
            else:
                print(x[2:] + x[0:2] + "ay")