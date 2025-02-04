import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
from skimage.transform import resize
from rasterio.plot import show

# 1. Wczytaj dane Sentinel-2
sentinel_path = 'C:/Users/tymot/OneDrive/Pulpit/Egzamin_Python/Sentinel2_GZM_AllBands.tif'  # Podmień na właściwą ścieżkę
with rasterio.open(sentinel_path) as dataset:
    img = dataset.read()  # Odczytaj wszystkie pasma
    profile = dataset.profile  # Pobierz metadane

# 2. Przygotowanie danych do K-Means
bands, height, width = img.shape
img_reshaped = img.reshape(bands, -1).T  # Przekształcenie na format [piksele, cechy]

# 3. Wykonaj klasyfikację K-Means
n_clusters = 5  # Liczba klas
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
kmeans.fit(img_reshaped)
classified = kmeans.labels_.reshape(height, width)

# 4. Zapisz wynikową klasyfikację
classified_path = 'C:/Users/tymot/OneDrive/Pulpit/Egzamin_Python/Sentinel2_KMeans.tif'
with rasterio.open(
    classified_path, 'w',
    driver='GTiff',
    height=height, width=width,
    count=1, dtype='uint8',
    crs=profile['crs'], transform=profile['transform']
) as dst:
    dst.write(classified.astype(np.uint8), 1)

print("Klasyfikacja zakończona. Wynik zapisano jako Sentinel2_KMeans.tif")

# 5. Wizualizacja wyników
plt.figure(figsize=(10, 5))
plt.imshow(classified, cmap='tab10')
plt.title("Klasyfikacja K-Means")
plt.colorbar()
plt.show()

# 6. Pobranie i przygotowanie mapy LULC
lulc_path = 'C:/Users/tymot/OneDrive/Pulpit/Egzamin_Python/LULC_GZM.tif'  # Podmień na odpowiednią mapę LULC
with rasterio.open(lulc_path) as dataset:
    lulc = dataset.read(1)

# 7. Dostosowanie rozdzielczości danych referencyjnych (LULC)
if lulc.shape != classified.shape:
    lulc_resized = resize(lulc, (height, width), mode='reflect', preserve_range=True)
    print("Dostosowano rozdzielczość danych LULC.")
else:
    lulc_resized = lulc

# 8. Zapisz dostosowane dane referencyjne
lulc_resized_path = 'C:/Users/tymot/OneDrive/Pulpit/Egzamin_Python/LULC_GZM_Resized.tif'
with rasterio.open(
    lulc_resized_path, 'w',
    driver='GTiff',
    height=height, width=width,
    count=1, dtype='float32',
    crs=profile['crs'], transform=profile['transform']
) as dst:
    dst.write(lulc_resized.astype(np.float32), 1)

print("Dane referencyjne zapisano jako LULC_GZM_Resized.tif")

# 9. Wizualizacja danych referencyjnych
plt.figure(figsize=(10, 5))
plt.imshow(lulc_resized, cmap='tab20b')
plt.title("Mapa LULC - Dostosowana rozdzielczość")
plt.colorbar()
plt.show()

# 10. Wykonanie analizy dokładności
accuracy_script = 'C:/Users/tymot/OneDrive/Pulpit/Egzamin_Python/accuracy.py'  # Ścieżka do skryptu accuracy.py
os.system(f'python {accuracy_script} {classified_path} {lulc_resized_path}')

print("Analiza dokładności zakończona.")
