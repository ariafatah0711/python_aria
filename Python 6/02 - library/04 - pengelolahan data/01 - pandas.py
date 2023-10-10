# pengelolahan data => bertujuan untuk membantu dalam manipulasi, analisis, dan pemrosesan data. Library ini menyediakan berbagai fungsi dan metode yang memudahkan pengguna
    # untuk melakukan operasi pengolahan data dengan lebih efisien dan cepat.
    
# pandas => library populer yang digunakan untuk pengelolaan dan analisis data
import pandas as pd

# membuat dataFrame dari dictionary
data = {
    "nama": ["aria", "fadly", "rafii"],
    "usia": [25, 30, 19],
    "pekerjaan": ["fe", "be", "fs"],
}

df = pd.DataFrame(data)

# menampilkan dataFrame
print(df)