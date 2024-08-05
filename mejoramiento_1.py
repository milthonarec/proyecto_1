# ingresa el codigo para una calculadora con con funciones e implementacion de docstring
def suma(a, b):
    """
    Suma dos números.

    :param a: El primer número.
    :param b: El segundo número.
    :return: La suma de a y b.
    """
    return a + b

def resta(a, b):
    """
    Resta el segundo número del primero.

    :param a: El primer número.
    :param b: El segundo número.
    :return: La resta de a menos b.
    """
    return a - b

def multiplicacion(a, b):
    """
    Multiplica dos números.

    :param a: El primer número.
    :param b: El segundo número.
    :return: El producto de a y b.
    """
    return a * b

def division(a, b):
    """
    Divide el primer número por el segundo.

    :param a: El primer número.
    :param b: El segundo número.
    :return: El cociente de a dividido por b.
    :raises ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b

def calculadora():
    """
    Ejecuta una calculadora básica que permite al usuario elegir una operación
    y proporciona dos números para realizar dicha operación.
    """
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            opcion = int(input("Ingrese su opción (1/2/3/4): "))
            if opcion not in [1, 2, 3, 4]:
                raise ValueError("Opción inválida, por favor ingrese 1, 2, 3, o 4.")
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if opcion == 1:
        print(f"El resultado de la suma es: {suma(num1, num2)}")
    elif opcion == 2:
        print(f"El resultado de la resta es: {resta(num1, num2)}")
    elif opcion == 3:
        print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
    elif opcion == 4:
        try:
            print(f"El resultado de la división es: {division(num1, num2)}")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    calculadora()
