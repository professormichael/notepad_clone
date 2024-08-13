# Importing The Important Modules Needed In This Note Pad Application
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import *
from tkinter import filedialog
import datetime
from tkinter import ttk
import tkinter
from tkinter import messagebox

# Making Use Class And Objects
class root(Tk):
    def __init__(self):
        super(root, self).__init__()
        self.minsize(800,400)
        self.maxsize(800,400)
        self.title('United - Notepad')
        # Creation Of The Menu
        #self.bind("<Control-n>", self.new)
        #self.bind("<Control-o>", self.open)
        
        #self.bind("<Control-c>", self.copy)
        #self.bind("<Control-v>", self.paste)
        #self.bind("<Delete>", self.delete)
        #self.bind("<Control-f>", self.find)
        #self.bind("<Control-h>", self.replace)
        #self.bind("<F5>", self.time)
        #self.bind("<Control-q>", self.exit)



        self.focus_set()
        menuBar = Menu()
        self.configure(menu=menuBar)
        file_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New                       Ctrl+N", command=self.new)
        file_menu.add_command(label="New Window       Ctrl+Shift+N", command=self.new1)
        file_menu.add_cascade(label="Open                     Ctrl+O", command=self.open)
        file_menu.add_command(label="Save                       Ctrl+S", command=self.save_text)
        file_menu.add_cascade(label="Save As                  Ctrl+Shift+S", command=self.save_text)
        #file_menu.add_command(label="Page Setup")
        #file_menu.add_command(label="Print                       Ctrl+P")
        file_menu.add_cascade(label="Exit                         Ctrl+Q", command=self.exit)

        # Part Of The Menu Bars
        edit_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo                       Ctrl+Z")
        edit_menu.add_command(label="Cut                          Ctrl+X")
        edit_menu.add_command(label="Copy                       Ctrl+C", command=self.copy)
        edit_menu.add_command(label="Paste                       Ctrl+V", command=self.paste)
        edit_menu.add_command(label="Delete                      Del", command=self.delete)
        edit_menu.add_command(label="Search with Bing   Ctrl+E")
        edit_menu.add_command(label="Find                         Ctrl+F", command=self.find)
        edit_menu.add_command(label="Find Previous         Shift+F3", command=self.find)
        edit_menu.add_command(label ="Replace                   Ctrl+H", command=self.replace)
        #edit_menu.add_command(label="Go To                      Ctrl+G")
        #edit_menu.add_command(label="Select All                Ctrl+A")
        edit_menu.add_command(label="Time/Date              F5", command=self.time)

        format_menu = Menu(menuBar, tearoff=0)



        menuBar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_checkbutton(label="Word Wrap")
        format_menu.add_command(label="Font ",command=self.new_window)
        view_menu = Menu(menuBar, tearoff=0)

        menuBar.add_cascade(label="View", menu=view_menu)
        self.sub_menu = Menu(view_menu, tearoff=0)
        view_menu.add_cascade(label="Zoom", menu=self.sub_menu)
        self.sub_menu.add_command(label="Zoom In                               Ctrl+Plus", command=self.zoom_in)
        self.sub_menu.add_command(label="Zoom Out                            Ctrl+Minus")
        self.sub_menu.add_command(label="Restore Default Zoom        Ctrl+0")


        view_menu.add_radiobutton(label="Status Bar")
        help_menu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=help_menu)

        self.conc()

    # Saving Text Code
    def save_text(self):
        text =self.scrolled_text.get("1.0", END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"), ("All Files", "*.*")])

        if file_path:
            with open(file_path,"w") as file:
                file.write(text)
            print("Text Saved Sucessfully. ")
    # Creation Of The Scrolled Text
    def conc(self):

        self.scrolled_text = scrolledtext.ScrolledText(self, width=100 )
        self.scrolled_text.pack()
    # New Window

    def new(self):
        self.destroy()
        self.after(300, self.__init__())
    def new1(self):
        self.destroy()
        self.after(300, self.__init__())

    # Open Files



    def open(self):

        a2 = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"), ("All Files", "*.*")])
        self.title = f'United{a2.title()}'
        print(a2.title(), self.title)
        self.scrolled_text.delete("1.0",END)
        if a2:
            with open(a2,"r") as file:
                a3 = file.read()
                self.scrolled_text.insert("1.0", a3)
    # Exit The Window
    def exit(self):
        self.destroy()

    # Delete  The Text
    def delete(self):
        self.scrolled_text.delete("1.0", END)
    # Find Time
    def time(self):
        self.scrolled_text.insert("1.0",datetime.datetime.now())

    # New Window
    def new_window(self):

        root1 = Tk()
        root1.title("Font")
        root1.minsize(400,250)

        # Button Configuration
        def but():
            self.a2.configure(font=self.a2.get()+self.a4.get())
            print(self.a2.configure())
            print(self.scrolled_text.get("1.0", END))
            self.scrolled_text.configure(font=self.a2.get() + self.a4.get())
            self.scrolled_text.configure(font=self.a2.get() + self.a4.get())
        self.label = Label(root1, text="Font")
        self.label.pack(anchor="center", side="left" )
        self.a2 = ttk.Combobox(root1,values=["Adobe", "Roman", "Arial", "Consolas"])
        self.a2.pack(side="left", anchor="center")
        self.label2 = Label(root1, text="Size")
        self.label2.pack(anchor="center", side="left")
        self.a4 = ttk.Combobox(root1, values=[" 11", " 12", " 14", " 16"," 18"," 20"," 22"," 24"," 28"," 36"," 72"])
        self.a4.pack(side="left", anchor="center")
        self.but = Button(root1, text="Test", command=but)
        self.but.pack(anchor="sw", side="left")
        self.font = self.a2.get()+self.a4.get()


       # New Window Assigned
        root1.mainloop()
    # Zoom In
    def zoom_in(self):

        print(self.scrolled_text.clipboard_get())
        print(self.scrolled_text.count("1.0", END))
    # Copy The Text
    def copy(self):
        self.scrolled_text.clipboard_append(self.scrolled_text.get("1.0", END))
    # Paste The Copied Text
    def paste(self):

        s3 = self.scrolled_text.clipboard_get()

        self.scrolled_text.insert("1.0", s3)
    # Find A Particular Text
    # New Window For Finding Text
    def find(self):


        root3 = Tk()
        root3.title("Find")
        root3.minsize(150, 150)
        # Button Assigned
        def but1():
            a4 = self.scrolled_text.search(exact=TRUE, pattern=self.a2.get(), index="1.0")
            self.label3.configure(text="The Find Text Is In Row "+a4,foreground="black", font="Roman 15")
        def but2():
            root3.destroy()


        self.label1 = Label(root3, text="Find")
        self.label1.pack(anchor="center", side="left")
        self.a2 = ttk.Entry(root3,width=30, font="Roman 14")
        self.a2.pack(side="left", anchor="center")
        self.button2 = Button(root3, text="Find Next", command=but1)
        self.button2.pack(anchor="center", side="left", pady=20)
        #self.a4 = ttk.Combobox(root1,
         #                      values=[" 11", " 12", " 14", " 16", " 18", " 20", " 22", " 24", " 28", " 36", " 72"])
        #self.a4.pack(side="left", anchor="center")
        self.label3 = Label(root3, text="", foreground="white")
        self.label3.pack(anchor="nw", side="top")
        self.but = Button(root3, text="Cancel", command=but2)
        self.but.pack(anchor="center", side="left")
        self.rad1 = ttk.Radiobutton(root3, text="Up")
        self.rad1.pack(anchor="sw", side="left")
        self.rad2 = ttk.Radiobutton(root3, text="Down")
        self.rad2.pack(anchor="sw", side="left")
        self.check = ttk.Checkbutton(root3, text="Match Case")
        self.check.pack(anchor="sw", side="left")
        self.check1 = ttk.Checkbutton(root3, text="Wrap Around")
        self.check1.pack(anchor="sw", side="left")



        # New Window Mainloop
        root3.mainloop()
    # Text Replace Code
    # New Window
    def replace(self):
        root4 = Tk()
        root4.title("Find")
        root4.minsize(150, 150)
        #Button
        def but1():
            if self.a2.get() in self.scrolled_text.get("1.0",END):
                
                A2 = self.scrolled_text.get("1.0",END)
                A3 =  A2.replace(self.a2.get(), self.a3.get())
                A4 =  self.scrolled_text.clipboard_append(A3)
                A5 = self.scrolled_text.delete("1.0",END)
                A6 = self.scrolled_text.clipboard_get()
                A7 = self.scrolled_text.insert("1.0", A6)
                print(A7)




        def but2():
            root4.destroy()

        self.label1 = Label(root4, text="Replace")
        self.label1.pack(anchor="center", side="left")
        self.a2 = ttk.Entry(root4, width=30, font="Roman 14")
        self.a2.pack(side="left", anchor="center")
        self.a3 = ttk.Entry(root4, width=30, font="Roman 14")
        self.a3.pack(side="left", anchor="center")
        self.button2 = Button(root4, text="Replace", command=but1)
        self.button2.pack(anchor="center", side="left", pady=20)
        # self.a4 = ttk.Combobox(root1,
        #                      values=[" 11", " 12", " 14", " 16", " 18", " 20", " 22", " 24", " 28", " 36", " 72"])
        # self.a4.pack(side="left", anchor="center")
        self.label3 = Label(root4, text="", foreground="white")
        self.label3.pack(anchor="nw", side="top")
        self.but = Button(root4, text="Cancel", command=but2)
        self.but.pack(anchor="center", side="left")

        root4.mainloop()


#Every Window Assignment

root2 = root()

root2.mainloop()