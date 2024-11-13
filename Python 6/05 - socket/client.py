import socket

def main():
    server_ip = input("Masukkan IP server: ")
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    print("Terhubung ke server. Selamat bermain Batu Gunting Kertas!")

    while True:
        choice = input("Pilih (batu, gunting, kertas): ").strip().lower()
        if choice not in ["batu", "gunting", "kertas"]:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        # Kirim pilihan ke server
        client_socket.send(choice.encode())

        # Terima hasil dari server
        result = client_socket.recv(1024).decode()
        print("Hasil:", result)

        play_again = input("Main lagi? (y/n): ").strip().lower()
        if play_again != 'y':
            break

    client_socket.close()

if __name__ == "_main_":
    main()