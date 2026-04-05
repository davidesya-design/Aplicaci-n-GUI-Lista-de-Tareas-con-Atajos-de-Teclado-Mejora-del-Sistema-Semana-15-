import sys
import os
sys.path.append(os.path.dirname(__file__))

from ui.app_tkinter import AppTkinter
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = AppTkinter(root)
    root.mainloop()