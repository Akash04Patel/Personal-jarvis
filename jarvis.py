import datetime
import os
import cv2
import random
import instaloader
import PyPDF2 as pdf2

import pyautogui
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time

import pyttsx3
import speech_recognition as sr
import _datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
#To text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")

    except Exception as e:
         speak("say that again please...")
         return "none"
    return query
#read pdf book
def pdf_reader():
    book=open('DSA.pdf','rb')
    pdfReader=pdf2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"Total numbers of pages in this book{pages}")
    speak("sir which pages you want listen?")
    num=int(takecommand().lower())
    page=pdfReader.getPage(num)
    text=page.extractText()
    speak(text)
#to wish
def wish():
   hour=int(datetime.datetime.now().hour)
   tt=time.strftime("%I:%M %p")


   if hour>=0 and hour<12:
         speak(f"good morning Boss,its{tt}")
   elif hour>=12  and hour<18:
         speak(f"good after noon Boss,its {tt}")
   else:
       speak(f"good evening Boss,its {tt}")
   speak("I am jarvis sir, how can i help you")
#to send email
def sendEmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()
#for news
def news():
    main_url='https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=47e1a2ae1bc4444e9d3a7ffa0f656f10'
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","four","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's  {day[i]} news is: {head[i]}")





if __name__=='__main__':
   # takecommand()
    wish()
    #speak("hello shiva")
    while True:
             query=takecommand().lower()
       #logic building for task
             if"open notepad" in query:
                  npath="C:\\Windows\\system32\\notepad.exe"
                  os.startfile(npath)
             elif"open google chrome browser"  in query:
                  apath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                  os.startfile(apath)
             elif "open cmd" in query:
                  cpath = "C:\\Windows\\system32\\cmd.exe"
                  os.startfile(cpath)
             elif" open camera" in query:
                 cap=cv2.VideoCapture(0)
                 while True:
                     ret, img =cap.read()
                     cv2.imshow('Camera',img)
                     k=cv2.waitKey(50)
                     if k==27:
                         break;
                     cap.release()
                     cv2.destroyAllWindows()
             elif "open Brave browser" in query:
                 bpath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                 os.startfile(bpath)
             elif"open vlc" in query:
                 vpath="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                 os.startfile(vpath)
             elif "open notepad plus plus"in query:
                 npath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                 os.startfile(npath)
             elif "open word"in query:
                 wpath="C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.exe"
                 os.startfile(wpath)
             elif"open music"in query:
                 music_dir="C:\\Users\\Akash\\Music"
                 songs=os.listdir(music_dir)
                 #rd=random.choice(songs)
                 for song in songs:
                     if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))
             elif "ip address" in query:
                 ip=get('https://api.ipify.org').text
                 speak(f"Your ip address is{ip}")
             elif"wikipedia"in query:
                 speak("searching wikipedia....")
                 query=query.replace("wikipedia","")
                 results=wikipedia.summary(query,sentences=2)
                 speak("according to wikipedia")
                 speak(results)
                 print(results)
             elif"open youtube"in query:
                 webbrowser.open("www.youtube.com")
             elif "open facebook" in query:
                 webbrowser.open("www.facebook.com")
             elif "open stackoverflow" in query:
                 webbrowser.open("www.stackoverflow.com")
             elif "open gfg" in query:
                 webbrowser.open("www.geeksforgeeks.org")
             elif "open leetcode" in query:
                 webbrowser.open("www.leetcode.com")
             elif"open google"in query:
                 speak("sir, what should i search on google")
                 cm=takecommand().lower()
                 webbrowser.open(f"{cm}")
             elif"send message"in query:
                 kit.sendwhatmsg("+919097735410","this is testing protocol",11,3)

             elif"play songs on youtube" in query or "play song on youtube"in query:
                 speak("sir, which song you want to play on youtube")
                 sm=takecommand().lower()
                 kit.playonyt(f"{sm}")
             elif"send email" in query:
                 speak("sir,To whom i have to send Email")
                 em=takecommand().lower()
                 try:
                     speak("what should i say to "f"{em}")
                     content=takecommand().lower()
                     to="pakash7253@gmail.com"
                     sendEmail(to,content)
                     speak("Email has been sent to"f"{em}")
                 except Exception as e:
                     print(e)
                     speak("sorry sir, i am not  able to send message")
             elif"no thanks"in query or "close" in query or "thank you" in query:
                 speak("thanks for using me sir ,have a good day")
                 sys.exit()
         #close any application


             elif"close notepad" in query:
                 speak("okay boss,closing notepad")
                 os.system("taskkill /f /im notepad.exe")
         #to set an alarm
             elif"set alarm"in query:
                 nn=int(datetime.datetime.now().hour)
                 if nn==22:
                     music_dir="C:\\Users\\Akash\\Music"
                     songs=os.listdir(music_dir)
                     os.startfile(os.path.join(music_dir,songs[0]))
             #to find a jokes
             elif"tell me a joke" in query:
                 joke=pyjokes.get_joke()
                 speak(joke)
             #to shut down
             elif"shut down the system"in query:
                 os.system("shutdown /s /t 5")
             #to restart
             elif"Restart the system"in query:
                 os.system("shutdown /r /s 5")
             #to sleep the system
             elif"sleep the system"in query:
                 os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
             elif"switch the window"in query:
                 pyautogui.keyDown("alt")
                 pyautogui.press("tab")
                 time.sleep(1)
                 pyautogui.keyUp("alt")
             elif"tell me news"in query:
                 speak("please wait sir,feteching the latest news")
                 news()
             #to find my location
             elif "where i am" in query or "where we are"in query:
                 speak("Wait sir, let me check")
                 try:
                     ipAdd=requests.get('https://api.ipify.org').text
                     print(ipAdd)
                     url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                     geo_requests=requests.get(url)
                     geo_data=geo_requests.json()
                     city=geo_data['city']
                     state=geo_data['region']
                     country=geo_data['country']
                     speak(f"sir i am not sure, but i think we are in{city} city of {state} state of {country} country")
                 except Exception as e:
                     speak("sorry sir, Due to network issue i am not able to find where we are ")
                     pass
             #to check instagram profile
             elif "check instagram profile" in query or "profile on instagram" in query:
                 speak("sir please enter the correct user name")
                 name=input("Enter user name here")
                 webbrowser.open(f"www.instagram.com/{name}")
                 speak(f"sir here is the profile of the user {name}")
                 time.sleep(5)
                 speak("sir would you like to download profile picture of this account?")
                 condition=takecommand().lower()
                 if "yes" in condition:
                     mod=instaloader.Instaloader()
                     mod.download_profile(name,profile_pic_only=True)
                     speak("i am done sir, profile picture is saved in our main folder")
                 else :
                     pass

             # To take screen shot
             elif"take a screenshot"in query or "take screenshot" in query:
                 speak("sir, please tell me the name for this screenshot file")
                 name=takecommand().lower()
                 speak("please sir hold the screen for few second, i am taking screenshot")
                 time.sleep(5)
                 img=pyautogui.screenshot()
                 img.save(f"{name}.png")
                 speak("i am done sir,the screenshot is saved in main folder")
            # pdf reader
             elif"read pdf"in query or"read book" in query:
                 pdf_reader()
           #To hide files and folder
             elif"hide all files"in query or "hide this folder" in query or"visible for everyone" in query:
                 speak("sir please tell me you want to hide this folder or make it visible for everyone ")
                 condition=takecommand().lower()
                 if"hide"in condition:
                     os.system("attrib +h /s /d")
                     speak("sir, all the files in this folder are now hidden")
                 elif"visible"in condition:
                     os.system("attrib -h /s /d")
                     speak("sir,all the files in this folder are now visible to everyone ")
                 elif"leave it"in condition or "leave for now"in condition:
                     speak("ok sir")
            # speak("sir,do you have any other work")