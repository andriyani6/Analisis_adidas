import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# Data CSV sebagai string
produksi_csv = """Jenis_Sepatu,Produksi_Bulan,Produksi
Running,2024-01,500
Running,2024-02,600
Running,2024-03,550
Running,2024-04,700
Casual,2024-01,400
Casual,2024-02,450
Casual,2024-03,500
Casual,2024-04,480
Sports,2024-01,300
Sports,2024-02,350
Sports,2024-03,330
Sports,2024-04,400
"""

persediaan_csv = """Jenis_Sepatu,Persediaan_Bulan,Persediaan
Running,2024-01,150
Running,2024-02,200
Running,2024-03,180
Running,2024-04,220
Casual,2024-01,100
Casual,2024-02,120
Casual,2024-03,110
Casual,2024-04,130
Sports,2024-01,80
Sports,2024-02,90
Sports,2024-03,85
Sports,2024-04,95
"""

penjualan_csv = """Jenis_Sepatu,Penjualan_Bulan,Penjualan
Running,2024-01,350
Running,2024-02,400
Running,2024-03,370
Running,2024-04,450
Casual,2024-01,300
Casual,2024-02,320
Casual,2024-03,350
Casual,2024-04,340
Sports,2024-01,220
Sports,2024-02,260
Sports,2024-03,245
Sports,2024-04,300
"""

# Membaca data dari string CSV menggunakan StringIO
produksi_df = pd.read_csv(StringIO(produksi_csv))
persediaan_df = pd.read_csv(StringIO(persediaan_csv))
penjualan_df = pd.read_csv(StringIO(penjualan_csv))

# Mengubah kolom tanggal menjadi datetime
produksi_df['Produksi_Bulan'] = pd.to_datetime(produksi_df['Produksi_Bulan'])
persediaan_df['Persediaan_Bulan'] = pd.to_datetime(persediaan_df['Persediaan_Bulan'])
penjualan_df['Penjualan_Bulan'] = pd.to_datetime(penjualan_df['Penjualan_Bulan'])

# Menggabungkan data berdasarkan bulan dan jenis sepatu
merged_df = pd.merge(produksi_df, persediaan_df, left_on=['Jenis_Sepatu', 'Produksi_Bulan'], right_on=['Jenis_Sepatu', 'Persediaan_Bulan'])
merged_df = pd.merge(merged_df, penjualan_df, left_on=['Jenis_Sepatu', 'Produksi_Bulan'], right_on=['Jenis_Sepatu', 'Penjualan_Bulan'])

# Menghapus kolom yang tidak diperlukan
merged_df = merged_df.drop(columns=['Persediaan_Bulan', 'Penjualan_Bulan'])

# Menghitung korelasi
correlation_matrix = merged_df[['Produksi', 'Persediaan', 'Penjualan']].corr()

# Menampilkan matriks korelasi
print(correlation_matrix)

# Visualisasi matriks korelasi menggunakan heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Matriks Korelasi antara Produksi, Persediaan, dan Penjualan Sepatu Adidas')
plt.show()
