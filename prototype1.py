import speech_recognition as sr
import win32com.client
import webbrowser
import os
import openai
import datetime
# import pyttsx3
# import wikipedia as wk

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            sites = [["Youtube", "https://www.youtube.com"], ["Wikipedia", "https://www.wikipedia.com"], ["Google", "https://www.google.com"]]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    speaker.Speak(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                    break
            else:
                if "what are you".lower() in query.lower():
                    speaker.Speak(f"I am an Artificial Intelligence Software made by Aryan to help him in his activities")
                # elif "I want to know something".lower() in query.lower():
                #     speaker.Speak("I'm listening, what's up!")
                #     voice = pyttsx3.init()
                #     In = input()  # This line needs modification, as input should not be taken from the speaker
                #     result = wk.summary(In, sentences=3)
                #     print(result)
                #     voice.say(result)
                #     voice.runAndWait()
                elif "the time".lower() in query.lower():
                    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speaker.Speak(f"The time is {strfTime}")
                elif "open vs code".lower() in query.lower():
                    code = r"C:\Users\conta\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    speaker.Speak("Opening VS Code, one second")
                    os.system(code)
                elif "did the chicken come first or the egg".lower() in query.lower():
                    speaker.Speak("The egg did, trust me I know, I was with god hahaha")
                else:
                    print(f"User said: {query}")
                    return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said!")
            return ""
        except sr.RequestError as e:
            print(f"Request error: {e}")
            return ""

if __name__ == '__main__':
    speaker.Speak("Hello, I am Jarvis")
    query = takeCommand()
    if query:
        speaker.Speak(query)

