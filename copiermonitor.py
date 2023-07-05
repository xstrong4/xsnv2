import pyperclip
import os
import threading

# Set the path to the folder where you want to save the copied content
folder_path = r"src\json"

# Create the folder if it doesn't already exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Set the file name to save the copied content
file_name = "tokens.txt"

# Set the full file path
file_path = os.path.join(folder_path, file_name)

# Initialize the variable to store the last clipboard content
last_clipboard_content = ""

# Define a function to continuously monitor the clipboard and save any new content to a file
def monitor_clipboard():
    global last_clipboard_content
    while True:
        # Get the current clipboard content
        clipboard_content = pyperclip.paste()
        
        # If the clipboard content is not empty and is different from the last saved content
        if clipboard_content != "" and clipboard_content != last_clipboard_content:
            # Save the content to a new line in the specified file
            with open(file_path, "a") as f:
                f.write(clipboard_content + " ")
            
            # Remember the currently saved clipboard content for comparison in the next iteration
            last_clipboard_content = clipboard_content

# Define a function to listen for user input from the command prompt and clear the file when the user types the command "tcls"
def listen_for_input():
    while True:
        command = input()
        if command.strip().lower() == "tcls":
            try:
                # Delete the file and create a new empty file
                os.remove(file_path)
                open(file_path, "w").close()
                
                # Print a message indicating that the file has been cleared
                print(f"File cleared: {file_path}")
            except OSError:
                # Print a message indicating that an error occurred while clearing the file
                print(f"Error: could not clear file {file_path}")

# Start a new thread to continuously monitor the clipboard
clipboard_thread = threading.Thread(target=monitor_clipboard)
clipboard_thread.start()

# Listen for user input from the command prompt in the main thread
listen_for_input()
