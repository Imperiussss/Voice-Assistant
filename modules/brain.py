import json
import webbrowser
from AppOpener import open as open_app
from datetime import date
from datetime import datetime
from modules.listener import robot_ear

with open("data/apps.json", "r", encoding="utf-8") as app_file:
    apps = json.load(app_file)

with open("data/webs.json", "r", encoding="utf-8") as web_file:
    webs = json.load(web_file)

def conversation_command(command):
    if "hello" in command or "hi" in command:
        robot_brain = "Hello, Thanh Vu"
    elif "today" in command:
        today = date.today()
        robot_brain = "Today is: " + today.strftime("%B %d, %Y")
    elif "time" in command:
        time = datetime.now()
        robot_brain = "Current time is: " + time.strftime("%H hours %M minutes %S seconds")
    elif "how are you" in command:
        robot_brain = "Im fine thank you, and you?"
    elif any(keyword for keyword in ("bye","goodbye","close")):
        robot_brain = "Goodbye!"
    else:
        robot_brain = "Sorry, i can't understand"
    return robot_brain


def application_command(command):
    for keyword in sorted(apps, key=len, reverse=True):
        app_name = apps[keyword]
        if keyword in command:
            robot_brain = "Open " + keyword
            open_app(app_name)
            return robot_brain
        
    return "I can't find this Application"

def website_command(command):
    for keyword in sorted(webs, key=len, reverse=True):
        web_name = webs[keyword]
        if keyword in command:
            robot_brain = "Open " + keyword
            webbrowser.open(web_name)
            return robot_brain
        
    return "I can't find this Website"



def learn(audio):
    try:
        command = robot_ear.recognize_google(audio).lower()
    except:
        command = ""

    print(command)
    
    if command == "":
        robot_brain = "Sorry, i can't hear you"            
    elif "open" in command:
        if any(keyword in command for keyword in webs):
            robot_brain = website_command(command)
        elif any(keyword in command for keyword in apps):
            robot_brain = application_command(command)    
        else: 
            robot_brain = "I can't find this website or application"
    else: 
        robot_brain = conversation_command(command)
    return robot_brain