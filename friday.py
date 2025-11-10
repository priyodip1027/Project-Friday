import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How may i help you ?")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def search_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)


def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search on youtube' in query:
            search_query = query.replace('search youtube', '').strip()
            search_youtube(search_query)

        elif 'search on google' in query:
            search_query = query.replace('google', '').strip()
            search_google(search_query)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'open reddit' in query:
            webbrowser.open("https://www.reddit.com")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com")


        elif 'open spotify' in query:
            # Path to the Spotify executable on your computer
            spotify_executable = r'C:/Users/USER\AppData/Local/Microsoft\WindowsApps/spotify.exe'
            os.startfile(spotify_executable)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        

        