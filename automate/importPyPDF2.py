import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes.pdf', 'rb') # cheating a bit - we only have one file

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
  page = reader1.getPage(pageNum)
  writer.addPage(page)

for pageNum in range(reader2.numPages):
  page = reader1.getPage(pageNum)
  writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')

writer.write(outputFile)
pdf1File.close()
pdf2File.close()
outputFile.close()