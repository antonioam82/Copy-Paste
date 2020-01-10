from tkinter import filedialog
import time
import sys
import pyperclip

def guardar(p):
    guardar = filedialog.asksaveasfilename(initialdir = "/",
              title = "Elija destino", defaultextension = ".txt",
              filetypes = (("txt files","*.txt"),
                           ("all files","*.*")))
    with open(guardar,'a') as f:
        f.write('{}\n$\n'.format(p))

last_paste = pyperclip.paste().strip()

while True:
    time.sleep(0.1)
    paste = pyperclip.paste().strip()
    if paste != last_paste:
        try:
            guardar(paste)
            last_paste = paste
        except Exception as e:
            sys.stderr.write("Error: {}".format(e))
            break
