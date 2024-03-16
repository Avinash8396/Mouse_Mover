# Mouse_Mover
Mouse Mover is an application which won't all your computer to sleep. 


#For building a standalone executable on Windows, you can follow these steps:

pip install pyinstaller

#Navigate to Your Script's Directory: Open a command prompt and navigate to the directory containing your Python script (mouse_mover.py).
Note: mouse_mover.py is the python app file.

Run PyInstaller: Run PyInstaller with the following command:

pyinstaller --onefile --windowed mouse_mover.py  

--onefile: This option tells PyInstaller to bundle everything into a single executable file.
--windowed: This option tells PyInstaller to hide the console window when the program runs, making it appear like a traditional GUI application.

Locate the Executable: After PyInstaller finishes, you'll find the standalone executable file (mouse_mover.exe) in the dist directory within your script's directory.

Run the Executable: You can now run the executable (mouse_mover.exe). Double-click on it, and it will display the GUI and function just like your Python script.




