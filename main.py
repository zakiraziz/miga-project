import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

<<<<<<< HEAD
def processCommand(command):
    print(f"Processing command: {command}")
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "quit" in command.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command.")

if __name__ == "__main__":
<<<<<<< HEAD
    speak("Initializing Jarvis....")
    try:
        while True:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust to ambient noise
                print("Listening for activation keyword 'Jarvis'...")
                audio = recognizer.listen(source, timeout=15, phrase_time_limit=10)  # Increased timeout for flexibility
                try:
                    activation_command = recognizer.recognize_google(audio).lower()

                    if activation_command == "jarvis":
                        speak("Yes, how can I help?")
                        print("Jarvis activated. Listening for a command...")

                        # Listen for actual command
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                        command = recognizer.recognize_google(audio).lower()
                        processCommand(command)
                
                except sr.UnknownValueError:
                    speak("Sorry, I didn't catch that.")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition; {e}")
    
    except KeyboardInterrupt:
        print("Program interrupted by user, exiting...")
        speak("Goodbye!")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
=======
    speak("Initializing Jarivis....")
=======

def processCommand(c):
    print(c)
    pass

if __name__ == "__main__":
    speak("Initializing Jarvis....")
>>>>>>> ddabea90fe8dd455222c80e4084cd5c27dbf5d07
    while True:
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing..")
        try:
<<<<<<< HEAD
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
>>>>>>> e4061e9a62d557e437f5cee066b161306aed7f55
=======
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
>>>>>>> ddabea90fe8dd455222c80e4084cd5c27dbf5d07
