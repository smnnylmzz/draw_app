from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

class CizimUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Çizim Uygulaması")
        self.root.configure(background="white")

        self.pointer = "black"
        self.erase = "white"

        # Uygulama başlığı
        text = Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial', 25), background='#292826', foreground='orange')
        text.insert("1.0", "Çizim Uygulaması")
        text.tag_add("tag_name", "1.0", "end")
        text.pack()

        # Renk seçenekleri
        self.renk_secimi = LabelFrame(self.root, text='Renkler', font=('arial', 15), bd=5, relief=RIDGE, bg="white")
        self.renk_secimi.place(x=0, y=40, width=90, height=185)

        renkler = ['blue', 'red', 'green', 'orange', 'purple', 'black', 'yellow', 'pink', 'gold', 'brown']
        i = j = 0
        for renk in renkler:
            Button(self.renk_secimi, bg=renk, bd=2, relief=RIDGE, width=3, command=lambda col=renk: self.renk_sec(col)).grid(row=i, column=j)
            i += 1
            if i == 6:
                i = 0
                j = 1

        # Silgi düğmesi
        self.silgi_btn = Button(self.root, text="Silgi", bd=4, bg='white', command=self.silgi, width=9, relief=RIDGE)
        self.silgi_btn.place(x=0, y=197)

        # Ekranı temizle düğmesi
        self.ekrani_temizle = Button(self.root, text="Ekranı Temizle", bd=4, bg='white', command=lambda: self.background.delete('all'), width=9, relief=RIDGE)
        self.ekrani_temizle.place(x=0, y=227)

        # Ekran görüntüsü kaydet düğmesi
        self.kaydet_btn = Button(self.root, text="Ekran Görüntüsü", bd=4, bg='white', command=self.cizimi_kaydet, width=9, relief=RIDGE)
        self.kaydet_btn.place(x=0, y=257)

        # Arkaplan rengi düğmesi
        self.arkaplan_btn = Button(self.root, text="Arkaplan", bd=4, bg='white', command=self.arkaplan_rengi, width=9, relief=RIDGE)
        self.arkaplan_btn.place(x=0, y=287)

        # Boyut ayarı
        self.boyut_cubugu = LabelFrame(self.root, text='Boyut', bd=5, bg='white', font=('arial', 15, 'bold'), relief=RIDGE)
        self.boyut_cubugu.place(x=0, y=320, height=200, width=70)

        self.boyut = Scale(self.boyut_cubugu, orient=VERTICAL, from_=48, to=0, length=168)
        self.boyut.set(1)
        self.boyut.grid(row=0, column=1, padx=15)

        # Çizim alanı
        self.background = Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=470, width=680)
        self.background.place(x=80, y=40)

        self.background.bind("<B1-Motion>", self.ciz)

    def ciz(self, event):
        x1, y1 = (event.x-2), (event.y-2)
        x2, y2 = (event.x+2), (event.y+2)
        self.background.create_oval(x1, y1, x2, y2, fill=self.pointer, outline=self.pointer, width=self.boyut.get())

    def renk_sec(self, renk):
        self.pointer = renk

    def silgi(self):
        self.pointer = self.erase

    def arkaplan_rengi(self):
        renk = colorchooser.askcolor()
        self.background.configure(background=renk[1])
        self.erase = renk[1]

    def cizimi_kaydet(self):
        try:
            dosya_ss = filedialog.asksaveasfilename(defaultextension='jpg')
            x = self.root.winfo_rootx() + self.background.winfo_x()
            y = self.root.winfo_rooty() + self.background.winfo_y()
            x1 = x + self.background.winfo_width()
            y1 = y + self.background.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(dosya_ss)
            messagebox.showinfo('Ekran Görüntüsü Başarıyla Kaydedildi:', str(dosya_ss))
        except:
            print("Ekran görüntüsü kaydedilirken hata oluştu")

if __name__ == "__main__":
    root = Tk()
    p = CizimUygulamasi(root)
    root.mainloop()
