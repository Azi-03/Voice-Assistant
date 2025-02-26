import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def talk(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Listens for user commands and processes them."""
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command


def run_alexa():
    """Executes actions based on user commands."""
    command = take_command()
    if not command:
        return  # Exit if no command was detected
    print(f"Processing command: {command}")
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")
        print(f"Time: {time}")
    elif 'tell me about' in command:
        person = command.replace('tell me about', '').strip()
        info = wikipedia.summary(person, sentences=1)
        talk(info)
        print(info)
    elif 'date' in command:
        talk("I have a headache.")
    elif 'are you single' in command:
        talk("I'm in a relationship with technology.")
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk("Please say the command again.")


# Main loop
while True:
    run_alexa()
