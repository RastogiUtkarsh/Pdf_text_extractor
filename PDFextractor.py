import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.title("Pdf Text Extractor")

root.geometry("1000x600")

logo = Image.open('logo2.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=2, row=0)

instr = tk.Label(root, text="Select a PDF for extraction of text")
instr.grid(columnspan=3, column=1, row=1, padx=30)

txt_box = tk.Text(root, height = 10, width = 50, padx = 30, pady = 40)
txt_box.tag_configure("center",justify = 'center')
txt_box.tag_add('left',1.0,'end')
txt_box.grid(column = 3 ,row =0)

def fileopen():
    btn_txt.set("Loading..")
    file = askopenfile(parent = root, mode = 'rb', title = 'Choose a file', filetype = [("PDF File","*.pdf")])
    if file:
        read = PyPDF2.PdfFileReader(file)
        page = read.getPage(0)
        content = page.extractText()
        txt_box.insert(1.0, content)
        btn_txt.set("Browse")

btn_txt = tk.StringVar()
btn = tk.Button(root, textvariable=btn_txt, command=lambda: fileopen(), fg='white', bg='red', height=1, width=15)
btn_txt.set("Browse")
btn.grid(columnspan=3, column=1, row=2)

root.mainloop()
