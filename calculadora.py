import pyttsx3
import speech_recognition as sr
import contas

r = sr.Recognizer()
with sr.Microphone() as source:
    print("""Bem-vindo a Calculadora falante!
(espere sempre uma confirmação visual)""")
    print("-"*40)
    engine = pyttsx3.init()
    engine.say("Fale o que você gostaria de fazer")
    engine.runAndWait()
    print("Fale o que voce gostaria de fazer:")
    audio = r.listen(source)
    opcao = r.recognize_google(audio, language="pt-BR")
    print("Voce escolheu", opcao.upper(), "!")
    if opcao == "somar":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.somar(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.somar(num1, num2))
        engine.runAndWait()
        print("-"*40)
    elif opcao == "subtrair":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.subtrair(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.subtrair(num1, num2))
        engine.runAndWait()
        print("-"*40)
    elif opcao == "multiplicar":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.multiplicar(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.multiplicar(num1, num2))
        engine.runAndWait()
        print("-"*40)
    elif opcao == "dividir":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.dividir(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.dividir(num1, num2))
        engine.runAndWait()
        print("-"*40)
    elif opcao == "porcentagem":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.porcentagem(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.porcentagem(num1, num2))
        engine.runAndWait()
        print("-"*40)
    elif opcao == "exponenciação":
        engine = pyttsx3.init()
        engine.say("Fale o primeiro numero")
        engine.runAndWait()
        print("Fale o primeiro numero:")
        audio = r.listen(source)
        numr1 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr1)
        engine = pyttsx3.init()
        engine.say("Fale o segundo numero")
        engine.runAndWait()
        print("Fale o segundo numero:")
        audio = r.listen(source)
        numr2 = r.recognize_google(audio, language="pt-BR")
        print("O numero escolhido foi:", numr2)
        num1 = float(numr1)
        num2 = float(numr2)
        print(contas.exponenciacao(num1, num2))
        engine = pyttsx3.init()
        engine.say(contas.exponenciacao(num1, num2))
        engine.runAndWait()
        print("-"*40)
    else:
        exit()
