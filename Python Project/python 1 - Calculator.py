import os, time
# data angka
angka_pertama = 0
angka_kedua = 0
operator = "#"
hasil = 0

# list calculator
def list():
    os.system("clear")
    print(
        "\t\033[36;1mCalculator\n"
        "\033[33;1m-------------------------\n"
        "|no| Operator \t| kode \t|\n"
        "-------------------------\n"
        "|1.| Pertambahan|  + \t|\n"
        "|2.| pengurangan|  - \t|\n"
        "|3.| perkalian  |  * \t|\n"
        "|4.| pembagian  |  / \t|\n"
        "|5.| modul      |  // \t|\n"
        "|6.| pangkat    |  ** \t|\n"
        "|7.| hasil bagi |  % \t|\n"
        "-------------------------\n"
        f"|*.| \033[36;1m{angka_pertama} \033[31;1m{operator} \033[36;1m{angka_kedua} \t\033[33;1m| \033[36;1m{hasil} \t\033[33;1m|\n"
        "\033[33;1m-------------------------\n"
    )

# input angka, operator
while True:
    list()
    print("    Q untuk keluar")
    
    # angka pertama
    angka_pertama = input("\033[37;1mmasukan angka pertama \t\t: \033[36;1m")
    if angka_pertama == "q":
        print("\n\033[31;1mprogam berhenti\033[37;1m")
        exit()
    elif angka_pertama.isdigit():
        angka_pertama = int(angka_pertama)
    else:
        print("input harus angka silakan coba lagi")
        time.sleep(2)
        continue
    # operator
    operator = input("\033[37;1mmasukan operator aritmatika \t: \033[31;1m")
    if operator == "q":
        print("\n\033[31;1mprogam berhenti\033[37;1m")
        exit()

    #angka kedua
    angka_kedua = input("\033[37;1mmasukan angka kedua \t\t: \033[36;1m")
    if angka_kedua == "q":
        print("\n\033[33;1mprogam berhenti\033[37;1m")
        exit()
    elif angka_kedua.isdigit():
        angka_kedua = int(angka_kedua)
    else:
        print("input harus angka silakan coba lagi")
        time.sleep(2)
        continue

    # kondisi +, -, *, /, %, dll
    if operator == "+":
        hasil = angka_pertama + angka_kedua
        os.system("clear")
        continue
    elif operator == "-":
        hasil = angka_pertama - angka_kedua
        os.system("clear")
        continue
    elif operator == "*":
        hasil = angka_pertama * angka_kedua
        os.system("clear")
        continue
    elif operator == "/":
        hasil = angka_pertama / angka_kedua
        os.system("clear")
        continue
    elif operator == "%":
        hasil = angka_pertama % angka_kedua
        os.system("clear")
        continue
    elif operator == "**":
        hasil = angka_pertama ** angka_kedua
        os.system("clear")
        continue
    elif operator == "//":
        hasil = angka_pertama // angka_kedua
        os.system("clear")
        continue
    else:
        print("\n\033[31;1moprator tidak memenuhi syarat ada kesalahan")
        time.sleep(1)
        os.system("clear")
        continue
