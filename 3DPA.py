from tkinter import *
from tkinter.ttk import *
import webbrowser

window = Tk()
window.iconbitmap(r'F:\Github\Python\3dPrintAssist\appIco.ico')

window.title("3D Print Assistant")
window.geometry('550x150')

lbl = Label(window, text= "3D model price generator", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

comboLbl = Label(window, text= "Select material: ")
comboLbl.grid(column=0, row=1)

combo = Combobox(window)
combo['values'] = ("Select...", "PLA", "PETG", "ASA", "ABS", "PC", "TPU")
combo.current(0)
combo.grid(column=1, row=1)

EntryLbl = Label(window, text= "Model weight: ")
EntryLbl.grid(column=0, row=2)

txt = Entry(window, width= 23)
txt.grid(column=1, row=2)

def OnClicked():
    if(combo.get() == "PLA"):
        plaVal = 30
        result = plaVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    elif(combo.get() == "PETG"):
        petgVal = 30
        result = petgVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    elif(combo.get() == "ASA"):
        asaVal = 32
        result = asaVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    elif(combo.get() == "ABS"):
        absVal = 30
        result = absVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    elif(combo.get() == "PC"):
        pcVal = 43
        result = pcVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    elif(combo.get() == "TPU"):
        tpuVal = 44
        result = tpuVal /1000 * int(txt.get())
        resLbl.config(text= "Total value: €" + str(result))
    else:
        resLbl.config(text= "ERROR: Invalid value(s)")

btn = Button(window, text = "Calculate", command= OnClicked)
btn.grid(column=1, row=3)

resLbl = Label(window, text= "Please enter the weight of the object and the material.")
resLbl.grid(column=1, row=4)

verLbl = Label(window, text= "Version: 1.0", font=("Arial Bold", 11))
verLbl.grid(column=0, row=3)

def link():
    webbrowser.open_new_tab(r"https://github.com/MassGaming25/3DPrintAssist")

abtBtn = Button(window, text="Github", command= link)
abtBtn.grid(column=0, row=4)

window.mainloop()