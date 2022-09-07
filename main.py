import pyttsx3                    # text to speech module
import speech_recognition as sr   # converts audio into text
import datetime                   # shows date , time
import pywhatkit                  # play youtube videos
import calendar                   # allows us to get day of a week
import wikipedia                  # for searching wikipedia information
import webbrowser                 # opens any webbrowser
import os                         # allows us to interact with operating system



print("Initializing Nova")

MASTER = 'Aditi'
engine = pyttsx3.init('sapi5')
#helps us to set the speed at which our assistants would speak when we assign sentences or words.
engine.setProperty('rate', 180) 
engine.setProperty('volume', 0.9) # change the default volume 
voices = engine.getProperty('voices')   # getter method(gets the current value of engine property)
engine.setProperty('voice', voices[1].id)  # setter method .[0]=male voice and [1]=female voice in set Property.


# speak method will help us in taking the voice from the machine.
def speak(text):
    engine.say(text)  # Method for the speaking of the the assistant
    engine.runAndWait() # Blocks while processing all the currently queued commands

speak('Initializing Nova...')


# This function will greet you as per the current time.
def wishMe():

    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good Morning" + ' '  + MASTER)
        print("Good Morning" + ' ' + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + ' ' + MASTER)
        print("Good Afternoon" + ' ' + MASTER)
    else:
        speak("Good Evening" + ' ' + MASTER)
        print("Good Evening" + ' ' + MASTER)

    speak('I am your Nova')
    print('I am your Nova')
    speak('What can I do for you?')
    print('What can I do for you?')

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the 'recongizer' method for recognizing
def takeCommand():

    r = sr.Recognizer() # from the speech_Recognition module we will use the Microphone module for listening the command
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Now we will be using the try and catch
    # method so that if sound is recognized 
    # it is good else we will have exception 
    # handling
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # for Listening the command in indian english
        print(f"user said: {query}\n")
    except Exception as e:
        print("Please say that again")
        speak("Please say that again")
        query = None
    return query


# Main program starts here
wishMe()

# This method will check for the condition. 
# If the condition is true it will return output. 
# We can add any number if conditions for it and if the condition satisfy we will get the desired output.
def Take_query():

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
    while(True):

        # taking the query and making it into
        # lower case so that most of the times 
        # query matches and we get the perfect 
        # output
        query = takeCommand().lower()
    
        if "tell me about" in query:
            # if any one wants to have a information
            # from wikipedia
            print("searching wikipedia...")
            speak("searching wikipedia...")
            query = query.replace("tell me about", "")

            # it will give the summary of 2 lines from 
            # wikipedia we can increase and decrease 
            # it also.
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = "youtube.com"
            chrome_path = 'C:/Users/Shree/AppData/Local/Google/Chrome/Application/chrome.exe %s'
            # in the open method we just to give the link
            # of the website and it automatically open 
            # it in your default browser
            webbrowser.get(chrome_path).open(url)
        
        elif 'play music' in query:    # this will play the songs present in your os
            songs_dir = 'F:\my songs'
            songs = os.listdir(songs_dir)
            # print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'time' in query:   # this is for getting current time
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is:' + ' ' + time)
            speak('Current time is:' + ' ' + time)

        elif 'date' in query:     # this is for getting current date
            now = datetime.datetime.now()
            my_date = datetime.datetime.today()
            weekday = calendar.day_name[my_date.weekday()]  # e.g. Monday
            monthNum = now.month
            dayNum = now.day

            month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October', 'November',
                   'December']
            ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th',
                      '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th',
                      '18th', '19th', '20th', '21st', '22nd',
                      '23rd', '24th', '25th', '26th', '27th',
                      '28th', '29th', '30th', '31st']

            print('Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + Year + '.')
            speak('Today is ' + weekday + ' ' +month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + Year + '.')


        elif 'play' in query:  # for playing videos
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)    # play videos on youtube

        # This will exit and terminate the program.
        elif "bye" or "see you later" in query:
            print("Bye. Have a nice day.")
            speak("Bye. Have a nice day.")
            exit()

if __name__ == '__main__':
     
    # main method for executing
    # the functions
    Take_query()

