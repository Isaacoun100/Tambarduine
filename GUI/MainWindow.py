from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog

from Compiler import Comp


class IDE:
    __compiler = Comp()

    def __init__(self):
        # Main IDE Window
        self.ide_window = Tk()

        # The main window will run at 1080p
        self.ide_window.attributes("-fullscreen", True)

        # Uncomment the next line to disable true fullscreen
        # ide_window.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        # The windows will not be resizable
        self.ide_window.resizable(False, False)

        # If true fullscreen is disable this line will show the window title
        self.ide_window.title("Tambarduine IDE")

        # Entry where the code will be
        self.code_Text = Text()
        self.output_Text = Text()

        # Canvas creation
        myCanvas = Canvas(self.ide_window,
                          width="1920", height="1080",
                          bd=0, highlightthickness=0)

        self.darkMode(myCanvas)
        myCanvas.pack(fill="both", expand=True)

        # Key commands
        self.ide_window.bind('<Escape>', lambda e: self.onExit())
        self.ide_window.bind('<F5>', lambda e: self.getCode())

    def startIDE(self):

        # Start the Top Bar
        self.topBar()

        # Start the program canvas
        self.codeCanvas()

        # Set the output text console
        self.console()

        # Window declaration.
        self.ide_window.mainloop()

    def codeCanvas(self):

        # Entry where the user can program in Tambarduine
        self.code_Text = Text(self.ide_window,
                              font=("Helvetica", 14),
                              bg="#282C34", bd=1,  # 282C34
                              fg="#FFFFFF", highlightthickness=1)

        self.code_Text.place(x=20, y=10, width=1850, height=800)

    def topBar(self):
        # This is the top bar where the program can be compiled, run, saved or opened
        menubar = Menu(self.ide_window)

        # Menubar declared
        self.ide_window.config(menu=menubar)

        # The file menu is being defined
        filemenu = Menu(menubar)

        # Filemenu created
        menubar.add_cascade(label="  File  ", menu=filemenu)

        # Filemenu options definition
        filemenu.add_command(label="  Open  ", command=self.onOpen)
        filemenu.add_command(label="  Save  ", command=self.onSave)
        filemenu.add_command(label="  Exit  ", command=self.onExit)

        # The run menu is being defined
        runmenu = Menu(menubar)

        # Runmenu created
        menubar.add_cascade(label="  Options  ", menu=runmenu)

        # Runmenu options definition
        runmenu.add_command(label="  Compile  ", command=self.getCode)
        runmenu.add_command(label="  Compile & Run  ", command=self.onExit)

        # The Edit menu is being defined
        editmenu = Menu(menubar)

        # Runmenu created
        menubar.add_cascade(label="  Options  ", menu=editmenu)

        # Runmenu options definition
        editmenu.add_command(label="  Go to line  ", command=self.askGoTo)

    def onOpen(self):
        path = filedialog.askopenfilename(initialdir="/", title=
        "Open file", filetypes=(("Tambarduine files", "*.tmn"),
                                ("All files", "*.*")))

        with open(path, "r") as f:
            code = ""
            for line in f:
                code += line

        self.setCode(code)

    def onSave(self):
        path = filedialog.asksaveasfilename(initialdir="/", title=
        "Save as", filetypes=(("Python files", "*.tmn;"),
                              ("All files", "*.*")))

    def onExit(self):
        self.ide_window.destroy()

    def darkMode(self, myCanvas):
        myCanvas.configure(bg="#21252B")
        myCanvas.pack(fill="both", expand=True)

    def getCode(self):

        code = self.code_Text.get("1.0", END)
        result = self.__compiler.compile(code)

        self.setConsole(result)

    def console(self):

        # Entry where the user can program in Tambarduine
        self.output_Text = Text(self.ide_window,
                                bg="#414752", bd=1,
                                fg="#FFFFFF", highlightthickness=1)
        self.output_Text.place(x=20, y=850, width=1850, height=175)

        self.setConsole("Welcome to the Tambarduine integrated development enviroment")

    def setConsole(self, message):

        # Write on the read only console
        self.output_Text.config(state=NORMAL)
        self.output_Text.insert(END, '\n' + message)
        self.output_Text.config(state=DISABLED)

    def setCode(self, message):
        # Write on the read only console
        self.code_Text.delete('1.0', END)
        self.code_Text.insert(END, message)

    def goToLine(self, line, column):
        self.code_Text.see("%d.%d" % (line + 1, column + 1))
        self.code_Text.focus_set()

    def askGoTo(self):
        line = simpledialog.askstring("Line", "Find line", parent=self.ide_window)
        if line is not None:
            column = simpledialog.askstring("Column", "Find column", parent=self.ide_window)
            if column is not None:
                self.goToLine(int(line), int(column))
