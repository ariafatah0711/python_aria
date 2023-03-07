# GUI -> Grapical User Interface (tampilan)
import tkinter as tk
from tkinter import ttk #tk untuk window ttk untuk widged
from tkinter.messagebox import showinfo 

window = tk.Tk() # tkinter.Tk()

# configure / init
window.configure(bg="white") # configure untuk mengatur tampilan
window.geometry("300x200") # mengatur ukuran default
window.resizable(False, False) # agar ukuran tidak dapat diubah
window.title("aria fatah window") # untuk judul windownya

#### Variable dan fungsi ####
NAMA_DEPAN = tk.StringVar() # seperti type string
NAMA_BELAKANG = tk.StringVar()  

def tombol_click():
    '''fungsi ini dipanggil oleh tombol'''
    pesan = f"halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} ganteng" # jangan lupa pake get()

    # menampilkan di terminal
    print(f"nama {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}") # gunakan .get() agar dapat keluar outputnya

    # menampilkan di window
    showinfo(title="halo guys", message=pesan) # title judul window, message untuk teks pesan 

# frame input
input_frame = ttk.Frame(window) # widged frame taruh di window
# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True) # pading batas atas dan bawah

# komponen komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan") # ttk label taruh di input frame
nama_depan_label.pack(padx=10,fill="x",expand=True) # mengambil pack dan menyesuaikan ukuran
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN) # variabletext untuk menamabah variable
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# 5. tombol
tombol_sapa = ttk.Button(input_frame,text="sapa!",command=tombol_click) # command untuk fungsi
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)

# mainloop window
window.mainloop() # untuk run progam biar muter terus