import speech_recognition
import pyttsx3
import webbrowser
from AppOpener import open
from datetime import date
from datetime import datetime

# ROBOT PART INIT
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

# MODULE LISTEN
def listen():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.record(mic, duration=3)
    return audio

# MODULE LEARN
def learn(audio):
    try:
        you = robot_ear.recognize_google(audio).lower()
    except:
        you = ""
    
    if you == "":
        robot_brain = "Sorry, i can't hear you, please try again"
    elif "hello" in you or "hi" in you:
        robot_brain = "Hello, Thanh Vu"
    elif "today" in you:
        today = date.today()
        robot_brain = "Today is: " + today.strftime("%B %d, %Y")
    elif "time" in you:
        time = datetime.now()
        robot_brain = "Current time is: " + time.strftime("%H hours %M minutes %S seconds")
    elif "how are you" in you:
        robot_brain = "Im fine thank you, and you?"
    elif "bye" in you or "goodbye" in you:
        robot_brain = "Goodbye!"
    elif "open" in you:
        url = None
        app = None
        if "google" in you:
            robot_brain = "Open Google"
            url = "https://www.google.com"
        elif "youtube" in you:
            robot_brain = "Open YouTube"
            url = "https://www.youtube.com"
        elif "facebook" in you:
            robot_brain = "Open Facebook"
            url = "https://www.facebook.com"
        elif "chrome" in you:
            robot_brain = "Open Google Chrome"
            app = "chrome"
        elif "notepad" in you:
            robot_brain = "Open notepad"
            app = "notepad"
        elif "spotify" in you:
            robot_brain = "Open Spotify"
            app = "spotify"
        elif "visual studio" in you:
            if "code" in you:
                robot_brain = "Open Visual Studio Code"
                app = "visual studio code"
            else: 
                robot_brain = "Open Visual Studio"
                app = "visual studio"
        else:
            robot_brain = "I don't know this website or application"
        if url:
            webbrowser.open(url)
        elif app:
            open(app)
    else:
        robot_brain = "I don't understand"
    return robot_brain

# MODULE SPEAK
def speak(text):
    robot_mouth.say(text)
    robot_mouth.runAndWait()


def main():
    while True:
        audio = listen()

        robot_brain = learn(audio)

        print("Robot: " + robot_brain)
        speak(robot_brain)

        if robot_brain == "Goodbye!":
            break

if __name__ == "__main__":
    main()
