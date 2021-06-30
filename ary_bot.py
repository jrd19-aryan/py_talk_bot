import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
from googlesearch.googlesearch import GoogleSearch
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# plays the predefined commands as audio to the user
def talk(text):
    engine.say(text)
    engine.runAndWait()

# takes voice command from the user
def take_command():
    try:
        # set default command value as null string 
        # in case the bot does not recognise audio
        command = ''    
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)             # voice from user microphone input as source
            command = listener.recognize_google(voice)  # feed voice to text from library
            command = command.lower()                   # convert query to lowercase to match with conditional statements

    except Exception as e:                              # print error message in case of an exception
            print(e)
    return command                                      

# runs search query based on input commands
def run_ary():
    flag = True
    while(flag):

        command = take_command()
        print(command)

        #conditional statement based on command recieved
        if 'ary' in command:
            talk("Hi user, how you doin'. Hope you doing fine")

        elif 'hello world' in command:
            talk('The world is at Sharda. Where are you?')

        elif 'play' in command:
            try:
                song = command.replace('play', '')
                talk('playing ' + song)
                url = 'www.youtube.com/results?search_query='+song
                webbrowser.open_new(url)

            except Exception as e:
                print e

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'who is' in command:
            try:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 2)
                print(info)
                talk(info)

            except Exception as e:
                print e
                talk('Sorry!!! Your person is not that famous right now')

        elif 'date' in command:
            talk(datetime.date.today())

        elif 'day today' in command:
            now = datetime.datetime.now()
            talk(now.strftime("%A"))

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'bye' in command or 'good night' in command or 'see you' in command:
            talk("It's been a long day, without you my friend. And I'll tell you all about it when I see you again, Take Care...")
            flag = False
        
        elif(command==''):
            talk("Please repeat the command I couldn't hear you.")
        
        else:
            talk('Here are some results from google to help you with')

            url = "https://www.google.co.in/search?q="+command
            webbrowser.open_new(url)

#call the run_ary function to execute
run_ary()