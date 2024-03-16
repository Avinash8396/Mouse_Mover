import pyautogui
import time
import math
import threading
import tkinter as tk

# Set the time interval for checking inactivity (in seconds)
INACTIVITY_THRESHOLD = 3  # 3 seconds

# Flag to control the movement of the mouse
move_mouse_flag = False

# Function to move the mouse pointer in a circular motion with a smaller circle radius
def move_mouse():
    global move_mouse_flag
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width / 2, screen_height / 2
    radius = min(screen_width, screen_height) / 5  # Adjusted radius for a smaller circle

    while move_mouse_flag:
        for angle in range(0, 360, 10):  # Move in 10-degree increments
            if not check_mouse_movement():
                x = center_x + radius * math.cos(math.radians(angle))
                y = center_y + radius * math.sin(math.radians(angle))
                pyautogui.moveTo(x, y, duration=0.1)
                if not move_mouse_flag:  # Check if movement should stop
                    break
            else:
                break

# Function to check for mouse movement
def check_mouse_movement():
    current_mouse_position = pyautogui.position()
    time.sleep(0.5)  # Wait for a short interval to check for movement again
    new_mouse_position = pyautogui.position()
    return current_mouse_position != new_mouse_position

# Function to check for mouse movement and inactivity
def check_activity():
    global move_mouse_flag
    last_activity_time = time.time()
    while True:
        current_time = time.time()
        # Check if the time since last activity exceeds the threshold
        if current_time - last_activity_time > INACTIVITY_THRESHOLD and move_mouse_flag:
            move_mouse()  # Move the mouse pointer
            last_activity_time = time.time()  # Update last activity time
        time.sleep(1)  # Check every second

# Function to start moving the mouse
def start_mouse():
    global move_mouse_flag
    move_mouse_flag = True
    # Change button color to green to indicate "START" state
    start_button.config(bg="green")
    stop_button.config(bg="SystemButtonFace")  # Reset stop button color

    # Start a separate thread to move the mouse
    mouse_thread = threading.Thread(target=move_mouse)
    mouse_thread.start()

# Function to stop moving the mouse
def stop_mouse():
    global move_mouse_flag
    move_mouse_flag = False
    # Change button color to red to indicate "STOP" state
    stop_button.config(bg="red")
    start_button.config(bg="SystemButtonFace")  # Reset start button color

if __name__ == "__main__":
    # Create the Tkinter GUI window
    root = tk.Tk()
    root.title("Mouse Mover")

    # Add start button
    start_button = tk.Button(root, text="START", command=start_mouse, bg="SystemButtonFace")
    start_button.pack()

    # Add stop button
    stop_button = tk.Button(root, text="STOP", command=stop_mouse, bg="SystemButtonFace")
    stop_button.pack()

    # Start a separate thread to check for mouse movement and inactivity
    activity_thread = threading.Thread(target=check_activity)
    activity_thread.start()

    # Start the Tkinter event loop
    root.mainloop()
