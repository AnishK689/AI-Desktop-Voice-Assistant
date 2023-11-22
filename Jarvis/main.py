import speech_recognition as sr
import datetime
import webbrowser
import win32com.client
import openai
import datetime
from config import apikey
import subprocess
# todo : we can play music, we can open our personal instagram account using web driver
speaker = win32com.client.Dispatch("SAPI.SpVoice")  # in mac there is no need for this

# while(1):
#     print("Enter the word")
#     s = input()
# speaker.Speak(s)
import os
import random
def get_date_and_day():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    day = now.strftime("%A")
    return date, day
def ai(prompt):
    openai.api_key = apikey
    text = f"Openai response for Prompt:  {prompt}\n****************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : wrap this inside of a try catch block
    print(response["choices"][0]["message"]["content"])
    text += response["choices"][0]["message"]["content"]
    if not os.path.exists("Openai "):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.randint(1,234543565)}", "w") as f:
        f.write(text)



def say(text):
    # os.system(f"say {text}")
    if text == "Jarvis stop":
        speaker.Speak("bye from jarvis")
        exit(1)
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        r.pause_threshold = 1 #we can change
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said {query}")
            return query
        except Exception as e:
            return "Some error occured, sorry from jarvis."
if __name__ == '__main__':
    print("Pycharm")
    say("Hello I am Jarvis AI.")
    while True :
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites =[["youtube", "https://www.youtube.com"], ["wikipedia",
        "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        if f"open {sites[0][0]}" in  query.lower():
            say(f"Opening {sites[0][0]} sir.")
            webbrowser.open("https://youtube.com")
        elif f"open {sites[1][0]}" in  query.lower():
            say(f"Opening {sites[1][0]} sir.")
            webbrowser.open(sites[1][1])
        elif f"open {sites[2][0]}" in query.lower():
            say(f"Opening {sites[2][0]} sir.")
            webbrowser.open(sites[2][1])
        # todo: Add a feature to play a specific song
        elif "open music" in query.lower():
            musicpath="C:/Users/anish/Downloads/tvari-hawaii-vacation-159069.mp3"
            say("Opening music...")
            os.startfile(musicpath) # we can use directory and search songs in it using jarvis
        elif "the time" in query :
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir time is {strfTime}")
        elif "what's the date" in query.lower() or "tell me the date" in query.lower() or "what day is it" in query.lower() or "what is the day today" in query.lower():
            date, day = get_date_and_day()
            print(f"Today is {date} and it's a {day}.")
            speaker.Speak(f"Today is {date} and it's a {day}.")
        elif "open vs code" in query.lower():
            say("Opening V S Code sir..")
            vscodepath= "C:/Users/anish/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(vscodepath)
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        else :
            say(query)