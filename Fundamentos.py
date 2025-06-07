#Archivo para operadores aritmeticos

def Suma(a,b):
    return a+b

def Resta(a,b):
    return a - b

def nuevoTema(tema):
    return f"\n---------- {tema} ----------\n"

if __name__ == "__main__":

    print(nuevoTema("Operadores aritmeticos"))
    print("Operador suma, 5 + 6 = ",Suma(5,6))
    print("Operador resta, 5 - 6 = ",Resta(5,6))
    print("Operador Multiplicacion, 5 * 6 = ",5*6)
    print("Operador Division, 5 / 6 = ",5/6)
    print("Operador Division entera, 5 // 6 = ",5//6)
    print("Operador Módulo, 5 % 6 = ",5%6)
    print("Operador Exponente, 5 ** 6 = ",5**6)
    print("Operador +, +5 = ",+5)
    print("Operador -, -5 = ",-5)

    ''' Comentario de varias lineas
    Línea 2 
    Etc....'''

    print(nuevoTema("Operadores lógicos")) 
    print("Operador not")
    print("not True:", not True)
    print("not False:", not False)

    print("Operador and")
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)

    print("Operador or")
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)


    print(nuevoTema("Operadores de comparacion "))
    x = 8
    y = 8
    print(x == y)
    print(x != y)
    print(x > y)
    print(x < y)
    print(x >= y)
    print(x <= y)


    print(nuevoTema("Variables"))
    a,b,c = 1,4,"Bienvenido"
    print(a)
    print(b)
    print(c)

    print(nuevoTema("Enteros"))
    x = 569
    y = 54684
    z = 7894165465464620101846168797605654064684046846046846804646546
    b = 0b1111
    h = 0xFF
    #print(x*y*z)
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(b,type(b))
    print(h,type(h))


    print(nuevoTema("Flotantes"))
    q = 985.63
    w = 1420.2
    print(q,type(q))
    print(w,type(w))


    print(nuevoTema("Complejos"))
    q = 3 + 2j
    w = -63j
    print(q,type(q))
    print(w,type(w))

