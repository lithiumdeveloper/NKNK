#!/usr/bin/env python
import subprocess
import tkinter as tk
import nknk
def contact():
    print("doesnt work in linux version")
def docmain():
    print("doesnt work in linux version")
def docex():
    print("doesnt work in linux version")
def main():
    print("This is free and open source software, if you paid for this you were scammed")
    print("Made by EZTLI on earth by humans roughly 2024 rotations around the sun after the death of our savior")
    print("Version MAIN1.1")

    fn = input("Enter filename: ")
    print(fn)

    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    print(ksfile)
    print("-----------\n\n")

    replacements = {
        ">": "age:            ",
        "~": "name:           ",
        "#": "phone:          ",
        "&": "family:         ",
        "^": "associates:     ",
        "_@": "emails:         ",
        "!": "address:        ",
        "*": "state/province: ",
        "$": "city/town:      ",
        "-": "apt/suite:      ",
        "//": "comments:       ",
        "`": "file/image:     ",
        ";": "ip address:     ",
        "_tt": "tiktok          ",
        "_yt": "youtube         ",
        "_sc": "snapchat        ",
        "_dc": "discord         ",
        "_ds": "discord server  ",
        "_ex": "extra social    ",
        "\\\\": "end comment     ",
        ",": ", ",
        "?": "unknown "
    }

    for old_str, new_str in replacements.items():
        ksfile = ksfile.replace(old_str, new_str)

    print(ksfile)

    fn2 = input("Enter output filename: ")
    with open(fn2, "w", encoding="utf-8") as fw:
        fw.write(ksfile)

    print("Done writing output file")

def ex():

    print("This is free and open source software, if you paid for this you were scammed")
    print("Made by EZTLI on earth by humans roughly 2024 rotations around the sun after the death of our savior")
    print("Version EX1.1 ")
    # the following is obsolete in the s3header version
    #help = input("Would you like to read documentation?: y/n?: ")
    #if help == "y":
    #    subprocess.call(['notepad.exe', "docs\doc2.txt"])
    #    exit()
    #elif help == "n":
    #    print("okay")
    #else:
    #    print("exit code 0")
    #    exit()
    fn = input("Enter filename: ")
    print(fn)
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    print(ksfile)
    print("-----------\n\n")
    new_string0 = ksfile.replace("_ag", "age:            ")
    new_string1 = new_string0.replace("_n", "name:           ")
    new_string2 = new_string1.replace("_p", "phone:          ")
    new_string3 = new_string2.replace("_f", "family:         ")
    new_string4 = new_string3.replace("_w", "work:           ")
    new_string5 = new_string4.replace("_e", "emails:         ")
    new_string6 = new_string5.replace("_ad", "address:        ")
    new_string7 = new_string6.replace("_sp", "state/province: ")
    new_string8 = new_string7.replace("_ct", "city/town:      ")
    new_string9 = new_string8.replace("_as", "apt/suite:      ")
    new_stringa = new_string9.replace("//", "comments:       ")
    new_stringb = new_stringa.replace("_h", "file/image:     ")
    new_stringc = new_stringb.replace("_ip", "ip address:     ")
    new_stringd = new_stringc.replace("_tt", "tiktok          ")
    new_stringe = new_stringd.replace("_yt", "youtube         ")
    new_stringf = new_stringe.replace("_sc", "snapchat        ")
    new_stringg = new_stringf.replace("_dc", "discord         ")
    new_stringh = new_stringg.replace("_ds", "discord server  ")
    new_stringi = new_stringh.replace("_ex", "extra social    ")
    new_stringj = new_stringi.replace("'\\'", "end comment     ")
    new_stringk = new_stringj.replace(",", ", ")
    fstr = new_stringk.replace("?", "unknown ")
    print(fstr)
    fn2 = input("Enter output filename: ")
    fw = open(fn2, "w", encoding="utf-8")
    fw.write(fstr)
    print("Done writing output file")
# new r/w functions
def readfile(fnr):
    with open(fnr, "r", encoding="utf-8") as file:
        fr = file.read()
    print(fr)
    input()
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
    else:
        exit()
    
#no input func for main and ex

def mainnoin(fn, fn2):
    print(fn)
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    new_string0 = ksfile.replace(">", "age:            ")
    new_string1 = new_string0.replace("~", "name:           ")
    new_string2 = new_string1.replace("#", "phone:          ")
    new_string3 = new_string2.replace("&", "family:         ")
    new_string4 = new_string3.replace("^", "associates:     ")
    new_string5 = new_string4.replace("_@", "emails:         ")
    new_string6 = new_string5.replace("!", "address:        ")
    new_string7 = new_string6.replace("*", "state/province: ")
    new_string8 = new_string7.replace("$", "city/town:      ")
    new_string9 = new_string8.replace("-", "apt/suite:      ")
    new_stringa = new_string9.replace("//", "comments:       ")
    new_stringb = new_stringa.replace("`", "file/image:     ")
    new_stringc = new_stringb.replace(";", "ip address:     ")
    new_stringd = new_stringc.replace("_tt", "tiktok          ")
    new_stringe = new_stringd.replace("_yt", "youtube         ")
    new_stringf = new_stringe.replace("_sc", "snapchat        ")
    new_stringg = new_stringf.replace("_dc", "discord         ")
    new_stringh = new_stringg.replace("_ds", "discord server  ")
    new_stringi = new_stringh.replace("_ex", "extra social    ")
    new_stringj = new_stringi.replace("'\\'", "end comment     ")
    new_stringk = new_stringj.replace(",", ", ")
    fstr = new_stringk.replace("?", "unknown ")
    fw = open(fn2, "w", encoding="utf-8")
    fw.write(fstr)
def exnoin(fn, fn2):
    with open(fn, "r", encoding="utf-8") as file:
        ksfile = file.read()
    new_string0 = ksfile.replace("_ag", "age:            ")
    new_string1 = new_string0.replace("_n", "name:           ")
    new_string2 = new_string1.replace("_p", "phone:          ")
    new_string3 = new_string2.replace("_f", "family:         ")
    new_string4 = new_string3.replace("_w", "work:           ")
    new_string5 = new_string4.replace("_e", "emails:         ")
    new_string6 = new_string5.replace("_ad", "address:        ")
    new_string7 = new_string6.replace("_sp", "state/province: ")
    new_string8 = new_string7.replace("_ct", "city/town:      ")
    new_string9 = new_string8.replace("_as", "apt/suite:      ")
    new_stringa = new_string9.replace("//", "comments:       ")
    new_stringb = new_stringa.replace("_h", "file/image:     ")
    new_stringc = new_stringb.replace("_ip", "ip address:     ")
    new_stringd = new_stringc.replace("_tt", "tiktok          ")
    new_stringe = new_stringd.replace("_yt", "youtube         ")
    new_stringf = new_stringe.replace("_sc", "snapchat        ")
    new_stringg = new_stringf.replace("_dc", "discord         ")
    new_stringh = new_stringg.replace("_ds", "discord server  ")
    new_stringi = new_stringh.replace("_ex", "extra social    ")
    new_stringj = new_stringi.replace("'\\'", "end comment     ")
    new_stringk = new_stringj.replace(",", ", ")
    fstr = new_stringk.replace("?", "unknown ")
    fw = open(fn2, "w", encoding="utf-8")
    fw.write(fstr)
def tkin():
    frame = tk.Tk() 
    frame.title("TextBox Input") 
    frame.geometry('400x200') 
    def printInput(): 
        global tkinp
        tkinp = inputtxt.get(1.0, "end-1c")
        writefile("tkinput.txt", tkinp)
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
    readfile("tkinput.txt")

def kslselector():
    option = ""
    while option != "q":
        print("1. contact info")
        print("2. view docs")
        print("3. run interpreter")
        print("q. Quit")
        option = input("Select an option: ")
        if option == "1":
            print("Contact info selected")
            contact()
        elif option == "2":
            suboption = ""
            while suboption != "q":
                print("1 main docs")
                print("2 extra docs")
                print("q. Go back")
                suboption = input("Select a suboption: ")
                if suboption == "1":
                    print("Main docs selected")
                    docmain()
                elif suboption == "2":
                    print("Extra docs selected")
                    docex()
                elif suboption == "q":
                    print("Going back to main menu")
                else:
                    print("Invalid suboption")
        elif option == "3":
            suboption = ""
            while suboption != "q":
                print("1 main")
                print("2 extra")
                print("q. Go back")
                suboption = input("Select a suboption: ")
                if suboption == "1":
                    print("Main interpreter selected")
                    main()
                elif suboption == "2":
                    print("Extra interpreter selected")
                    ex()
                elif suboption == "q":
                    print("Going back to main menu")
                elif suboption == "n":
                    notepad()
                elif suboption == "m":
                    nreadfile()
                else:
                    print("Invalid suboption")
        elif option == "q":
            print("Exiting the program")
        else:
            print("Invalid option")
def pyrun(path):
    exec(open(path).read())
def scmd(cmd):
    nknk.subprocess.call(cmd, shell=True)
# KEEP AT END
# PLS FTLOG KEEP THIS FUNC AT THE END

def cmdline():
    while True:
        function_name = input("Ksl.py@User:~$ ")
        if function_name == "exit":
            print("Exiting...")
            break
        else:
            exec(function_name)