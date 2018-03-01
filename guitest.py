"""
The GUI class is a WIP gui for the encryption module. Currently served only
when the --gui flag is set in the main.py script.
"""

import tkinter
import main

class GUI(object):
    def __init__(self):
        self.master = tkinter.Tk()
        self.master.minsize(width=300, height=150)
        self.master.title("Encryption Program")
        self.do_gui()

    def create_modules(self):
        self.button = tkinter.Button(self.master, text="Encrypt!", bg="grey")
        self.label = tkinter.Label(self.master, text="Text To Encrypt: ", fg="blue")
        self.entry = tkinter.Entry(self.master, bd=5, justify='center', width=35)
        self.text = tkinter.Text(self.master, width=35, height=1)
        
    def do_gui(self):
        self.create_modules()
        self.button.pack(side='bottom')
        self.label.pack(side='left')
        self.entry.pack(side='left')
        self.text.pack(side='bottom')
        self.master.mainloop()


def main():
    myGui = GUI()
        
if __name__ ==  '__main__':
    main()


        

