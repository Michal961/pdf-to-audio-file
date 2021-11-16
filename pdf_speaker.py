import Configuration
import PyPDF2
from gtts import gTTS

def main():
    try:
        # path of the PDF file
        path = open(Configuration.FILE_PATH, mode="br")
        # creating a Pdf_File_Reader object
        pdfReader = PyPDF2.PdfFileReader(path)

        # the page with which you want to start
        # this will read the page of 25th page.
        page = pdfReader.getPage(0)

        # extracting the text you want to convert to audio
        mytext = page.extractText()
        print(mytext)
        # Language in which you want to convert
        language = Configuration.LANGUAGE

        # Passing the text and language to the engine
        myobj = gTTS(text=mytext, lang=language, slow=False)
        # Saving the converted audio in a mp3 file
        myobj.save("cv.mp3")

    except:
        print("File not found")


if __name__ == "__main__":
    main()