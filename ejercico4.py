''' Define una función llamada num_min() que nos devuelva en pantalla el número
menor entre 3 diferentes enteros. En caso de que todos sean iguales imprime en
pantalla un mensaje indicándolo.
'''
def nunMin(a,b,c,):
    if a<b and a<c:
      return a
    elif b<a and b<c:
        return b
    elif c<a and c<b: 
        return c      
    else:
         print("Todos son iguales")

f = nunMin(5,10,10,) 
print(f)