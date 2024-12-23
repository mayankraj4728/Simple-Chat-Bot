import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[132].id)  
engine.setProperty('rate', 160)  
engine.setProperty('volume', 1) 


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""  
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)  
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-US')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')  
            print(f"Command recognized: {command}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command


talk("Hello, I am Rosy. How can I help you?")
#



# engine = pyttsx3.init()


# voices = engine.getProperty('voices')

# print("Available Voices:")
# for index, voice in enumerate(voices):
#     print(f"{index}: {voice.name}, Language: {voice.languages}, ID: {voice.id}")


# indian_voice = None
# for voice in voices:
#     if "en_IN" in voice.languages or "hi_IN" in voice.languages:  
#         indian_voice = voice.id
#         break

# if indian_voice:
#     engine.setProperty('voice', indian_voice)
#     print("\nIndian voice found and set successfully!")
# else:
#     print("\nIndian voice not found. Using default voice.")

# # Set Speaking Rate (optional for clarity)
# engine.setProperty('rate', 150)  # Default is ~200 words per minute

# # Text to Speak (Input your text here)
# text_to_speak = "नमस्ते! मैं आपका सहायक हूँ। Hello! How can I help you today?"

# # Speak the text
# print("\nSpeaking...")
# engine.say(text_to_speak)
# engine.runAndWait()

#

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)  
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)  
        print(info)
        talk(info)
    elif 'when was' in command:
        person = command.replace('when was', '')
        info = wikipedia.summary(person, 1)  
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')
    elif 'do you love me' in command:
        talk('ofcourse i love you.')
    elif 'varun' in command:
        talk('varun is a bitch guy!')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('could you please speak again.')


while True:
    run_alexa()


