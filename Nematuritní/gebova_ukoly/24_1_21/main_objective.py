import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.menu = tk.Menu(self)

        self.submenu_text = tk.Menu(self.menu, tearoff=0)
        self.submenu_text.add_command(label="Spirng", command=lambda: self.__lbl_text(text="Spring"))
        self.submenu_text.add_command(label="Summer", command=lambda: self.__lbl_text(text="Summer"))
        self.submenu_text.add_command(label="Autumn", command=lambda: self.__lbl_text(text="Autumn"))
        self.submenu_text.add_command(label="Winter", command=lambda: self.__lbl_text(text="Winter"))
        self.menu.add_cascade(label="Text", menu=self.submenu_text)

        self.submenu_color = tk.Menu(self.menu, tearoff=0)
        self.submenu_color.add_command(label="Blue", command=lambda: self.__lbl_color(color="blue"))
        self.submenu_color.add_command(label="Red", command=lambda: self.__lbl_color(color="red"))
        self.submenu_color.add_command(label="Green", command=lambda: self.__lbl_color(color="green"))
        self.submenu_color.add_separator()
        self.submenu_color.add_command(label="White", command=lambda: self.__lbl_color(color="white"))
        self.submenu_color.add_command(label="Violet", command=lambda: self.__lbl_color(color="purple"))
        self.menu.add_cascade(label="Color", menu=self.submenu_color)

        self.submenu_help = tk.Menu(self.menu, tearoff=0)
        self.submenu_help.add_command(label="About", command=self.__show_help)
        self.menu.add_cascade(label="Help", menu=self.submenu_help)

        self.menu.add_command(label="Exit", command = self.quit)

        self.label = tk.Label(text="",bg="white")
        self.label.place(x=150,y=150, width=300, height=300)

        self.config(menu=self.menu)

    def __lbl_text(self,text):
        self.label.config(text=text)
        

    def __lbl_color(self,color):
        self.label.config(bg=color)

    def __show_help(self):
        help_win = tk.Toplevel()
        help_win.title("LUL")
        help_win.geometry("300x100+300+200")
        help_info = tk.Label(help_win, text="If žalud sees this. We won ZULUL")
        help_info.pack()




app = Main()
app.geometry("600x600")
app.mainloop()