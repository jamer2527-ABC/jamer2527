import keyboard
import time

print("hold q and press w for creative mode\n")
print("hold e and press r for debug message\n")
print("hold t and press y for survival mode\n")

while True:
    # Check if both F3 and F4 are pressed for Creative Mode
    if keyboard.is_pressed('q') and keyboard.is_pressed('w'):
        print('Set own game mode to Creative Mode')
        while keyboard.is_pressed('q') or keyboard.is_pressed('w'):  
            time.sleep(0.1)  # Venter til tastene slippes

    # Check if both F1 and F2 are pressed for the debug message
    elif keyboard.is_pressed('e') and keyboard.is_pressed('r'):
        print("[Debug]: Unable to open game mode switcher: no permission")
        while keyboard.is_pressed('e') or keyboard.is_pressed('r'):  
            time.sleep(0.1)

    # Check if both F5 and F6 are pressed for Survival Mode
    elif keyboard.is_pressed('t') and keyboard.is_pressed('y'):
        print("Set own game mode to Survival Mode")
        while keyboard.is_pressed('t') or keyboard.is_pressed('y'):  
            time.sleep(0.1)

    time.sleep(0.1) 

# hei mats