from tkinter import *
from PIL import Image, ImageTk
album = Tk()
album.title("Kapadokya Fotoğraf Albümü")


kapadokya1 = ImageTk.PhotoImage(Image.open("kapadokya1.jpg"))
kapadokya2 = ImageTk.PhotoImage(Image.open("kapadokya2.jpg"))


etiket = Label(album, text="Kapadokya Fotoğraf Albümü")
etiket.pack()

def ileri():
    if display == kapadokya1:
        panel1.configure(image=kapadokya2)
    else:
        panel1.configure(image= kapadokya1)

ileributon = Button(album, text="İleri", font = ("Arial Black", 24), command=ileri)
ileributon.pack(side="right")

def geri():
    if display2 == kapadokya2:
        panel1.configure(image = kapadokya1)
    else:
        panel1.configure(image = kapadokya2)

geributon = Button(album, text="Geri", font = ("Arial Black", 24), command=geri)
geributon.pack(side="left")

panel1 = Label(album, image=kapadokya1)
display = kapadokya1
panel1.pack(side="top")

panel2 = Label(album, image=kapadokya2)
display2 = kapadokya2


album.mainloop()
