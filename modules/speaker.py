import pyttsx3

robot_mouth = pyttsx3.init()

def speak(text):
    robot_mouth.say(text)
    robot_mouth.runAndWait()