from tkinter import Tk, Label, Button, LEFT, RIGHT,font, BOTTOM
import random

class giyimMarkaları:
    def __init__(self,sayfa):
        self.sayfa=sayfa
        sayfa.title("Giyim Markaları")
        sayfa.configure(background="yellow")

        self.label= Label(sayfa, text="Giyim Markaları",font=("Arial Black",14),bg="purple")
        self.label.pack()

        self.markalar= Button(sayfa, text="İlerle",font=("Book Antiqua",11),command=self.markalar,bg="pink")
        self.markalar.pack(side=RIGHT)

        self.cıkıs=Button(sayfa, text="Kapat",font=("Arial",11),command= sayfa.quit,bg="red")
        self.cıkıs.pack(side=BOTTOM)

    def markalar(self):
        markaİsimleri=("Lc Waikiki", "KİP","Koton","Levi's","Boyner", "Süvari","Nike", "Adidas", "Aker","Barbour","Mavi","Milan Kiss","Rodi","Defacto","New Balance","Converse","Columbia","Dagi","Lacoste","Bambi","Calvin Clein","İpekyol","Ramsey","Faik Sönmez","Hummel","Nine West","Net Work","QUE","Twist")
        markaSec=random.choice(markaİsimleri)

        self.markalar=Label(self.sayfa, text=markaSec)
        self.markalar.pack()

root=Tk()
markalar=giyimMarkaları(root)
root.mainloop()
