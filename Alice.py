# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import smtplib
import eel


engine = pyttsx3.init('sapi5')
# print(voices[1].id)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 178)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

@eel.expose
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alice Madam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        # eel.DisplayMessage("Listening...")
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        eel.receiverText("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(query)

    except Exception as e:
        print(e)    
        # speak("Pardon me, Say that again please...")  
        # print("Pardon me, Say that again please...")  
        return " "
    # return query
text=takeCommand()
speak(text)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant Alice is shutting down, See you soon')
            print('your personal assistant Alice is shutting down, see you soon')
            break

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open W3schools' in query:
            webbrowser.open("w3schools.com")
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Alice 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Kritika Gulati")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))  


        elif 'play music' in query:
            music_dir = "C:\\Users\\KRITIKA\\Music"
            songs = os.listdir(music_dir)
            d=random.choice(songs)
            print(songs)    
            # os.startfile(d)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in query:
            statement = query.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Maam, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\KRITIKA\\Downloads\\VSCodeUserSetup-x64-1.86.2.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            codePath = "C:\\Users\\KRITIKA\\Downloads\\VSCodeUserSetup-x64-1.86.2.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kritikagulati58@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry dear, I am not able to send this email")    
        else:
            print("No query matched")