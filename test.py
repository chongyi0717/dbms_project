import tkinter as tk

class SubWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        x = tk.Text(self)
        x.pack()

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.win1 = SubWindow(self)
        self.win1.pack(side="top")
        self.win2 = SubWindow(self)
        self.win2.pack(side="bottom")

if __name__ == "__main__":
    main = MainWindow()
    main.mainloop()
