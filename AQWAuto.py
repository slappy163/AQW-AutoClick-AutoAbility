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

def key_combo(combo = str, delay = float):
    '''
    Presses the Combo
    '''
    for i in combo:
        pyautogui.write('1')
        pyautogui.write(i)
        time.sleep(delay)

def mouse_position(x1 = int, y1 = int, x2 = int, y2 = int):
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

def main():
    # Open the files
    qsfile = open_instructions("quickstart.txt")
    classes = open_instructions("class_combo_delay.txt")
    instructionsfile = open_instructions("instructions.txt")





if __name__ == "__main__":
    main()
