
##pip3 install PyPDF2
##import PyPDF2
##
##
##PDFfilename = "Orissa 16- Malkangiri 31.05.2011.pdf" #filename of your PDF/directory where your PDF is stored
##
##pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
##
##pg4 = pfr.getPage(16) #extract pg 127
##
##writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
###add pages
##writer.addPage(pg4)
##
##NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
##with open(NewPDFfilename, "wb") as outputStream:
##    writer.write(outputStream) #write pages to new PDF
##

py -m pip install pdfplumber
import pdfplumber as scrapper

text = []
with scrapper.open('./Orissa 16- Malkangiri 31.05.2011.pdf') as pdf:
    for page in pdf.pages:
        text.append(page.extract_text())
