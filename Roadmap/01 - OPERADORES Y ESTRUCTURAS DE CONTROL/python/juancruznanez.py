# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

'''
Operadores
'''

# Operadores aritmeticos 
print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"Resto: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 10 = {10 == 10}")
print(f"Desigualdad: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 - 3 == 7 and 10 + 3 == 13 = {10 - 3 == 7 and 10 + 3 == 13}")
print(f"OR | : 10 + 3 == 13 and 10 + 5 == 14 = {10 + 3 == 13 or 10 + 5 == 14}")
print(f"NOT ! : 10 > 20 = {10 > 20}")

# Operadores y asignación 
My_variable = 10
print(My_variable)
My_variable += 10 # Suma y asignación
print(My_variable)
My_variable -= 5 # Resta y asignación
print(My_variable)
My_variable *= 10 # Multiplicación y asignación 
print(My_variable)
My_variable /= 2 # División y asignación
print(My_variable)
My_variable %= 2 # Resto y asignación
print(My_variable)
My_variable **= 2 # Exponente y asignación
print(My_variable)
My_variable //= 3 # División entera y asignación
print(My_variable)

# Operadores de identidad
my_new_variable = My_variable
print(f"My_variable is my_new_variable es {My_variable is my_new_variable}")
print(f"My_variable is not my_new_variable es {My_variable is not my_new_variable}")

# Operadores de pertenencia
print(f"'u' in 'juancruz' = {'u' in 'juancruz'}")
print(f"'g' not in 'juancruz' = {'b' not in 'juancruz'}")

# Operadores de bit (todas las operaciones las realiza en lenguaje de bit)
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "JuanCruz"

if my_string == "Juan":
    print("my_string es 'Juan'")
elif my_string == "JuanCruz":
    print("my_string es 'JuanCruz'")
else:
    print("my_string no es 'Juan' ni 'JuanCruz'")

# Iterativas 

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)