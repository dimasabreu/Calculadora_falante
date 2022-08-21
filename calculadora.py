import pyttsx3
import speech_recognition as sr
import calculadora

r = sr.Recognizer()
with sr.Microphone() as source:
    engine = pyttsx3.init()
    engine.say("Fale o que você gostaria de fazer")
    engine.runAndWait()
    print("Fale o que você gostaria de fazer")
    audio = r.listen(source)
    opcao = r.recognize_google(audio, language="pt-BR")
    print(opcao)
if opcao == "somar":
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    print(calculadora.somar(num1, num2))
    engine = pyttsx3.init()
    engine.say(calculadora.somar(num1, num2))
    engine.runAndWait()
