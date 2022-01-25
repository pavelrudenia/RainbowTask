from tkinter import *

root =Tk()
root.title("Радуга")
root.geometry('400x223')
root.resizable(False,False)
root.config(bg='gray')
e=Entry(root,justify=CENTER)
e.pack()
l = Label(root)
l.pack()
colors = {
    'Красный':'#ff0000',
    'Оранжевый':'#ff7d00',
    'Желтый': '#ffff00',
    'Зеленый':'#00ff00',
    'Голубой':'#007dff',
    'Синий':'#0000ff',
    'Фиолетовый':'#7d00ff'
}
class MyButtons:

    def __init__(self,master,text_color,hex_color):
        self.text_color=text_color
        self.hex_color=hex_color
        self.button =Button(root, bg=hex_color, command=self.get_color)
        self.button.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)


for color,rgb in colors.items():
    MyButtons(root,color,rgb)

root.mainloop()