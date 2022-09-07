import os
from tkinter import *
from tkinter import messagebox,colorchooser
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename


# Update Method
def Update(event):
    word_length.config(text="Word Length: {}".format(len(text_area.get("1.0",END))))

# File Menu Command Methods
def new_method():
    win.title("Untitled")
    text_area.delete(1.0,END)

def open_method():
    file = askopenfilename(title="Open Files",
        defaultextension="*.txt",
        filetypes=[("Text file","*.txt"),
        ("Python file","*.py"),
        ("Java file","*.java"),
        ("HTML file","*.html"),
        ("CSS file","*.css"),
        ("Javascript file","*.js")]
    )

    try:
        win.title(os.path.basename(file))
        text_area.delete(1.0,END)

        files = open(file,"r")
        r = files.read()
        
        text_area.insert(1.0,r)
        word_length.config(text="Word Length: {}".format(len(text_area.get("1.0",END))))
    except Exception:
        messagebox.showwarning("Display File","Could not show file")
    

def saveas_method():
    file  = asksaveasfilename(
        title="Save_As",
        defaultextension="*.txt",
        filetypes=[("Text file","*.txt"),
        ("Python file","*.py"),
        ("Java file","*.java"),
        ("HTML file","*.html"),
        ("CSS file","*.css"),
        ("Javascript file","*.js")]
    )

    try:
        win.title(os.path.basename(file))
        file = open(file,"w")
        file.write(text_area.get(1.0,END))
    except Exception:
        messagebox.showwarning("Save File","Couldn't save file")

def close_method():
    win.destroy()


# Alter Menu Command Methods
def copy_method():
    text_area.event_generate("<<Copy>>")

def cut_method():
    text_area.event_generate("<<Cut>>")

def paste_method():
    text_area.event_generate("<<Paste>>")

def select_method():
    text_area.tag_add('select_all','1.0',END)
    text_area.tag_config('select_all',background="wheat",foreground="white")


def deselect(event):
    text_area.tag_config('select_all',background="",foreground="")

def clear_method():
    text_area.event_generate("<<Clear>>")



# Personalize Menu Command Methods
def color_method():
    colors = colorchooser.askcolor(title="Pick a color")
    text_area.config(fg=colors[1])

def font_method():
    def change_font(*args):
        text_area.config(font=(font_var.get()))
    top_level = Toplevel(win)
    top_level.title("Font")
    top_level.geometry("330x100")
    font_label = Label(top_level,text="Fonts:")
    font_box = OptionMenu(top_level,font_var, *font.families(),command=change_font)

    font_label.grid(row=1,column=10,padx=30,pady=40)
    font_box.grid(row=1,column=20,sticky=W + E)
    

def size_method():
    def change_size(*args):
        get_size = int(size_box.get())
        text_area.config(font=("",get_size))
    top_levels = Toplevel(win)
    top_levels.title("Size")
    top_levels.geometry("250x100")
    size_label = Label(top_levels,text="Size:")
    size_box = Spinbox(top_levels,from_=0,to=100,textvariable=size_var,command=change_size)

    size_label.grid(row=1,column=10,padx=30,pady=40)
    size_box.grid(row=1,column=20,sticky=W + E)

win = Tk()
win.geometry("650x400")
win.title("Liner")
win.resizable(1,1)
win.iconbitmap(f'{os.getcwd()}/text-editor.ico')


# Add Menu
main_menu = Menu(win)

file_menu = Menu(main_menu,tearoff=0)
file_menu.add_command(label="New",command=new_method)
file_menu.add_command(label="Open",command=open_method)
file_menu.add_command(label="Save As",command=saveas_method)
file_menu.add_separator()
file_menu.add_command(label="Close",command=close_method)


main_menu.add_cascade(label="File", menu=file_menu)

# Ater Menu
alter_menu = Menu(main_menu,tearoff=0)
alter_menu.add_command(label="Copy",command=copy_method)
alter_menu.add_command(label="Cut",command=cut_method)
alter_menu.add_command(label="Paste",command=paste_method)
# alter_menu.add_command(label="Select All",command=select_method)
alter_menu.add_command(label="Clear",command=clear_method)

main_menu.add_cascade(label="Alter",menu=alter_menu)

# Personalize Menu
personalize_menu = Menu(main_menu,tearoff=0)
personalize_menu.add_command(label="Color",command= color_method)
personalize_menu.add_command(label="Font",command=lambda :font_method())
personalize_menu.add_command(label="Size",command=size_method)

main_menu.add_cascade(label="Personalize",menu=personalize_menu)

# Other Codes
font_var = StringVar(win)
font_var.set("Arial")

size_var = IntVar(win)
size_var.set(12)

text_area = Text(win,font=(font_var.get(), size_var.get()))
text_area.grid(sticky=N + E + S + W)


win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)


scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT,fill=Y)

text_area.config(yscrollcommand=scroll_bar.set)

main_frame = Frame(win)
main_frame.grid()

word_length = Label(main_frame,text="")
word_length.config(text="Word Length: ")

text_area.bind('<KeyPress>',Update)
text_area.bind('<KeyRelease>',Update)
text_area.bind('<Button-1>',deselect)
if text_area.tag_config('select',background='',foreground=""):
    text_area.tag_add('sellect')



word_length.grid(column=5)
win.config(menu=main_menu)
win.mainloop()