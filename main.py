import PyPDF2

# PDF files are binary files. PyPDF2 start indexing pages at 0. This module can't create PDF files from scratch.
pdfFile = open('curriculum.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
# OR
# reader = PyPDF2.PdfReader('curriculum.pdf')

# Number of pages
print(reader.numPages)

# Extract text from the first page
page = reader.getPage(0)
print(page.extractText())
pdfFile.close()

# Write content in a new PDF
reader1 = PyPDF2.PdfReader('curriculum.pdf')
reader2 = PyPDF2.PdfReader('graph.pdf')

# The new PDF
writer = PyPDF2.PdfWriter()
for pageNum in range(reader1.numPages):
    pageToAdd = reader1.getPage(pageNum)
    writer.addPage(pageToAdd)

for pageNum in range(reader2.numPages):
    pageToAdd = reader2.getPage(pageNum)
    writer.addPage(pageToAdd)

outputFile = open('combined.pdf', 'wb')
writer.write(outputFile)
outputFile.close()

# Merging example

# mergeFile = PyPDF2.PdfFileMerger()
#
# mergeFile.append(PyPDF2.PdfFileReader('file1.pdf', 'rb'))
#
# mergeFile.append(PyPDF2.PdfFileReader('file2.pdf', 'rb'))
#
# mergeFile.write("NewMergedFile.pdf")
