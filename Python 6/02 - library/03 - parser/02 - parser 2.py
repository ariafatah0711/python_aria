# python <nama_file> -n NAMA
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)