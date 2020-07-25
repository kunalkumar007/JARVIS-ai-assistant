import pyttsx3
import datetime
import speech_recognition as Sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Jarvis ready for Command ,Sir!!")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = Sr.Recognizer()
    with Sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print("User Said:", query)
    except Exception as e:
        print(e)
        print("Say that Again Sir...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    takeCommand()
