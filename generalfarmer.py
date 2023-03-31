import pyautogui
import time
import keyboard
import threading


def key_pressed(combo=str, delay=float):
    for i in range(len(combo)):
        pyautogui.write('1')
        time.sleep(delay)
        pyautogui.write(combo[i])
        time.sleep(delay)


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
    print("Random = 25252345")
    print("Lightcaster = 423523232, delay = 0.65")
    print("Archpaladin = 42352235 delay = 1")
    combo = str(input("Enter combo: "))
    delay = float(input("Enter delay: "))
    clicker = str(input("Do you need auto click(y/n? ")).lower()
    print("1. Press <ctrl+`> to start the program")
    print("---if you said no to auto click, skip to step 4")
    print("2. Place cursor on quest then press <ctrl+1>")
    print("3. Place cursor on turn-in then press <ctrl+2>")
    print("4. Sit back, relax, and chill")
    print("5a. Press <ctrl+alt+q> to pause")
    print("     5b. Press <ctrl+`> to resume")
    print("6. Press <ctrl+q> to quit after unpausing")

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
        if keyboard.is_pressed('ctrl+alt+q'):
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
