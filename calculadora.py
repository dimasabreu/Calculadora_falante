import pyttsx3
import speech_recognition as sr
from contas import *

# Parte de inicializacao

print("-"*40)
print("Bem-vindo a Calculadora falante!\n", end="")
print("ESPERE SEMPRE UMA CONFIRMAÇÃO VISUAL\n", end="")
print("Para comecar diga: Abrir calculadora")
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    ini = r.recognize_google(audio, language="pt-BR")
    if ini == "Abrir calculadora":
        print("Calculadora iniciada!")
        engine = pyttsx3.init()
        engine.say("Bem vindo, vou listar abaixo as opcões disponiveis:")
        engine.runAndWait()
        print("OPÇÕES:\nSomar\nSubtrair\nMultiplicar\nDividir", end="")
        print("\nPorcentagem\nExponenciação")
        engine = pyttsx3.init()
        engine.say("Fale o que você gostaria de fazer")
        engine.runAndWait()
        print("Fale o que voce gostaria de fazer:")
        audio = r.listen(source)
        opcao = r.recognize_google(audio, language="pt-BR")
        if opcao == "Fechar":
            exit()
        else:
            print("Voce escolheu", opcao.upper(), "!")
    else:
        engine = pyttsx3.init()
        engine.say("Não entendi")
        engine.runAndWait()
        exit()
print("-"*40)


"""r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    opcao = r.recognize_google(audio, language="pt-BR")"""


# func para captar audio


def captacao():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.say("Fale o numero")
        engine.runAndWait()
        print("Fale o numero:")
        audio = r.listen(source)
        num = r.recognize_google(audio, language="pt-BR")
        return (num)


# func para falar o resultado


def fala():
    engine = pyttsx3.init()
    engine.say(falando)
    engine.runAndWait()


# comecando o programa

if opcao == "somar":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(somar(num1, num2))
    falando = (somar(num1, num2))
    fala()
    print("-"*40)

elif opcao == "subtrair":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(subtrair(num1, num2))
    falando = (subtrair(num1, num2))
    fala()
    print("-"*40)

elif opcao == "multiplicar":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(multiplicar(num1, num2))
    falando = (multiplicar(num1, num2))
    fala()
    print("-"*40)

elif opcao == "dividir":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(dividir(num1, num2))
    falando = (dividir(num1, num2))
    fala()
    print("-"*40)

elif opcao == "porcentagem":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(porcentagem(num1, num2))
    falando = (porcentagem(num1, num2))
    fala()
    print("-"*40)

elif opcao == "exponenciação":
    num1 = float(captacao())
    print("O numero falado foi:", num1)
    num2 = float(captacao())
    print("O numero falado foi:", num2)
    print(exponenciacao(num1, num2))
    falando = (exponenciacao(num1, num2))
    fala()
    print("-"*40)

else:
    falando = "não entendi"
    fala()
    exit()

