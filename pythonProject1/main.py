# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyttsx3 as p
import speech_recognition as s_r
from youtube import You  # Ensure 'You' class is imported correctly from the 'youtube' module
from sel_webdriver import infow
from news import *
import randfacts
from joke import *
from weather import *
import datetime


voice = p.init()
voice.setProperty('rate', 145)
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)

def sayit(text):
    voice.say(text)
    voice.runAndWait()

def greetings():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

# Speech-to-text portion
today=datetime.datetime.now()
re = s_r.Recognizer()

print("Hello, good " +greetings() + " I am Suri")
sayit("Hello, good " +greetings() + " I am Suri")

date_string = "Today is " + today.strftime("%d") + " of " + today.strftime("%B") + " and it's currently " + today.strftime("%I") + ":" + today.strftime("%M") + " " + today.strftime("%p")

print(date_string)
sayit(date_string)
print("How is your day going?")
sayit("How is your day going?")
with s_r.Microphone() as sound:
    re.energy_threshold = 15000
    re.adjust_for_ambient_noise(sound, 1.5)
    print("Listening...")
    speech = re.listen(sound)
    text = re.recognize_google(speech)
    print(text)

if "how" in text or "what" in text and "are" in text or "about" in text and "you" in text:
    sayit("I am fantastic")

print("please choose the task you need my assistance in:")
print("1. Information")
print("2. Audio/Video")
print("3. News")
print("4. Random facts/ jokes")
print("5. Weather")

sayit("How may I assist you?")

with s_r.Microphone() as sound:
    re.energy_threshold = 15000
    re.adjust_for_ambient_noise(sound, 1.5)
    print("Listening...")
    speech = re.listen(sound)
    text2 = re.recognize_google(speech)
    print(text2)

if "information" in text2:
    sayit("What information do you need?")

    with s_r.Microphone() as sound:
        re.energy_threshold = 15000
        re.adjust_for_ambient_noise(sound, 1.5)
        print("Listening...")
        speech = re.listen(sound)
        text3 = re.recognize_google(speech)
        sayit("Searching {} in Wikipedia...".format(text3))
        print(text3)

    inst = infow()
    inst.get_Info(text3)
    # Keep the browser open
    try:
        while True:
            if not inst.driver.window_handles:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        inst.driver.quit()

elif "play" in text2 and ("video" in text2 or "song" in text2):
    sayit("What video should I play?")
    with s_r.Microphone() as sound:
        re.energy_threshold = 15000
        re.adjust_for_ambient_noise(sound, 1.5)
        print("Listening...")
        speech = re.listen(sound)
        start = re.recognize_google(speech)
        print("Playing {}...".format(start))
        sayit("Playing {}...".format(start))
        auto = You()
        auto.play(start)
        # Keep the browser open
        try:
            while True:
                if not auto.driver.window_handles:
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            auto.driver.quit()

elif "news" in text2:
    print("showing the latest news...")
    sayit("showing the latest news...")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        sayit(arr[i])

elif "fact" in text2 or "facts" in text2:
    print("showing some random fact...")
    sayit("showing some random fact...")
    y=randfacts.get_fact()
    print(y)
    sayit("did you know that, "+y)

elif "joke" in text2 or "jokes" in text2:
    print("telling some random jokes...")
    sayit("telling some random jokes...")
    arr = joke()
    print(arr[0])
    sayit(arr[0])
    print(arr[1])
    sayit(arr[1])

elif "weather" in text2 or "temperature" in text2:
    print("temperature in Indore is:" + str(temp()) + "degree celsius " + "and with " + str(desc()))

    sayit("temperature in Indore is:" + str(temp()) + "degree celsius "+   "and with " + str(desc()))

