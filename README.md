# AQW-AutoClick-AutoAbility

## What it does?
Not the best, not the worse... As for my first cs project, I chose to write a program that will automate keyboard and mouse actions. This is designed for AQW (Adventure quest Worlds). A game with a lot of tedious grind and endless starring at a screen keyboard smashing. As to resolve this program, will do farming **HANDS FREE**.

## How it works?
```
When you first run up the program, it will show a list of instructions:
    Random = 25252345
    Lightcaster = 423523232, delay = 0.65
    Archpaladin = 42352235, delay = 1                 // Examples of classes, and combo and delay I use to run
    Enter combo:                                      // Enter the combo you want it to play
    Enter delay:                                      // cooldown timer btw each timer
    Do you need auto click(y/n?)                      // Do you need auto turn-in
    1. Press <ctrl+`> to start the program            // Starts the program
    ---if you said no to auto click, skip to step 4
    2. Place cursor on quest then press <ctrl+1>
    3. Place cursor on turn-in then press <ctrl+2>
    4. Sit back, relax, and chill
    5a. Press <ctrl+alt+q> to pause
         5b. Press <ctrl+`> to resume
    6. Press <ctrl+q> to quit after unpausing
```

## Language Used
###**Python**
```
pyautogui
keyboard
threading
time
