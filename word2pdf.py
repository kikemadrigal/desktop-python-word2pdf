import sys
import os
from tkinter import Tk, Label, Button
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
import Converter



window= Tk()
window.title("Tipolisto pdf-word converter")
operation_rejected=False


#aki obtendremos el path absoluto y crearemos las acciones de conversión según la extensión
def convert(in_file):
    # 1 convertimos la entrada a minúscula
    in_file = in_file.lower()
    #2 Obtenemos la posición del punto
    point_position=in_file.find(".")
    #3 Obtenemos su extensión, no es necesario poner el tamaño, python ya lo supone
    extension=in_file[point_position+1:]

    if extension=="doc" or extension=="docx":
        #Converter.convertWord2PdfWithComTypes(in_file)
        Converter.convertWord2PdfWithDocx2Pdf(in_file)
    elif extension=="pdf": 
        Converter.convertWord2PdfWithPdf2Docx(in_file)
    else:
        print("can't convert: "+extension)




def create_window():
    #window.iconbitmap("data\icon.ico")
    lbl=Label(window, text="Choose file")
    lbl.grid(row=0,column=0, padx=5, pady=5)
    #lblResult=Label(window, text="")
    #lblResult.grid(row=1,column=1, padx=5, pady=5)
    button=Button(window,text="Select", width=30, command=open_file)
    button.grid(row=0,column=1, padx=5, pady=5)
    window.geometry("400x50")
    #lbl.config(text="Converted file: \n"+in_file)
    #lbl["text"]="Converting the file: "+out_file
    #lbl.pack()
    window.mainloop()
    window.quit()
def open_file():
        print("Click en el boton de abrir archivo")
        file=askopenfile(filetypes=[('Word Files','*.docx'),('Pdf Files','*.pdf')])
        # if file is not None:
        if file is None:
            print("No se obtuvo el archivo a convertir")
            showinfo("Error","No se obtuvo el archivo")
        else:
            print(file.name)
            convert(file.name)
            showinfo("Done","File successfully converted.")
            #window.quit()



print("Tipolisto word2pdf, pdf2word")
#out_file = os.path.abspath(sys.argv[2])
cmd=True
if len(sys.argv)<=1:
    print("No se obtuvieron argumentos en el command line, abriendo ventana")
    create_window()
    CMD=False
elif len(sys.argv)>1:
    if cmd:
        in_file = os.path.abspath(sys.argv[1])
        print("Se obtuvieron argumentos en el command line, ejecutando en consola ")
        convert(in_file)
    else:
        create_window()
print("Bye")











