import tkinter as tk
from tkinter import ttk 
from PIL import Image,ImageTk

# @uthor - backup_python.dev


image_list = ["1.png",
            "2.png","3.png","4.png",
            "5.png","6.png","7.png",
            "8.png" 
            ]

text_list = ['León','Oso Panda', 'Ciudad', 'Nueva York',
"Hojas","Oceano","Montañas","Mujer"]

index=0
def Next(event):
    global index
    if index <len(image_list):
        index += 1
        image = Image.open(image_list[index-1])
        photo = ImageTk.PhotoImage(image)
        label['text'] = text_list[index-1]
        label['image'] = photo
        label.photo = photo
        if index==len(image_list):
            index=0


def prev(event):
    global index
    if index<len(image_list):
        if index<0:
            index=len(image_list)-1
        index-=1 
        image = Image.open(image_list[index-1])
        photo = ImageTk.PhotoImage(image)
        label['text'] = text_list[index-1]
        label['image'] = photo
        label.photo = photo
   


root = tk.Tk()

root.title("Galeria")
root.config(bg="black")                                   
root.resizable(0,0)
root.geometry("570x500")
letter="Dyuthi 20"
label = tk.Label(root,bg="black",
fg="white",font=letter,compound=tk.TOP)
label.grid(row=1,column=1)

sig = Image.open('next.png')
sig = ImageTk.PhotoImage(sig)
atras = Image.open('atras.png')
atras = ImageTk.PhotoImage(atras)

a=tk.Label(root, image=atras,bg="black")
s=tk.Label(root, image=sig, bg="black")

a.bind('<ButtonRelease>',prev)
s.bind('<ButtonRelease>',Next)
s.grid(row=1,column=2,padx=10,pady=230)
a.grid(row=1,column=0,padx=10)
root.bind('<Left>',prev)
root.bind('<Right>',Next)
Next(True)

root.mainloop()