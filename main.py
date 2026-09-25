from modules import listen, learn, speak

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
