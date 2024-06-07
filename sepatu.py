import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data produksi, persediaan, dan penjualan sepatu Adidas secara acak
np.random.seed(0)
months = pd.date_range(start='2023-01-01', end='2024-12-01', freq='M')
production = np.random.randint(1000, 5000, size=len(months))
inventory = np.random.randint(500, 2000, size=len(months))
sales = np.random.randint(200, 1500, size=len(months))

# Membuat DataFrame dari data yang dibuat
adidas_data = pd.DataFrame({
    'Month': months,
    'Production': production,
    'Inventory': inventory,
    'Sales': sales
})

# Menyimpan DataFrame ke file CSV
adidas_data.to_csv('adidas_data.csv', index=False)

# Membaca data dari file CSV
adidas_data = pd.read_csv('adidas_data.csv', parse_dates=['Month'])

# Visualisasi data dalam bentuk diagram
plt.figure(figsize=(10, 6))

# Diagram produksi
plt.subplot(2, 2, 1)
plt.plot(adidas_data['Month'], adidas_data['Production'], marker='o', color='blue')
plt.title('Production of Adidas Shoes')
plt.xlabel('Month')
plt.ylabel('Production')

# Diagram persediaan
plt.subplot(2, 2, 2)
plt.plot(adidas_data['Month'], adidas_data['Inventory'], marker='o', color='green')
plt.title('Inventory of Adidas Shoes')
plt.xlabel('Month')
plt.ylabel('Inventory')

# Diagram penjualan
plt.subplot(2, 2, 3)
plt.plot(adidas_data['Month'], adidas_data['Sales'], marker='o', color='red')
plt.title('Sales of Adidas Shoes')
plt.xlabel('Month')
plt.ylabel('Sales')

# Pie chart penjualan
plt.subplot(2, 2, 4)
total_sales = adidas_data['Sales'].sum()
sales_proportion = adidas_data['Sales'] / total_sales
labels = adidas_data['Month'].dt.strftime('%b %Y')
plt.pie(sales_proportion, labels=labels, autopct='%1.1f%%')
plt.title('Monthly Sales Proportion')

plt.tight_layout()
plt.show()

# Scatter plot penjualan vs. persediaan
plt.figure(figsize=(8, 6))
plt.scatter(adidas_data['Inventory'], adidas_data['Sales'], color='purple')
plt.title('Sales vs. Inventory')
plt.xlabel('Inventory')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
