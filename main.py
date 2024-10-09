import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    print(c)
    pass

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            if command.lower() == "jarvis":
                speak("Ya")
                # listn for commannd
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(c)

        except Exception as e:
            print("Error; {0}".format(e))
