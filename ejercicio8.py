'''Define una función que permita multiplicar los números de una lista y sumar
sus resultados.
'''
def mul (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    print (multiplicacion)
mul([4,2,6])