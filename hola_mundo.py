# Proyecto básico de Python para aprender fundamentos y crear una calculadora simple.
# Estructura clara y profesional para un nivel junior.


def print_title(title):
    print(f"\n--- {title} ---")


# 1. Variables y tipos de dato
print_title("1. Variables y tipos de dato")
name = "Fernando"
age = 39
height = 1.75
is_active = True

print(f"Nombre: {name}")
print(f"Edad: {age}")
print(f"Altura: {height}")
print(f"¿Está activo?: {is_active}")


# 2. Estructuras condicionales
print_title("2. Estructuras condicionales")
score = 85

if score >= 90:
    print(f"Puntuación {score}: Excelente")
elif score >= 70:
    print(f"Puntuación {score}: Aprobado")
else:
    print(f"Puntuación {score}: Necesita revisión")


# 3. Listas
print_title("3. Listas")
qa_tools = ["Postman", "Playwright", "Jira", "TestRail"]
print("Herramientas:", qa_tools)
print("Primera herramienta:", qa_tools[0])


# 4. Bucle for
print_title("4. Bucle for")
for tool in qa_tools:
    print(f"Revisando herramienta: {tool}")


# 5. Funciones
print_title("5. Funciones")

def greet_user(person_name):
    return f"Hola {person_name}, bienvenido al módulo de Python QA."

print(greet_user(name))


# 6. Operaciones aritméticas
print_title("6. Operaciones aritméticas")
num_1 = 10
num_2 = 3

print(f"Suma: {num_1} + {num_2} = {num_1 + num_2}")
print(f"Resta: {num_1} - {num_2} = {num_1 - num_2}")
print(f"Multiplicación: {num_1} * {num_2} = {num_1 * num_2}")
print(f"División: {num_1} / {num_2} = {num_1 / num_2}")
print(f"Módulo: {num_1} % {num_2} = {num_1 % num_2}")
print(f"Potencia: {num_1} ** 2 = {num_1 ** 2}")


# 7. Operadores lógicos
print_title("7. Operadores lógicos")
user_active = True
has_permission = False
is_admin = True

print(f"Usuario activo: {user_active}")
print(f"Tiene permiso: {has_permission}")
print(f"Es administrador: {is_admin}")
print(f"AND: {user_active and has_permission}")
print(f"OR: {user_active or has_permission}")
print(f"NOT: {not has_permission}")
print(f"Acceso completo: {(user_active and is_admin) or (has_permission and is_admin)}")


# 8. Ejemplos de lógica condicional
print_title("8. Ejemplos de lógica condicional")
score = 78
balance = 250
user_age = 17

if score >= 90:
    print(f"Puntuación {score}: Excelente")
elif score >= 70:
    print(f"Puntuación {score}: Aprobado")
else:
    print(f"Puntuación {score}: Necesita revisión")

if balance >= 200 and user_age >= 18:
    print("Puede comprar un producto premium")
elif balance >= 200 and user_age < 18:
    print("Tiene saldo suficiente, pero es menor de edad")
else:
    print("No cumple los requisitos")

if not user_active:
    print("El usuario está inactivo")
else:
    print("El usuario está activo y puede continuar")


# 9. Bucle while
print_title("9. Bucle while")
counter = 1
while counter <= 5:
    print(f"Iteración del bucle: {counter}")
    counter += 1


# 10. Listas y diccionarios
print_title("10. Listas y diccionarios")
colors = ["Rojo", "Azul", "Verde"]
colors.append("Amarillo")
print("Colores:", colors)
print("Segundo color:", colors[1])

person = {
    "nombre": "Fernando",
    "edad": 39,
    "ciudad": "Bogotá"
}
print("Datos de la persona:", person)
print("Nombre de la persona:", person["nombre"])


# 11. Funciones con parámetros
print_title("11. Funciones con parámetros")

def calculate_iva(price, tax_rate=19):
    return price * tax_rate / 100

product_price = 100
print(f"Precio: {product_price} - IVA: {calculate_iva(product_price)}")


def validate_age(age):
    if age >= 18:
        return "Mayor de edad"
    return "Menor de edad"

print(f"Validación de edad: {validate_age(28)}")


# 12. Bucle for con diccionario
print_title("12. Bucle for con diccionario")
for key, value in person.items():
    print(f"{key}: {value}")


# 13. Proyecto: calculadora básica
print_title("13. Proyecto: calculadora básica")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def show_menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def ask_for_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")


def perform_operation(option, a, b):
    if option == "1":
        return add(a, b)
    if option == "2":
        return subtract(a, b)
    if option == "3":
        return multiply(a, b)
    if option == "4":
        return divide(a, b)
    raise ValueError("Operación no válida.")


def get_symbol(option):
    symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }
    return symbols.get(option, "?")


def main():
    while True:
        show_menu()
        option = input("Selecciona una opción: ").strip()

        if option == "5":
            print("Gracias por usar la calculadora.")
            break

        if option not in ["1", "2", "3", "4"]:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        first_number = ask_for_number("Ingresa el primer número: ")
        second_number = ask_for_number("Ingresa el segundo número: ")

        try:
            result = perform_operation(option, first_number, second_number)
            print(f"Resultado: {first_number} {get_symbol(option)} {second_number} = {result}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
