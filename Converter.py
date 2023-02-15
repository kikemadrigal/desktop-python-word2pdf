#Module word2pdf
#comtypes es para el manejo de programas del paquete microsoft office
import comtypes.client
from docx2pdf import convert
from pdf2docx import parse
from typing import Tuple

def convertWord2PdfWithComTypes(in_file):
    print("Procesando...")
    point_position=in_file.find(".")  
    extension=in_file[point_position+1:]
    out_file=in_file.replace(extension,".pdf")
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
    print("Conversion to pdf completed successfully.")


def convertPdf2WordWithComTypes(in_file, out_file):
    a=2


def convertWord2PdfWithDocx2Pdf(in_file:str):
    convert(in_file)

def convertWord2PdfWithPdf2Docx(input_file :str, pages: Tuple = None):
    output_file=input_file.replace(".pdf",".docx")
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_file= output_file, pages=pages)

    summary = {
        "File" : input_file, "Pages": str(pages), "Output File": output_file
    }

    print("## Summary #########################################################")
    print("\n".join("{}:{}".format(i, j) for i , j in summary.items()))
    print("#####################################################################")
    return result



