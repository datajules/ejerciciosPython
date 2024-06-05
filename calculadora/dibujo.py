
def creando_dibujo(display):
    #display = f'''{num1} {operacion} {num2} = {resultado}'''
    dibujo_display = f'''| |                 | |'''
    largo_dibujo_display = len(dibujo_display)
    largo_di = len(display)
    diferencia= f'''{" "*(largo_dibujo_display - largo_di-3-4)}'''
    calculadora_dibujo = f'''
 _____________________
|  _________________  |
| | {display}{diferencia}| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
    return(calculadora_dibujo)


#print(creando_dibujo(5,3,"+",8))

