import speech_recognition

robot_ear = speech_recognition.Recognizer()

def listen():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.record(mic, duration=4)
        
    return audio