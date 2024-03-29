import pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia
import os
import playsound     # pip install playsound


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
 

#taking voice input from user and converting it to string
def take_command():
  r = sr.Recognizer() #user input
  with sr.Microphone() as source:
    print("Listening.....")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognitizing.....")
    query  = r.recognize_google(audio, language='en-in')
    print (f"User said: {query}\n")

  except Exception as e:
    print(e)
    speak("say that again")
    return "none"
  return query



def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wish_me():
  hour = int(datetime.datetime.now().hour)  #typecasting this to int
  if hour >=0 and hour <12:
    speak("Good Morning")
  elif hour >=12 and hour <18:
    speak("Good afternoon")
  else:
    speak("Good evening")
  speak("I am jarvis. How can I assit you Sir.")




if __name__ == "__main__":
  engine.setProperty('rate',400)
  speak("hello Sir")
  wish_me()
  while True:
    query = take_command().lower()

    # below is the logic for searching stuffs on wiki
    if 'wikipedia' in query:
      speak("searching wiki....")
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=2)
      speak("According to wikipedia")
      speak(results)

    elif 'open youtube' in query:
      webbrowser.open("youtube.com",new=2)
    elif 'open Google' in query:
      webbrowser.open("Google.com")

    elif 'play music' in query:
      music_dir = "/Users/rajans/mp3"
      songs = os.listdir(music_dir)
      length = len(songs) - 1 
      song_number=random.randint(0,length)
      psong=songs[song_number]
      playsound(os.path.join(music_dir,psong), True)
      #os.startfile(os.path.join(music_dir,songs[0]))

    elif "time" in query:
      curr_time = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"the current time is {curr_time}")









