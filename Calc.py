def calc ():
    while True: 
        try:
            num1 = float (input('Introduzca primer valor: '))
            num2 = float (input('Introduzca segundo valor: '))
            return num1 , num2
        except ValueError:
            print('Solo se permiten valores numericos! ')
            
def suma (a , b):
    return a + b 

def resta (a , b):
    return a - b

def mult (a , b):
    return a * b

def div (a , b):
    if b == 0:
        print('No se puede dividir entre 0')
    else:
        return a / b
  

while True: 
    print('''Introduzca que operacion desea realizar:
          1) Suma
          2) Resta
          3) Mult
          4) Div
          5) Salir
          ''')
    try:
        eleccion = int(input())
    except ValueError:
        print('Error! **Ingrese valores numericos** Intenta nuevamente!')    
    
    if eleccion == 5:
        print('Hasta pronto!')
        break
    
        print('Ingresa un valor entre 1 y 5')
        continue
    
    num1, num2 = calc()
        
    if eleccion == 1:
        print(' ')
        print('Resultado: ',suma(num1,num2))
        print(' ')
    elif eleccion == 2:
        print(' ')
        print('Resultado: ',resta(num1,num2))
        print(' ')
    elif eleccion == 3:
        print(' ')
        print('Resultado: ',mult(num1,num2))
        print(' ')
    elif eleccion == 4:
        print(' ')
        print('Resultado: ',div(num1,num2))
        print(' ')
    else:
        print('Opcion invalida')
