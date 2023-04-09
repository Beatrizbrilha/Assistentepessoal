import speech_recognition as sr
import pyttsx3

# Initialize speech recognition engine and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and execute commands


def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            if "hello" in command.lower():
                speak("Hello! How can I help you today?")
            elif "what's your name" in command.lower():
                speak("My name is Python Assistant.")
            else:
                speak("Sorry, I didn't understand that.")
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Call recognize_speech function in a loop
while True:
    recognize_speech()
