import pyperclip
import pyshorteners
from tkinter import *


root=Tk()
root.geometry("800x400")
root.title("Shorten your URL here")
root.configure(bg="yellow")


url=StringVar()
url_add=StringVar()


def short():
    urladd=url.get()
    url_short=pyshorteners.Shortener().tinyurl.short(urladd)
    url_add.set(url_short)


def copyu():
    url_short=url_add.get()
    pyperclip.copy(url_short)


Label(root, text="URL Shortener", font="Arial").pack(pady=20)
Entry(root, textvariable=url).pack(pady=10)
Button(root, text="Shorten URL", command=short).pack(pady=7)
Entry(root, textvariable=url_add).pack(pady=10)
Button(root, text="Copy", command=copyu).pack(pady=7)

root.mainloop()
