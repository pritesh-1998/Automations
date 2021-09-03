import PyPDF2
first_pdf=r"C:\Users\plath\Documents\programming codes\Python automations\Automations\pdf-operations\first.pdf"
second_pdf=r"C:\Users\plath\Documents\programming codes\Python automations\Automations\pdf-operations\second.pdf"
with open(r"C:\Users\plath\Documents\programming codes\Python automations\Automations\pdf-operations\first.pdf","rb") as file:
    reader=PyPDF2.PdfFileReader(file)
    #prints number pages in pdf
    print(reader.numPages)
    #get specific page
    page=reader.getPage(0)
    #rotating and writing to seprate new file
    page.rotateClockwise(90)
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(r"C:\Users\plath\Documents\programming codes\Python automations\Automations\pdf-operations\edited.pdf","wb") as edited_file:
        writer.write(edited_file)

#combining pdfs
merger= PyPDF2.PdfFileMerger()
files=[first_pdf,second_pdf]
for file_name in files:
    merger.append(file_name)
merger.write("combined.pdf")
