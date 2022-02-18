vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def pigger():
    while True:
        word =  input("Word please: ")
        if word[0] in vowels:
            print(word + "yay")
        else:
            if word[1] in vowels:
                print(word[1:] + word[0] + "ay")
            else:
                print(word[2:] + word[0:2] + "ay")