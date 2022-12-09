import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime 
import wikipedia
import webbrowser
import os
import smtplib
engine =  pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak (audio) :
    # say method on the engine that passing input text to be spoken
    engine.say(audio)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
def wishMe() :
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12 : 
                speak ("Good Morning:")
        elif hour>=12 and hour<18 :
                speak ("Good Afternoon")
                speak('I am Jarvis sir How may I help you')
        else:
                speak("Good Evening")
                speak('I am Jarvis sir How may I help you')
def takeCommand():
    #It takes microphone input from the user and returns string output
   r  = sr.Recognizer() 
   with sr.Microphone() as source:
       print ("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)
       try:
           print("Recognizing :")
           query = r.recognize_google(audio, language ='en-in')
           print (f"User said: {query}\n")
           
       except Exception as e:
           #print(e)
           print("Say that again please ... ")
           return "None"
   return query 
#Email function to send email on the desied Email account
def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.ehlo()
    server.starttls()
    server.login("emailId" , "password")
    server.sendmail("emailId" , to , content)
    server.close()
           
if __name__ == "__main__":
          wishMe()
        #   while True:
if 1:
            query = takeCommand().lower()
            if 'wikipedia' in query :
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences =2)
             speak("According to Wikepedia")
             print(results)
             speak(results)
             
             #Open Web Browser
            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open google" in query:
                webbrowser.open("google.com")
            elif "open stackoverflow" in query:
                webbrowser.open("stackoverflow.com")
                
                #Music play
            elif "play music" in query:
                music_dir = "C:\\Music" 
                songs = os.listdir(music_dir)
                os.startfile(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir , songs[0]))
                
                #Present Time Display
                
            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                
                #Opening an application inside our computer
            elif "open code"  in query:
                codepath = "C:\\Users\\yogesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
                os.startfile(codepath)
                
            elif "email" in query:
                try:
                    speak("What should I say")
                    content = takeCommand()
                    to = "yoagrawal4@gmail.com"
                    sendEmail(to , content)
                    speak("Email has Been Sent")
                except Exception as e:
                    print(e)
                    speak("Sorry My Friend Yogesh I am unable to send the mail due to unforseen circumstances")
                