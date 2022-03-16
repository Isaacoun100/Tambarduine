from tkinter import *
from tkinter import filedialog

class IDE:
    def __init__(self):
        #Main IDE Window
        self.ide_window = Tk()

        #The main window will run at 1080p
        self.ide_window.attributes("-fullscreen", True)

        #Uncomment the next line to disable true fullscreen
        #ide_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        #The windows will not be resizable
        self.ide_window.resizable(False, False)

        #If true fullscreen is disable this line will show the window title
        self.ide_window.title("Tambarduine IDE")

        #Escape sequence with the Esc button
        self.ide_window.bind('<Escape>', lambda e: self.onExit() )

        #Entry where the code will be
        self.code_Text=Text()

    def startIDE(self):

        #Start the Top Bar
        self.topBar()

        #Start the program canvas
        self.codeCanvas()

        #Window declaration.
        self.ide_window.mainloop()

    def codeCanvas(self):

        #Canvas creation
        myCanvas = Canvas(self.ide_window,
            width="1920", height="1080",
            bd=0, highlightthickness=0)

        self.darkMode(myCanvas)
        myCanvas.pack(fill="both", expand=True)

        #Entry where the user can program in Tambarduine
        self.code_Text = Text(self.ide_window,
            font=("Helvetica", 14),
            bg="#282C34", bd=0,
            fg="#FFFFFF",highlightthickness=0)

        self.code_Text.place(x=10, y=10, width=1850, height=800)

    def topBar(self):
        #This is the top bar where the program can be compiled, run, saved or opened
        menubar = Menu(self.ide_window)

        #Menubar declared
        self.ide_window.config(menu=menubar)

        #The file menu is being defined
        filemenu = Menu(menubar)

        #Filemenu created
        menubar.add_cascade(label="  File  ", menu=filemenu)

        #Filemenu options definition
        filemenu.add_command(label="  Open  ", command = self.onOpen)
        filemenu.add_command(label="  Save  ", command = self.onSave)
        filemenu.add_command(label="  Exit  ", command = self.onExit)

        #The file menu is being defined
        runmenu = Menu(menubar)

        #Runmenu created
        menubar.add_cascade(label="  Options  ", menu=runmenu)

        #Runmenu options definition
        runmenu.add_command(label="  Compile  ", command = self.getCode)
        runmenu.add_command(label="  Compile & Run  ", command = self.onExit)

    def onOpen(self):
        print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

    def onSave(self):
        print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

    def onExit(self):
        self.ide_window.destroy()

    def darkMode(self, myCanvas):
        myCanvas.configure(bg="#21252B")
        myCanvas.pack(fill="both", expand=True)

    def lightMode(self, myCanvas):
        myCanvas.configure(bg="#F8EFE6")
        myCanvas.pack(fill="both", expand=True)

    def getCode(self):
        code = self.code_Text.get("1.0",END)
        print(code)
