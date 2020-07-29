import keyboard

text_to_print='default_predefined_text'
shortcut = 'ctrl+=' #define your hot-key
print('Hotkey set as:', shortcut)

def on_triggered(): #define your function to be executed on hot-key press
    print(text_to_print)
    #write_to_textfield(text_to_print) #<-- your function
keyboard.add_hotkey(shortcut, on_triggered) #<-- attach the function to hot-key

if __name__ =="__main__":
    print("Press ESC to stop.")
    i = 1
    while 1:
        print(i)
        i =i +1
    keyboard.wait('esc')