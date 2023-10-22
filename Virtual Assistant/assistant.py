
import speech_recognition as sr
import pyttsx3
import webbrowser as web


recognizer = sr.Recognizer()


# def SpeakCommands(command):
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()


# with sr.Microphone() as source2:
#     recognizer.adjust_for_ambient_noise(source2, duration=0.2)

#     audio2 = recognizer.listen(source2)

#     text = recognizer.recognize_google(audio2)
#     text = text.lower()

#     print("Did you say " + text)
#     SpeakCommands(text)


def main():
    path = "C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s"
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        print("Please Say Something")

        audio = recognizer.listen(source)
        print("Recognizing Now...")

        try:
            dest = recognizer.recognize_google(audio)
            print("You have said : " + dest)

            web.get(path).open(dest)

        except Exception as e:
            print("Error : " + str(e))


if __name__ == "__main__":
    main()
