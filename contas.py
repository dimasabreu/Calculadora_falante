

def somar(num1, num2):
    soma = num1 + num2
    resultado = (f"A soma dos numeros é {soma}")
    return resultado


def subtrair(num1, num2):
    sub = num1 - num2
    resultado = (f"A subtração dos numeros é {sub}")
    return resultado


def multiplicar(num1, num2):
    mult = num1 * num2
    resultado = (f"A multiplicação dos numeros é {mult}")
    return resultado


def dividir(num1, num2):
    div = num1 / num2
    resultado = ("A divisão dos numeros é %.2f" % (div))
    return resultado


def porcentagem(num1, num2):
    por = (num1 / 100) * num2
    resultado = ("%d porcento de %d é %.2f" % (num1, num2, por))
    return resultado


def exponenciacao(num1, num2):
    expo = num1 ** num2
    resultado = (f"{num1} elevado a {num2} é {expo}")
    return resultado

#def primo():
