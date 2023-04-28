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
    global running
    global is_paused
    while True:
        if running and not is_paused:
            for i in combo:
                pyautogui.write('1')
                pyautogui.write(i)
                time.sleep(delay)


def key_consumable():
    '''
    Presses the consumable
    '''
    global running
    global is_paused
    while True:
        if running and not is_paused:
            pyautogui.write('6')
            time.sleep(1)


def mouse_position(x1=int, y1=int, x2=int, y2=int):
    '''
    Controls the mouse position:
    P1: The quest
    P2: The turn-in button
    '''
    global running
    global is_paused
    while True:
        if running and not is_paused:
            pyautogui.moveTo(x1, y1)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(x2, y2)
            pyautogui.click()


def exit():
    global running
    print('Waiting for exit hotkey')
    keyboard.wait('ctrl+q')
    print("Exit hotkey pressed")
    running = False
    while True:
        if running:
            time.sleep(0.05)
        else:
            break


def pause():
    global is_paused
    keyboard.wait('ctrl+shift+q')
    print("Pausing...")
    is_paused = True
    keyboard.wait('ctrl+`')
    is_paused = False
    print('Resuming...')


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
    exit_thread = threading.Thread(target=exit)
    exit_thread.start()

    running = True

    global is_paused
    pause_thread = threading.Thread(target=pause)
    pause_thread.start()

    is_paused = False

    # Thread for the combo and consumable
    combo_thread = threading.Thread(target=key_combo, args=[combo, delay])
    consumable_thread = threading.Thread(target=key_consumable)
    combo_thread.start()
    consumable_thread.start()

    # Thread for the mouse
    if clicker == "y":
        mouse_thread = threading.Thread(target=mouse_position, args=[
                                        initial_x, initial_y, next_x, next_y])
        mouse_thread.start()

    # while running:
    #    if is_paused:
    #        print("Paused...")
    #        keyboard.wait('ctrl+`')

    while running:
        pass
    else:
        print("exiting")
        exit()

    combo_thread.join()
    consumable_thread.join()

    if clicker == "y":
        mouse_thread.join()

    exit_thread.join()
    pause_thread.join()


if __name__ == "__main__":
    main()
