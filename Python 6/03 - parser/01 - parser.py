# parser => menyediakan fasilitas untuk menguraikan kode Python menjadi
    # struktur data yang dapat diproses dan dianalisis
    # Anda dapat menggunakan Getopt atau ArgParse

    # python <nama_file> -o / --output
    # python <nama_file> -h / --help
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py")

