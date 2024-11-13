import socket

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Seri!"
    elif (choice1 == "batu" and choice2 == "gunting") or \
         (choice1 == "gunting" and choice2 == "kertas") or \
         (choice1 == "kertas" and choice2 == "batu"):
        return "Pemain 1 menang!"
    else:
        return "Pemain 2 menang!"

def main():
    host = '0.0.0.0'  # Dengarkan di semua interface
    port = 5555       # Port yang digunakan

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)

    print("Menunggu pemain...")
    conn1, addr1 = server_socket.accept()
    print("Pemain 1 terhubung dari", addr1)

    conn2, addr2 = server_socket.accept()
    print("Pemain 2 terhubung dari", addr2)

    while True:
        # Terima pilihan dari pemain 1
        choice1 = conn1.recv(1024).decode().strip()
        if not choice1:
            break
        print("Pemain 1 memilih:", choice1)

        # Terima pilihan dari pemain 2
        choice2 = conn2.recv(1024).decode().strip()
        if not choice2:
            break
        print("Pemain 2 memilih:", choice2)

        # Tentukan pemenang
        result = determine_winner(choice1, choice2)
        print("Hasil:", result)

        # Kirim hasil ke kedua pemain
        conn1.send(result.encode())
        conn2.send(result.encode())

    conn1.close()
    conn2.close()
    server_socket.close()

if __name__ == "_main_":
    main()