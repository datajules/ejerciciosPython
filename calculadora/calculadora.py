import dibujo

# 1. Funciones matemáticas
def calculadora(num1,operacion,num2):
    if operacion == "+":
        return f"{num1} {operacion} {num2} = {round(num1 + num2,2)}"
    elif operacion == "-":
        return f"{num1} {operacion} {num2} = {round(num1 - num2,2)}"
    elif operacion == "*":
        return f"{num1} {operacion} {num2} = {round(num1 * num2,2)}"
    elif operacion == "/":
        return f"{num1} {operacion} {num2} = {round(num1 / num2,2)}"

# 2. Interfaz gráfica


# 3. Interacción con el usuario
print("Calculadora")
print("Bienvenido a la calculadora")   
print("Por ingrese el primer número")
num1 = float(input()) 
print("Por ingrese la operación: +, -, *, /")
operacion = input()
print("Por ingrese el segundo número")
num2 = float(input()) 
display = calculadora(num1,operacion,num2)
print(dibujo.creando_dibujo(display))