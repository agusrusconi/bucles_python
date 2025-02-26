# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

secuencia_numerica = 0
# for ... in range(....)

# Imprimir el valor de la sumatoria

secuencia = range(inicio, fin+1)
for i in secuencia:
    secuencia_numerica =+ i
    print("secuencia: {}".format(secuencia_numerica))

for i in secuencia:
    sumatoria += i
    print("numero: {} , sumatoria: {}".format(i, sumatoria))

print("la sumatoria de todos los numeros de la secuencia es: {}".format(sumatoria))
print("terminamos!")
