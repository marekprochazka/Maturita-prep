import tkinter as tk


def show_help():
    help_win = tk.Toplevel()
    help_win.title("LUL")
    help_win.geometry("300x100+300+200")
    help_info = tk.Label(help_win, text="If žalud sees this. We won ZULUL")
    help_info.pack()

def lbl_text(text,label):
    label.config(text=text)

def lbl_color(color, label):
    label.config(bg=color)

main = tk.Tk()

main_label = tk.Label(main, text="",bg="white")

menu = tk.Menu(main)

submenu_text = tk.Menu(menu, tearoff=0)
submenu_text.add_command(label="Spirng", command=lambda: lbl_text(text="Spring", label=main_label))
submenu_text.add_command(label="Summer", command=lambda: lbl_text(text="Summer", label=main_label))
submenu_text.add_command(label="Autumn", command=lambda: lbl_text(text="Autumn", label=main_label))
submenu_text.add_command(label="Winter", command=lambda: lbl_text(text="Winter", label=main_label))
menu.add_cascade(label="Text", menu=submenu_text)

submenu_color = tk.Menu(menu, tearoff=0)
submenu_color.add_command(label="Blue", command=lambda: lbl_color(color="blue", label=main_label))
submenu_color.add_command(label="Red", command=lambda: lbl_color(color="red", label=main_label))
submenu_color.add_command(label="Green", command=lambda: lbl_color(color="green", label=main_label))
submenu_color.add_separator()
submenu_color.add_command(label="White", command=lambda: lbl_color(color="white", label=main_label))
submenu_color.add_command(label="Violet", command=lambda: lbl_color(color="purple", label=main_label))
menu.add_cascade(label="Color", menu=submenu_color)

submenu_help = tk.Menu(menu, tearoff=0)
submenu_help.add_command(label="About", command=show_help)
menu.add_cascade(label="Help", menu=submenu_help)
menu.add_command(label="Exit", command = main.quit)

main_label.place(x=150,y=150, width=300, height=300)

main.config(menu=menu)
main.geometry("600x600")
main.mainloop()