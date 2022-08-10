"""
El juego consiste en lo siguiente:
Se debe asignar a cada persona su número mágico, que se obtienen con la siguiente
regla: se suman los dígitos de la fecha de nacimiento y se suman nuevamente los dígitos
del resultado hasta obtener un solo digito como en el siguiente ejemplo:
"""


def obtener_numero_magico(day, month, year):
    resultado = 0
    num_magico = day + month + year

    for num in str(num_magico):
        resultado += int(num)

    if len(str(resultado)) > 1:
        for num in str(resultado):
            resultado += int(num)
        print('El número magico es: ', resultado)
    else:
        print('El número magico es: ', resultado)


mensaje = 'Este programa permite calcular un número magico'
print(mensaje.center(len(mensaje) + 50, '='))

try:
    dia = int(input('Por favor ingrese el dia de su nacimiento: '))
    mes = int(input('Por favor ingrese el mes de su nacimiento (en números 1 - 12): '))
    year = int(input('Por favor ingrese el año de su nacimiento: '))
    obtener_numero_magico(dia, mes, year)
except Exception as e:
    print(f'Ocurrió un error: {e}')
