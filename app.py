import tkinter as tk

window = tk.Tk()
window.title("My Python Window")
window.geometry("400x300")

label = tk.Label(window, text="SDSA", font=("Arial", 12))
label.pack(pady=20)
button = tk.Button(window, text="graphical", command=lambda: print("uhh"))
button.pack(pady=10)

window.mainloop()