# FRIDAY
<p align = "left"><img src = "https://github.com/aryanc381/FRIDAY/blob/master/fridaypicreadme.jpg" width = 100% height = 100%

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2303.17580)
[![Open in Spaces](https://img.shields.io/badge/%F0%9F%A4%97-Open%20in%20Spaces-blue)](https://huggingface.co/spaces/microsoft/HuggingGPT)

## Description
The mission of Friday is to create a personalized virtual Artificial Intelligence model that helps you in everything.

## Libraries used 
+ Speech_Recognition
+ Win32com.client
+ Webbrowser
+ OS
+ OpenAI
+ Datettime
+ Pyttsx3
+ Wikipedia

## Things to add
+ Sign detection in the room using OpenCV with the integration of the DeepLearning model.
+ Appropriate voice module for human-like conversation.
+ Sense of Humour.
+ OpenAI API.
+ Machine Learning Model for Friday.
+ Integration of Friday to RasberryPi to connect to speaker, camera microphone, and other electronic components.
+ DBMS for storing data and conversations.
+ Interface of DBMS if one wants to access the conversations made.
+ Integrating apps with Friday to send and receive commands.

## Inspo
See my inspiration [Jarvis with Tony](https://www.youtube.com/watch?time_continue=93&v=Zg_nD_x0bgM&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fsca_esv%3Db93ed2d8a499a99a%26sca_upv%3D1%26sxsrf%3DACQVn08YUuAw2XPSnGo7BpFMT8PD_vendw%3A1712648187758%26q%3Diron%2Bm&source_ve_path=Mjg2NjY&feature=emb_logo)

## Code 
#### 1. Basic Conditions to make conversations : 
```bash
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
```
## Conclusion 
Friday is supposed to be set and in use as soon as possible and furnished by 4th of July 2024. 
