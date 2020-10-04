import pyttsx3
import PyPDF2

bukname = input("Note: The pdf file should be in the same directory or folder in which audiobook.py is present\n"
                "Please enter the book's name with .pdf along with the name: ")
book = open(bukname, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print("The pdf file named ", bukname, " has", pages, " pages\n")

speaker = pyttsx3.init()
nump = int(input("Please enter the page no. from where you want to start reading the book\n"
                 "(Enter 0 for Page no. 1, 1 for Page no. 2 and so on): "))
for pgs in range(nump, pages):
    page = pdfReader.getPage(pgs)
    content = page.extractText()
    speaker.say(content)
    speaker.runAndWait()

