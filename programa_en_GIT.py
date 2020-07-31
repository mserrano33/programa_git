#numero1=input('ingrese primer numero ')

#numero2=input('ingrese segundo numero ')

 
#if numero1<=numero2:

#    print('el mayor numero entre', numero1, 'y', numero2, 'es ', numero2)


#else:

#    print('el mayor numero entre', numero1, 'y', numero2, 'es ', numero1)
#A=int(input("ingrese un numero\n"))
#B=int(input("ingrese otro numero\n"))
#C=int(input("ingrese un nuemero\n"))
#if(A > B and A > C):
 #print("El numero mayor es " + str(A))
#else:
 #if(B > A and B > C):
  #print("El numero mayor es " + str(B))
 #else:
  #print("El numero mayor es " + str(C))
#l = ["a","b","b"]
#[[x,l.count(x)] for x in set(l)]
#[['a', 1], ['b', 2]]
#dict((x,l.count(x)) for x in set(l))
#{'a': 1, 'b': 2}

vocales = ['a','e','i','o','u']

caracter = input('Ingrese un caracter:')

if caracter in vocales:

  print('El caracter %c es una vocal' %caracter)
else:

  print('El caracter %c es una consonante' %caracter)