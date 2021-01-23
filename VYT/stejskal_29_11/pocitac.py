from tkinter import *

def zvetsit(entry):
    entry["text"] = str(int(entry["text"]) + 1)

def zmensit(entry):
    entry["text"] = str(int(entry["text"]) - 1)

def restart(entry):
    entry["text"] = "0"

def end():
    main.quit()


main = Tk()
main.geometry("400x50")

text = Label(main,width=40,text="0")

plus = Button(main,width=10,text="+",command=lambda:zvetsit(text))
minus = Button(main,width=10,text="-",command=lambda:zmensit(text))
reset = Button(main,width=10,text="reset",command=lambda:restart(text))
end = Button(main,width=10,text="end",command=lambda:main.quit())

plus.grid(row=0 ,column=0)
minus.grid(row=0 ,column=1)
reset.grid(row=0 ,column=2)
end.grid(row=0 ,column=3)
text.grid(row=1 ,column=0,columnspan=4)

main.mainloop()
