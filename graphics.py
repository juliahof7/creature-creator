# graphics.py

import tkinter as tk

def show_graphic(name):
    window = tk.Tk()
    window.title("Creature Confirmation")

    window.geometry("400x300")
    window.configure(bg="#e3f2fd")

    title = tk.Label(window, text="✨ Your Creature Has Been Created! ✨", font=("Arial", 14, "bold"), bg="#e3f2fd")
    title.pack(pady=20)

    name_label = tk.Label(window, text=f"Name: {name}", font=("Arial", 20), fg="#4a148c", bg="#e3f2fd")
    name_label.pack(pady=10)

    emoji = tk.Label(window, text="🦄🧬🐲", font=("Arial", 30), bg="#e3f2fd")
    emoji.pack(pady=10)

    close_button = tk.Button(window, text="Close", command=window.destroy)
    close_button.pack(pady=20)

    window.mainloop()
