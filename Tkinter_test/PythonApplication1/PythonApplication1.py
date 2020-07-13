import tkinter as tk

window = tk.Tk()
window.title("My App")
window.geometry("400x400")
#Label
title = tk.Label(text ="Hello world")
title.grid(column=0,row = 0)
# Button
btn1 = tk.Button(text = "Click me!")
btn1.grid(column=0,row = 1)
# Entry field
entry_field = tk.Entry()
entry_field.grid(column=0,row=2)


window.mainloop()

