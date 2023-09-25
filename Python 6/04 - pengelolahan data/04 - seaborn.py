# seaborn =>  library dengan tujuan untuk visualisasi data sama seperti matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()