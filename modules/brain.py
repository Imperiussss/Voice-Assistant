import json
import webbrowser
from AppOpener import open as open_app
from AppOpener import close as close_app
from datetime import date, datetime
from modules.listener import robot_ear
from urllib.parse import quote_plus

# ================================== READ KEYWORD ==================================

with open("data/apps.json", "r", encoding="utf-8") as app_file:
    apps = json.load(app_file)

with open("data/webs.json", "r", encoding="utf-8") as web_file:
    webs = json.load(web_file)

# ===================================== COMMAND =====================================

OPEN_COMMANDS =  {
    "open", "launch", "start", "run"
}

SEARCH_COMMANDS = { 
    "search", "google", "look up"
}

CLOSE_COMMANDS = { 
    "close", "exit", "quit"
}

# ===================================== UTILS ===================================== 

def contains_command(sentences, commands):
    return any(word in sentences for word in commands)


# ===================================== COMMAND ( BRAIN ) ===================================== 

def conversation_command(command):
    if "hello" in command or "hi" in command:
        return "Hello, Thanh Vu"
    elif "today" in command:
        today = date.today()
        return "Today is: " + today.strftime("%B %d, %Y")
    elif "time" in command:
        time = datetime.now()
        return "Current time is: " + time.strftime("%H hours %M minutes %S seconds")
    elif "how are you" in command:
        return "Im fine thank you, and you?"
    elif any(keyword in command for keyword in ("bye","goodbye","close")):
        return "Goodbye!"
    else:
        return "Sorry, i can't understand"


def application_command(command):
    for keyword in sorted(apps, key=len, reverse=True):
        app_name = apps[keyword]

        if contains_command(command, OPEN_COMMANDS) and keyword in command:
            open_app(app_name)
            return "Open " + keyword
        elif contains_command(command, CLOSE_COMMANDS) and keyword in command:
            close_app(app_name)
            return "Close " + keyword
        
    return "I can't find this Application"

def website_command(command):
    for keyword in sorted(webs, key=len, reverse=True):
        web_name = webs[keyword]

        if contains_command(command, OPEN_COMMANDS) and keyword in command:
            webbrowser.open(web_name)
            return "Open " + keyword
        
    return "I can't find this Website"


def search_command(command):
    for keyword in SEARCH_COMMANDS:
        if command.startswith(keyword):
            query = command[len(keyword):].strip()

            if query:
                encoded_query = quote_plus(query)
                url = "https://www.google.com/search?q=" + encoded_query
                webbrowser.open(url)
                return command + query

    return "What do you want me to search?"

# ===================================== LEARN ===================================== 

def learn(audio):
    try:
        command = robot_ear.recognize_google(audio).lower()
    except:
        command = ""

    print(command)
    
    if command == "":
        robot_brain = "Sorry, i can't hear you"   
    elif any(command.startswith(keyword) for keyword in SEARCH_COMMANDS):
            robot_brain = search_command(command)             
    elif any(keyword in command for keyword in webs):
        robot_brain = website_command(command)
    elif any(keyword in command for keyword in apps):
        robot_brain = application_command(command)
    else: 
        robot_brain = conversation_command(command)
    return robot_brain