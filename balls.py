import tkinter as tk
import subprocess
import os
import platform

if platform.system() == "Windows":
    def clean_temp_folder():
        try:
            subprocess.run('del /s /q /f "%temp%\\*.*"', shell=True)
            result_label.config(text="Temporary files cleaned successfully.")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    def open_youtube_link():
        subprocess.run('start https://www.youtube.com/watch?v=YVNiYnEQ5lA', shell=True)

    def shutdown_pc():
        try:
            subprocess.run('shutdown /s /c "Time to rest" /f', shell=True)
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    def lockstation():
        try:
            subprocess.run(args='Rundll32.exe user32.dll,LockWorkStation', shell=True)
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")


    def WinAudio():
        try:
            cmd = ('runas /noprofile /user:administrator "net stop audiosrv && net start audiosrv"')
            os.system(cmd)
            result_label.config(text=f"WinAudio restarted successfully")
            result_label.grid(column=1,row=9)
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    def update_prompt():
        prompt_text = prompt_entry.get()
        prompt_label.config(text=prompt_text)



    # Create a basic tkinter window
    window = tk.Tk()
    window.title("Utility GUI")
    window.geometry("412x240")
    window.resizable(0,0)

    # Create a label to display results or errors
    result_label = tk.Label(window, text="")

    # Create a label and an entry for the text prompt
    prompt_label = tk.Label(window, text="Enter a prompt:")
    prompt_entry = tk.Entry(window, width=30)
    update_button = tk.Button(window, text="Update Prompt", command=update_prompt)

    # Create buttons
    button1 = tk.Button(window, text="Temp Cleaner", command=clean_temp_folder, width=15, height=2)
    button2 = tk.Button(window, text="Void", command=open_youtube_link, width=15, height=2)
    button3 = tk.Button(window, text="Shutdown", command=shutdown_pc, width=15, height=2)
    button4 = tk.Button(window, text="Lock PC", command=lockstation, width=15, height=2)
    button5 = tk.Button(window, text="Restart Audio", command=WinAudio, width=15, height=2)

    # Pack the text prompt widgets
    prompt_label.grid(column=1, row=1)
    update_button.grid(column=1, row=3)
    prompt_entry.grid(column=1, row=2)

    # Set focus on the text entry and provide default text
    prompt_entry.insert(0, "Default Prompt")
    prompt_entry.focus()

    # Create a label to display results or errors
    result_label = tk.Label(window, text="")


    # Pack the buttons and label
    button1.grid(column=0, row=3)
    button2.grid(column=0, row=4)
    button3.grid(column=0, row=5)
    button4.grid(column=0, row=6)
    button5.grid(column=2, row=3)


    result_label.grid()

    # Start the tkinter main loop
    window.mainloop()
