'''Define una función que nos devuelva True si al darle una vocal mayúscula nos
devuelva False, mientras que si es minúscula sea True
'''
def vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print(True)
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
           print(False)
vocal('E')

