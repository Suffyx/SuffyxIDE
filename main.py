from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
import subprocess

# import idlelib.colorizer as ic
# import idlelib.percolator as i
import re
import tkinter

from pygments.lexers.python import PythonLexer
# from pygments.lexers.special import TextLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.html import XmlLexer
from pygments.lexers.templates import HtmlPhpLexer
from pygments.lexers.perl import Perl6Lexer
from pygments.lexers.ruby import RubyLexer
# from pygments.lexers.configs import IniLexer
# from pygments.lexers.configs import ApacheConfLexer
from pygments.lexers.shell import BashLexer
# from pygments.lexers.diff import DiffLexer
from pygments.lexers.dotnet import CSharpLexer
from pygments.lexers.sql import MySqlLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.c_cpp import CLexer
from pygments.lexers.c_cpp import CppLexer
from pygments.lexers.css import CssLexer

from pygments.styles import get_style_by_name
from tkinter import font

# create an instance for window
window = Tk()
# set title for window
window.title("Suffyx IDE")
# create and configure menu
menu = Menu(window)
window.config(menu=menu)
# create editor window for writing code
editor = ScrolledText(window, font=("haveltica 10 bold"), wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
file_path = ""

# cdg = ic.ColorDelegator()
# cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
# cdg.idprog = re.compile(r'\s+(\w+)', re.S)

# cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F'}

# # These five lines are optional. If omitted, default colours are used.
# cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000'}
# cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00'}
# cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00'}
# cdg.tagdefs['STRING'] = {'foreground': '#7F3F00'}
# cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F'}

# ip.Percolator(editor).insertfilter(cdg)
# function to open files
def open_file(event=None):
    global code, file_path
    # code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)


window.bind("<Control-o>", open_file)
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == "":
        save_path = asksaveasfilename(
            defaultextension=".py", filetypes=[("Python File", "*.py")]
        )
        file_path = save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)


window.bind("<Control-s>", save_file)
# function to save files as specific name
def save_as(event=None):
    global code, file_path
    # code = editor.get(1.0, END)
    save_path = asksaveasfilename(
        defaultextension=".py", filetypes=[("Python File", "*.py")]
    )
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code)


window.bind("<Control-S>", save_as)
# function to execute the code and
# display its output
def run(event=None):
    global code, file_path
    """
    code = editor.get(1.0, END)
    exec(code)
    """
    cmd = "python {file_path}".format(file_path=file_path)
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    # delete the previous text from
    # output_windows
    output_window.delete(1.0, END)
    # insert the new output text in
    # output_windows
    output_window.insert(1.0, output)
    # insert the error text in output_windows
    # if there is error
    output_window.insert(1.0, error)


window.bind("<F5>", run)
# function to close IDE window
def close(event=None):
    window.destroy()


window.bind("<Control-q>", close)
# define function to cut
# the selected text
def cut_text(event=None):
    editor.event_generate(("<<Cut>>"))


# define function to copy
# the selected text
def copy_text(event=None):
    editor.event_generate(("<<Copy>>"))


# define function to paste
# the previously copied text
def paste_text(event=None):
    editor.event_generate(("<<Paste>>"))


# create menus
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
language_menu = Menu(menu, tearoff=0)
# add menu labels
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label="View", menu=view_menu)
menu.add_cascade(label="Theme", menu=theme_menu)
menu.add_cascade(label="Language", menu=language_menu)
# add commands in flie menu
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)
# add commands in edit menu
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
run_menu.add_command(label="Run", accelerator="F5", command=run)
# function to display and hide status bar
show_status_bar = BooleanVar()
show_status_bar.set(True)


def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side=BOTTOM)
        show_status_bar = True


view_menu.add_checkbutton(
    label="Status Bar",
    onvalue=True,
    offvalue=0,
    variable=show_status_bar,
    command=hide_statusbar,
)
# create a label for status bar
status_bars = ttk.Label(
    window, text="www.bulshit.software \t\t\t\t\t\t characters: 0 words: 0"
)
status_bars.pack(side=BOTTOM)
# function to display count and word characters
text_change = False


def change_word(event=None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ", ""))
        status_bars.config(
            text="www.bullshit.software \t\t\t\t\t\t characters: {character} words: {word}".format(
                character=chararcter, word=word
            )
        )
    editor.edit_modified(False)


editor.bind("<<Modified>>", change_word)
# function for light mode window
def light():
    editor.config(bg="white", fg="black")
    output_window.config(bg="white", fg="black")


# function for dark mode window
def dark():
    editor.config(fg="white", bg="#2c2f33")
    output_window.config(fg="white", bg="#2c2f33")


def ultra_dark():
    editor.config(fg="white", bg="black")
    output_window.config(fg="white", bg="black")


# add commands to change themes
theme_menu.add_command(label="light", command=light)
theme_menu.add_command(label="dark", command=dark)
theme_menu.add_command(label="ultra dark", command=ultra_dark)
# create output window to display output of written code
output_window = ScrolledText(window, height=10)
output_window.pack(fill=BOTH, expand=1)


def create_tags():
    """
    thmethod creates the tags associated with each distinct style element of the
    source code 'dressing'
    """
    bold_font = font.Font(editor, editor.cget("font"))
    bold_font.configure(weight=font.BOLD)
    italic_font = font.Font(editor, editor.cget("font"))
    italic_font.configure(slant=font.ITALIC)
    bold_italic_font = font.Font(editor, editor.cget("font"))
    bold_italic_font.configure(weight=font.BOLD, slant=font.ITALIC)
    style = get_style_by_name("default")

    for ttype, ndef in style:
        tag_font = None

        if ndef["bold"] and ndef["italic"]:
            tag_font = bold_italic_font
        elif ndef["bold"]:
            tag_font = bold_font
        elif ndef["italic"]:
            tag_font = italic_font

        if ndef["color"]:
            foreground = "#%s" % ndef["color"]
        else:
            foreground = None

        editor.tag_configure(str(ttype), foreground=foreground, font=tag_font)


create_tags()


def lang_py():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = PythonLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_js():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = JavascriptLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_java():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = JavaLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_c():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = CLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_cpp():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = CppLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_cs():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = CSharpLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_html():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = HtmlLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_css():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = CssLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_xml():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = XmlLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_sql():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = MySqlLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_bash():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = BashLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_perl():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = Per16Lexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_php():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = HtmlPhpLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


def lang_ruby():
    """
    this method colors and styles the prepared tags
    """
    code = editor.get("1.0", "end-1c")
    tokensource = RubyLexer().get_tokens(code)
    start_line = 1
    start_index = 0
    end_line = 1
    end_index = 0

    for ttype, value in tokensource:
        if "\n" in value:
            end_line += value.count("\n")
            end_index = len(value.rsplit("\n", 1)[1])
        else:
            end_index += len(value)

        if value not in (" ", "\n"):
            index1 = "%s.%s" % (start_line, start_index)
            index2 = "%s.%s" % (end_line, end_index)

            for tagname in editor.tag_names(index1):  # FIXME
                editor.tag_remove(tagname, index1, index2)

            editor.tag_add(str(ttype), index1, index2)

        start_line = end_line
        start_index = end_index


lang_config = {"lang": "py"}

syntax = {
    "py": lang_py,
    "js": lang_js,
    "java": lang_java,
    "c": lang_c,
    "cpp": lang_cpp,
    "cs": lang_cs,
    "html": lang_html,
    "css": lang_css,
    "xml": lang_xml,
    "sql": lang_sql,
    "bash": lang_bash,
    "perl": lang_perl,
    "php": lang_php,
    "ruby": lang_ruby,
}


def set_lang_py():
    lang_config["lang"] = "py"


def set_lang_js():
    lang_config["lang"] = "js"


def set_lang_java():
    lang_config["lang"] = "java"


def set_lang_c():
    lang_config["lang"] = "c"


def set_lang_cpp():
    lang_config["lang"] = "cpp"


def set_lang_cs():
    lang_config["lang"] = "cs"


def set_lang_html():
    lang_config["lang"] = "html"


def set_lang_css():
    lang_config["lang"] = "css"


def set_lang_xml():
    lang_config["lang"] = "xml"


def set_lang_sql():
    lang_config["lang"] = "sql"


def set_lang_bash():
    lang_config["lang"] = "bash"


def set_lang_perl():
    lang_config["lang"] = "perl"


def set_lang_php():
    lang_config["lang"] = "php"


def set_lang_ruby():
    lang_config["lang"] = "ruby"


language_menu.add_command(label="Python", command=set_lang_py)
language_menu.add_command(label="Javascript/Node", command=set_lang_js)
language_menu.add_command(label="Java", command=set_lang_java)
language_menu.add_command(label="C", command=set_lang_c)
language_menu.add_command(label="C++", command=set_lang_cpp)
language_menu.add_command(label="C#", command=set_lang_cs)
language_menu.add_command(label="HTML", command=set_lang_html)
language_menu.add_command(label="CSS", command=set_lang_css)
language_menu.add_command(label="XML", command=set_lang_xml)
language_menu.add_command(label="SQL", command=set_lang_sql)
language_menu.add_command(label="BASH/BATCH", command=set_lang_bash)
language_menu.add_command(label="Perl", command=set_lang_perl)
language_menu.add_command(label="PHP/HTML", command=set_lang_php)
language_menu.add_command(label="Ruby", command=set_lang_ruby)

# auo set to dark mode
editor.config(fg="white", bg="#2c2f33")
output_window.config(fg="white", bg="#2c2f33")


def check_highlight():
    syntax[lang_config["lang"]]()
    window.after(1, check_highlight)


window.after(1, check_highlight)
window.mainloop()
