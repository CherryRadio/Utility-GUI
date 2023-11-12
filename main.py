import customtkinter
import tkinter as tk
import subprocess
import os
import platform

if platform.system() == "Windows":
    def clean_temp_folder():
        try:
            subprocess.run('del /s /q /f "%temp%\\*.*"', shell=True)
            result_label.configure(text="Temp files removed.")
        except Exception as e:
            result_label.configure(text=f"Error: {str(e)}")

    def open_youtube_link():
        subprocess.run('start https://www.youtube.com/watch?v=YVNiYnEQ5lA', shell=True)

    def shutdown_pc():
        try:
            subprocess.run('shutdown /s /c "Time to rest" /f', shell=True)
        except Exception as e:
            result_label.configure(text=f"Error: {str(e)}")

    def lockstation():
        try:
            subprocess.run(args='Rundll32.exe user32.dll,LockWorkStation', shell=True)
        except Exception as e:
            result_label.configure(text=f"Error: {str(e)}")

    def update_prompt():
        prompt_text = prompt_entry.get()
        prompt_label.configure(text=prompt_text)



    # Create a basic tkinter window
    window = customtkinter.CTk()
    from PIL import Image 
  
    urllib.request.urlretrieve( 
  'https://raw.githubusercontent.com/CherryRadio/Utility-GUI/main/icon.ico', 
   "icon.ico") 
  
    icon = Image.open("icon.ico") 
    window_icon = tk.PhotoImage(file= icon)
    window.iconbitmap(False, icon)
    window.title("Utility GUI")
    window.geometry("412x240")
    window.resizable(0,0)

    # Create a label to display results or errors
    result_label = customtkinter.CTkLabel(window, text="")

    # Create a label and an entry for the text prompt
    prompt_label = customtkinter.CTkLabel(window, text="Enter a prompt:")
    prompt_entry = customtkinter.CTkEntry(window)
    update_button = customtkinter.CTkButton(window, text="Update Prompt", command=update_prompt)

    # Create buttons
    button1 = customtkinter.CTkButton(window, text="Temp Cleaner", command=clean_temp_folder)
    blank1 = customtkinter.CTkLabel(window, text=" ", height=3)
    button2 = customtkinter.CTkButton(window, text="Void", command=open_youtube_link)
    blank2 = customtkinter.CTkLabel(window, text=" ", height=3)
    button3 = customtkinter.CTkButton(window, text="Shutdown", command=shutdown_pc)
    blank3 = customtkinter.CTkLabel(window, text=" ", height=3)
    button4 = customtkinter.CTkButton(window, text="Lock PC", command=lockstation)
    # Right
    """
    button5 = customtkinter.CTkButton(window, text="Button")
    blank5 = customtkinter.CTkLabel(window, text=" ", height=3)
    button6 = customtkinter.CTkButton(window, text="Button")
    blank6 = customtkinter.CTkLabel(window, text=" ", height=3)
    button7 = customtkinter.CTkButton(window, text="Button")
    blank7 = customtkinter.CTkLabel(window, text=" ", height=3)
    button8 = customtkinter.CTkButton(window, text="Button")
    """
    # Pack the text prompt widgets
    prompt_label.grid(column=3, row=1)
    prompt_entry.grid(column=3, row=2)
    update_button.grid(column=3, row=3)

    # Set focus on the text entry and provide default text
    prompt_entry.insert(0, "Default Prompt")
    prompt_entry.focus()

    # Create a label to display results or errors
    result_label = customtkinter.CTkLabel(window, text="")


    # Pack the buttons and label
    # Left
    button1.grid(column=1, row=4)
    blank1.grid(column=1, row=5)
    button2.grid(column=1, row=6)
    blank2.grid(column=1, row=7)
    button3.grid(column=1, row=8)
    blank3.grid(column=1, row=9)
    button4.grid(column=1, row=10)
    # Right
    """
    button5.grid(column=4, row=4)
    blank1.grid(column=4, row=5)
    button6.grid(column=4, row=6)
    blank2.grid(column=4, row=7)
    button7.grid(column=4, row=8)
    blank3.grid(column=4, row=9)
    button8.grid(column=4, row=10)
    """

    result_label.grid(column=3, row=10)

    # Start the tkinter main loop
    window.mainloop()

elif platform.system() == "Linux":
    os.system('xdg-open https://www.youtube.com/watch?v=WIRK_pGdIdA')
