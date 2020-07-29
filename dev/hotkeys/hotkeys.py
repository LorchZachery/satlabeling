from pynput import keyboard

# the key combination to look for 
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=65)}
]

def execute():
    """function to execute when a combination is pressed"""
    print("do something")


# The currently pressed key (initially empty)
pressed_vks = set()

def get_vk(key):
    """
    Get the virtual key code form a key.
    these are used so case/shift modifications are ignored
    """
    
    return key.vk if hasattr(key, 'vk') else key.value.vk
    
def is_combination_pressed(combination):
    """check if the combination is satisifed using the keys pressed in pressed_vks
    """
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    """when a key is pressed"""
    vk = get_vk(key) # get keys vk
    pressed_vks.add(vk) # adding it to the set of currently pressed keys
    
    for combination in COMBINATIONS: 
        if is_combination_pressed(combination):
            execute()
            break

def on_release(key):
    """when key is released"""
    vk = get_vk(key)
    pressed_vks.remove(vk)
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()