# Beautifulsoup => library untuk mengambil data dari halaman web
    # dan mengekstrak informasi yang diperlukan

from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)