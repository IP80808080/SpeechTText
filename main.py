import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source1:
    print("Speak")
    audio1 = r.listen(source1)
    get = r.recognize_google(audio1)
    print(get)