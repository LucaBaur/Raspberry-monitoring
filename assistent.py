import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sage etwas:")
        audio = recognizer.listen(source)

    try:
        print("Ich denke, du hast gesagt: " + recognizer.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Entschuldigung, ich habe dich nicht verstanden.")
    except sr.RequestError:
        print("Es gab ein Problem bei der Spracherkennung.")

if __name__ == "__main__":
    recognize_speech()
