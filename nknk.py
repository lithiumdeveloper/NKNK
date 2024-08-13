#!$HOMEDIRECTORYvenv/bin/python
# nk's not ksl
import subprocess
import sys
import os
import shutil
import re
import builtins
import timeit
from rich.console import Console # type: ignore
from rich.markdown import Markdown # type: ignore

SUPRESSLOGS = False
NOHISTORY = True
homedir = "~"
# This is the backup shell it is only used if init fails
SystemShell = "/bin/bash"
nkdir = f"/~/bin/lnknk/"
DefaultDir = '~/bin/lnknk'
Source = f"{DefaultDir}/nknk.py"
HOMEDIR = '~'
COMMANDS = [
    'scmd',
    'initialize',
    'sharks',
    'make_the_sharks_swim',
    'incstack',
    'readfile',
    'writefile',
    'nreadfile',
    'nwritefile',
    'notepad',
    'tkin',
    'readtkin',
    'cd',
    'mkdir',
    'pyrun',
    'inrun',
    'pwd',
    'impksl',
    'clear',
    'delete',
    'rmdir',
    'ls',
    'curl',
    'refresh',
    'sideload',
    'vim',
    'nknkdef',
    'cmdline',
    'vink',
    'davinki',
    'pdv',
    'history',
    'nknk',
    'exit',
    'guinotepad',
    '!'
]

def initialize():
    global console, SystemShell, readline, socket
    import readline
    import socket
    # This is where you can set the recursion limit (1000 default)
    incstack(1000)
    # This is where you can change your regular Shell
    SystemShell = "/usr/bin/zsh"
    # Markdown
    console = Console()

def scmd(cmd):
    try:
        subprocess.run(cmd, shell=True, executable=SystemShell)
    except Exception as e:
        print("Shell:", e)


def NKlog():
    if not SUPRESSLOGS:
        print("NKNK: Log: Shell:", SystemShell)
        print("NKNK: Log: Dir:", DefaultDir)
        print("NKNK: Log: recursion limit: ",sys.getrecursionlimit())

def sharks():
    arguments = sys.argv[1:]
    if arguments:
        command = ' '.join(arguments)
        scmd(command)
    else:
        initialize()
        NKlog()
        cmdline()

def make_the_sharks_swim():
    if __name__=="__main__":
        sharks()
    elif not SUPRESSLOGS:
        print("NKNK: Log: Importing script is handling init")

#fun
def incstack(number):
    sys.setrecursionlimit(number)
    print(sys.getrecursionlimit())
#files
def readfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents
def writefile(fnw, data):
    fw = open(fnw, "w", encoding="utf-8")
    fw.write(data)
    print(fw)
def nreadfile():
    fnr = input("Filename to read(utf-8): ")
    with open(fnr, "r", encoding="utf-8") as file:
        fr = file.read()
    print(fr)
    input()
def nwritefile():
    fw = input("Filename to write to(utf-8): ")
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    fr2 = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        fr2.append(line)
    with open(fw, "w") as outfile:
        outfile.write("\n".join(fr2))
    print(fr2)
def notepad():
    s1 = input("would you like to r/w?: ")
    if s1 == "r":
        nreadfile()
    elif s1 == "w":
        nwritefile()
#tkinter        
def tkin():
    import tkinter as tk
    frame = tk.Tk() 
    frame.title("TextBox Input") 
    frame.geometry('400x200') 
    def printInput(): 
        global tkinp
        tkinp = inputtxt.get(1.0, "end-1c")
        writefile("tkinput.py", tkinp)
    inputtxt = tk.Text(frame, 
                    height = 5, 
                    width = 20) 
    inputtxt.pack() 
    printButton = tk.Button(frame, 
                            text = "submit",  
                            command = printInput) 
    printButton.pack() 
    lbl = tk.Label(frame, text = "") 
    lbl.pack() 
    frame.mainloop() 
def readtkin():
    readfile("tkinput.py")
#syscmd
def cd(path):
    os.chdir(path)
def mkdir(path):
    try:  
        os.mkdir(path)  
    except OSError as error:  
        print(error)
def inrun():
    path = input("python file: ")
    exec(open(path).read())
def pwd():
    global current_working_directory
    current_working_directory = os.getcwd()
    print(current_working_directory)
def impksl():
    global ksl
    import ksl
def clear():
    _ = os.system('clear')
def rmdir(path):
    try:
        shutil.rmtree(path)
        print('Folder and its content removed')
    except:
        print('Folder not deleted')

def delete(path):
        if os.path.isfile(path) == True:
            os.remove(path)
        if os.path.isdir(path):
            rmdir(path)
        else:
            print("The file or directory does not exist") 

def ls():
    print(os.listdir('.'))
def curl(argument):
    scmd(f"curl {argument}")
def refresh():
    r="refreshing"
    print(r)
    os.execv(sys.argv[0], sys.argv)
def sideload():
    fnr = "tkinput.py"
    with open(fnr, "r", encoding="utf-8") as file:
        fr = file.read()
    exec(fr)
def vim(a):
    scmd(f"vim {a}")
def vink():
    scmd(f'vim {__file__}')
def pdv():
    script_variables = set(globals().keys())
    default_variables = set(dir(builtins))
    defined_variables = script_variables - default_variables

    for var in defined_variables:
        if var != '__builtins__' and var != 'copyright' and var != 'credits':
            print(var, "=", globals()[var])
#history
def history():
            nk_history_file=readfile(f"{nkdir}.NKHISTORY")
            nk_history_file+=nknk_history
            print(nk_history_file)
            return(nk_history_file)
def clearhistory():
    delete(f"{nkdir}.NKHISTORY")

def nknkdef(code):
    nknk = readfile(Source)
    nknk += f'\n{code}'
    writefile(Source, nknk)
    refresh()
#CLI
RE_SPACE = re.compile('.*\\s+$', re.M)
class Completer(object):

        def _listdir(self, root):
            "List directory 'root' appending the path separator to subdirs."
            res = []
            for name in os.listdir(root):
                path = os.path.join(root, name)
                if os.path.isdir(path):
                    name += os.sep
                res.append(name)
            return res

        def _complete_path(self, path=None):
            "Perform completion of filesystem path."
            if not path:
                return self._listdir('.')
            dirname, rest = os.path.split(path)
            tmp = dirname if dirname else '.'
            res = [os.path.join(dirname, p)
                    for p in self._listdir(tmp) if p.startswith(rest)]
            # more than one match, or single match which does not exist (typo)
            if len(res) > 1 or not os.path.exists(path):
                return res
            # resolved to a single directory, so return list of files below it
            if os.path.isdir(path):
                return [os.path.join(path, p) for p in self._listdir(path)]
            # exact file match terminates this completion
            return [path + ' ']

        def complete_extra(self, args):
            "Completions for the 'extra' command."
            if not args:
                return self._complete_path('.')
            # treat the last arg as a path and complete it
            return self._complete_path(args[-1])

        def complete(self, text, state):
            "Generic readline completion entry point."
            buffer = readline.get_line_buffer()
            line = readline.get_line_buffer().split()
            # show all commands
            if not line:
                return [c + ' ' for c in COMMANDS][state]
            # account for last argument ending in a space
            if RE_SPACE.match(buffer):
                line.append('')
            # resolve command to the implementation function
            cmd = line[0].strip()
            if cmd in COMMANDS:
                impl = getattr(self, 'complete_%s' % cmd)
                args = line[1:]
                if args:
                    return (impl(args) + [None])[state]
                return [cmd + ' '][state]
            results = [c + ' ' for c in COMMANDS if c.startswith(cmd)] + [None]
            return results[state]
def nkrun(user_input):
    global nknk_history, elapsed_time
    isshell = user_input.startswith('!')
    issudo = user_input.startswith('#')
    isrun = user_input.startswith('@')
    isback = user_input.startswith('..')
    if isshell: 
        command = user_input.replace('!','')
        scmd(command)
    elif issudo:
        command = user_input.replace('#','sudo ')
        scmd(command)
    elif isrun:
        command = user_input.replace('@','sudo ./')
        scmd(command)
    elif isback:
        cd('..')
    elif user_input == "q":
        nk_history_file=readfile(f"{nkdir}.NKHISTORY")
        nk_history_file+=nknk_history
        writefile(f"{nkdir}.NKHISTORY",nknk_history)
        return(0)
    elif user_input == "qa":
        return(0)
    elif user_input == "nknk":
        help = readfile("~/bin/lnknk/man.md")
        md = Markdown(help)
        console.print(md)
    else:
        try:
            start_time = timeit.default_timer()
            withhome = user_input.replace('~', homedir)
            exec(withhome)
            end_time = timeit.default_timer()
            elapsed_time = round(end_time - start_time, 2)
        except Exception as e:
            print("Cmdline Error:", e)
    if not NOHISTORY:
        nknk_history+=f"{user_input}\n"
def cmdline():
    elapsed_time=0
    if __name__=="__main__":
        if not SUPRESSLOGS:
            print("NKNK: ATTENTION! You are using nknk.py as your nknk console! This is not advised, Please use a nknk console such as nk")
        # please dont actually use this often
        # use a nk terminal application with better fallback features
        exec("from nknk import *")

    if not SUPRESSLOGS:
        print("NKNK: Help: enter 'nknk' ")
    user = os.getlogin()
    PCname = socket.getfqdn()
    comp = Completer()
    AtNameDir = f"@{PCname}:"
    Prompt = f"{user}{AtNameDir}"
    readline.set_completer_delims('\t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(comp.complete)
    while True:
        current_working_directory = os.getcwd()
        user_input = input(f"{Prompt}{current_working_directory} ({elapsed_time})\n:")
        isshell = user_input.startswith('!')
        issudo = user_input.startswith('#')
        isrun = user_input.startswith('@')
        isback = user_input.startswith('..')
        if isshell: 
            command = user_input.replace('!','')
            scmd(command)
        elif issudo:
            command = user_input.replace('#','sudo ')
            scmd(command)
        elif isrun:
            command = user_input.replace('@','sudo ./')
            scmd(command)
        elif isback:
            cd('..')
        elif user_input == "q":
            nk_history_file=readfile(f"{nkdir}.NKHISTORY")
            nk_history_file+=nknk_history
            writefile(f"{nkdir}.NKHISTORY",nknk_history)
            return(0)
        elif user_input == "qa":
            return(0)
        elif user_input == "nknk":
            help = readfile("~/lnknk/man.md")
            md = Markdown(help)
            console.print(md)
        else:
            try:
                start_time = timeit.default_timer()
                withhome = user_input.replace('~', homedir)
                exec(withhome)
                end_time = timeit.default_timer()
                elapsed_time = round(end_time - start_time, 2)
            except Exception as e:
                print("Cmdline Error:", e)
        if not NOHISTORY:
            nknk_history+=f"{user_input}\n"
#args
make_the_sharks_swim()

#user added commands
#start
def viwb(x):
    if x== "j":
        scmd("sudo vim /etc/xdg/waybar/config.jsonc")
    elif x=="c":
        scmd("sudo vim /etc/xdg/waybar/style.css")
    else:
        print("j/c")
def vihl():
    scmd(f"vim ~/.config/hypr/hyprland.conf")
def vihp():
    scmd(f"vim ~/.config/hypr/hyprpaper.conf")
def vink():
    scmd(f"vim {Source}")
def guinotepad():
    import tkinter as tk
    from tkinter import filedialog

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                text = text_widget.get("1.0", tk.END)
                file.write(text)

    def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                text = file.read()
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, text)

    def clear_text():
        text_widget.delete("1.0", tk.END)

    # Create the main window
    window = tk.Tk()
    window.title("Notepad")

    # Create a text widget
    text_widget = tk.Text(window)
    text_widget.pack()

    # Create a menu bar
    menubar = tk.Menu(window)
    file_menu = tk.Menu(menubar, tearoff=1)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Clear", command=clear_text)
    file_menu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Configure the window to use the menu bar
    window.config(menu=menubar)

    # Start the main event loop
    window.mainloop()


#end

#nknkdef added commands
#start
