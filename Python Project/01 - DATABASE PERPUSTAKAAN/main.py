import os, time
import CRUID as CRUID

if __name__ == "__main__":
    sistem_operasi = os.name

    def clear():
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

    def head():
        print("="*32)
        print(f'|{"SELAMAT DATANG DI PROGAM":^30}|')
        print(f'|{"DATA BASE PERPUSTAKAAN":^30}|')
        print("="*32)

    def body():
        print(f'{"| 1. Read Data":<30} |')
        print(f'{"| 2. Create Data":<30} |')
        print(f'{"| 3. Update Data":<30} |')
        print(f'{"| 4. Delete Data":<30} |')
        print("="*32)
    
    # check database itu ada atau tidak
    clear()
    head()
    CRUID.init_console()

    while True:
        
        clear()
        head()
        body()

        user_option = input("masukan opsi: ")

        match user_option:
            case "1": CRUID.read_console()
            case "2": CRUID.create_console()
            case "3": CRUID.update_console()
            case "4": CRUID.delete_console()
            case _:
                print("opsi tidak ditemukan, silakan coba lagi")
                time.sleep(1.3)
                continue

        if CRUID.view.v == True:
            CRUID.view.lanjut()
            if CRUID.view.x == True:
                break
            else:
                pass
        else:
            pass

    print("progam berakhir")