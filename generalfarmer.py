import pyautogui
import time
import keyboard
import threading
import os


def key_pressed(combo=str, delay=float):
    for i in range(len(combo)):
        pyautogui.write('1')
        pyautogui.write(combo[i])
        time.sleep(delay)


def open_instructions(filename=str):
    text = []
    with open(filename, 'r') as file:
        for line in file:
            text.append(line.strip())
    return text


def mouse_movement(x1=int, y1=int, x2=int, y2=int):
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()


def listen_for_exit():
    global running
    keyboard.wait('ctrl+q')
    running = False
    while True:
        if running:
            time.sleep(0.05)
        else:
            break


def main():
    qsfile = open_instructions("quickstart.txt")
    classes = open_instructions("class_combo_delay.txt")
    instructionsfile = open_instructions("instructions.txt")
    request = str()

    while (True):
        for i in qsfile:
            print(i)
        request = str(input("Input: ")).lower()
        if request == "start":
            break
        elif request == "list":
            os.system('cls')
            for i in classes:
                print(i)
        else:
            os.system('cls')
            print(f"Please enter a valid request 'start' or 'list'\n\n")

    combo = str(input("Enter combo: "))
    delay = float(input("Enter delay: "))
    clicker = str(input("Do you need auto click(y/n? ")).lower()
    for i in instructionsfile:
        print(i)

    keyboard.wait('ctrl+`')

    # Set initial and next positions of the mouse
    if clicker == "y":
        keyboard.wait('ctrl+1')
        initial_x, initial_y = pyautogui.position()
        keyboard.wait('ctrl+2')
        next_x, next_y = pyautogui.position()

    # Press keys and move mouse between initial and next positions
    global running
    threading.Thread(target=listen_for_exit).start()  # start the thread
    running = True
    while running:
        if keyboard.is_pressed('ctrl+shift+q'):
            # If the user pressed ctrl+`, break the loop and wait for the hotkey again
            print("Paused...")
            while True:
                if keyboard.is_pressed('ctrl+`'):
                    print("Resuming...")
                    break
                time.sleep(0.1)
        elif keyboard.is_pressed('ctrl+q'):
            # If the user pressed ctrl+q, exit the program
            exit()
        key_pressed(combo, delay)
        if clicker == "y":
            mouse_movement(initial_x, initial_y, next_x, next_y)


if __name__ == "__main__":
    main()
