from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# List of PDF files to merge
pdf_files = [
    "file1.pdf",
    "file2.pdf",
    "file3.pdf"
]

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()

print("PDFs merged successfully!")