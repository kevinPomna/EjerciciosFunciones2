'''• Define una función llamada num_max() que nos devuelva en pantalla el número
mayor entre 4 diferentes enteros. No definas ningún valor a imprimir en caso
de que ambos números sean iguales
'''
def nunMax(a,b,c,d):
    if a>b and a>c and a>d:
      return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c      
    else:
         return d

f = nunMax(10,6,7,8) 
print(f)