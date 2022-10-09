import speech_recognition as sr
import pyttsx3 as txt
import pywhatkit as do
import datetime
import wikipedia

listener = sr.Recognizer()
engine = txt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#class peace_out():
def talk(text):
    engine.say(text)
    engine.runAndWait()


def orders():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'peace' in command:
                command = command.replace('peace', ' ')
                print(command)
    except:
        pass
    return command


class peace_out():
    def peace():
        command = orders()
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            do.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I %M %p')
            print(time)
            talk('current time is' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

    peace()


peace_out()
