# errores
errorData = -666
error1 = -3
error2 = -5
error3 = -9


def func1(x):
    if (x == str(x)):
        indice = 0
        contador = 0
        while indice < len(x):
            caracter = x[indice]
            if (caracter.islower() is True):
                indice += 1
            else:
                contador += 1
                indice += 1
        if (contador == 0):
            return x.upper()
        else:
            return error1
    else:
        return errorData


def func2(b):
    if (b == str(b)):
        if (b.find('w') >= 0):
            return "Se encontró el string 'w'"
        else:
            return "No se encontró el string 'w'"
    else:
        return errorData


def func3(c, d):
    if (c >= 0 and d >= 0 and c > d):
        return c - d
    else:
        return error3
