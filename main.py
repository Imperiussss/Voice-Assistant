import speech_recognition
import pyttsx3
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
