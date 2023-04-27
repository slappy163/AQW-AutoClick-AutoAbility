import pyautogui
import time
import keyboard
import threading
import os


def open_file(filename=str):
    '''
    Open the files
    '''
    text = []
    with open(filename, 'r') as file:
        for line in file:
            text.append(line.strip())
    return text


def key_combo(combo=str, delay=float):
    '''
    Presses the Combo
    '''
    for i in combo:
        pyautogui.write('1')
        pyautogui.write(i)
        time.sleep(delay)


def consumable():
    '''
    Presses the consumable
    '''
    pyautogui.write('6')
    time.sleep(10)


def mouse_position(x1=int, y1=int, x2=int, y2=int):
    '''
    Controls the mouse position:
    P1: The quest
    P2: The turn-in button
    '''
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(x2, y2)
    pyautogui.click()


def exit():
    global running
    keyboard.wait('ctrl+q')
    running = False
    while True:
        if running:
            time.sleep(0.5)
        else:
            break


def pause():
    global is_paused
    keyboard.wait('ctrl+shift+q')
    is_paused = True
    while True:
        if not is_paused:
            time.sleep(0.5)
        else:
            break


def main():
    # Open the files
    qsfile = open_file("quickstart.txt")
    classes = open_file("class_combo_delay.txt")
    instructionsfile = open_file("instructions.txt")

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
    clicker = str(input("Do you need auto turn-in(y/n)? ")).lower()
    for i in instructionsfile:
        print(i)

    if clicker == "y":
        keyboard.wait('ctrl+1')
        initial_x, initial_y = pyautogui.position()
        keyboard.wait('ctrl+2')
        next_x, next_y = pyautogui.position()

    # Will continue with the program once it recieves input
    keyboard.wait('ctrl+`')

    # Main Loop
    global running
    threading.Thread(target=exit).start()  # start the thread
    running = True

    global is_paused
    threading.Thread(target=pause).start()
    is_paused = False

    combo = threading.Thread(target=key_combo, args=[combo, delay]).start()
    mouse = threading.Thread(target=mouse_position, args=[
                             initial_x, initial_y, next_x, next_y])
    consumable = threading.Thread(target=consumable).start()

    if clicker == "y":
        mouse.start()

    while running:
        if is_paused:
            print("Paused...")
            keyboard.wait('ctrl+`')
            print('Resuming...')

    combo.join()
    mouse.join()
    consumable.join()


if __name__ == "__main__":
    main()
