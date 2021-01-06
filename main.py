import pyttsx3
engine = pyttsx3.init()



while True:
    talk = input("What do you want me to say")
    engine.say(talk)
    engine.runAndWait();
