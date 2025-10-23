import tkinter as tk
from PIL import Image, ImageTk
import random as rd
import os 

window = tk.Tk()
window.title("hampter_randomizer")
window.geometry("400x400")

label = tk.Label(window)
label.pack()

def openImage():
    folder = "/Users/kine/Downloads/hampt"
    images = [f for f in os.listdir(folder) if f.endswith(('.png'))]
    
    random_image = rd.choice(images)
    full_path = os.path.join(folder, random_image)
    
    img = Image.open(full_path) # gjør om bildet til neo tkinter kan frostå
    photo = ImageTk.PhotoImage(img)
    
    label.config(image=photo)
    label.image = photo

# def refresh_window():
#     window.update()

button = tk.Button(window, text="randomiser!!", command=openImage)
button.pack()

window.mainloop()





 