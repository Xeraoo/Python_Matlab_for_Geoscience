import rasterio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ścieżki do plików TIFF
ndvi_spring_path = "t3_ndvi2024May.tif"
ndvi_summer_path = "t3_ndvi2023_Jul_Aug.tif"
temp_spring_path = "t3_lst2024May.tif"
temp_summer_path = "t3_lst2023_Jul_Aug.tif"

# Funkcja do wczytania danych z pliku TIFF
def read_tif(filepath):
    with rasterio.open(filepath) as dataset:
        return dataset.read(1)  # Czytamy tylko pierwszą warstwę

# Wczytanie danych
ndvi_spring = read_tif(ndvi_spring_path)
ndvi_summer = read_tif(ndvi_summer_path)
temp_spring = read_tif(temp_spring_path)
temp_summer = read_tif(temp_summer_path)

# Wyświetlenie 4 obrazów
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

images = [
    (ndvi_spring, "NDVI Wiosna", "Greens"),
    (ndvi_summer, "NDVI Lato", "Greens"),
    (temp_spring, "Temp. Wiosna", "coolwarm"),
    (temp_summer, "Temp. Lato", "coolwarm")
]

for ax, (data, title, cmap) in zip(axes.flat, images):
    img = ax.imshow(data, cmap=cmap)
    ax.set_title(title)
    fig.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()

# Tworzenie histogramów
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(ndvi_spring.flatten(), bins=30, kde=True, ax=ax[0], color='green', label='NDVI Wiosna')
sns.histplot(ndvi_summer.flatten(), bins=30, kde=True, ax=ax[0], color='darkgreen', alpha=0.7, label='NDVI Lato')
ax[0].set_title('Histogram NDVI')
ax[0].legend()

sns.histplot(temp_spring.flatten(), bins=30, kde=True, ax=ax[1], color='blue', label='Temp Wiosna')
sns.histplot(temp_summer.flatten(), bins=30, kde=True, ax=ax[1], color='red', alpha=0.7, label='Temp Lato')
ax[1].set_title('Histogram Temperatury')
ax[1].legend()

plt.show()

# Wykres rozrzutu (NDVI vs Temperatura)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=ndvi_spring.flatten(), y=temp_spring.flatten(), color='blue', alpha=0.5, label='Wiosna')
sns.scatterplot(x=ndvi_summer.flatten(), y=temp_summer.flatten(), color='red', alpha=0.5, label='Lato')
plt.xlabel('NDVI')
plt.ylabel('Temperatura')
plt.title('Wykres rozrzutu: NDVI vs. Temperatura')
plt.legend()
plt.show()