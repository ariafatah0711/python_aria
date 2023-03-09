import tkinter as tk

# fungsi
def usd_to_idr():
    angka = textbok.get()
    dollar = float(angka) * 14405.5
    text.set("Rp"+str(dollar))
    label2.config(font=("Helvetica",15,"bold"),fg="green")

# configurasi
window = tk.Tk()

window.title("USD TO IDR")
window.geometry("250x150")
window.resizable(False, False)
window.configure(bg="white")

# main progam
label1 = tk.Label(window,text="USD",font=("Helvetica", 15, "bold"))
label1.pack()

textbok = tk.Entry(window,font=("Helvetica", 18, "bold"),width=6,justify=tk.CENTER)
textbok.pack()

button1 = tk.Button(window,text="TO",command=usd_to_idr,font=("Helvetica", 15, "bold"))
button1.pack()

text = tk.StringVar()
text.set("IDR")

label2 = tk.Label(window,textvariable=text,font=("Helvetica", 15, "bold"))
label2.pack()

window.mainloop()