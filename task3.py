import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from rasterio.plot import show
from osgeo import gdal

# 1. Wczytaj dane Sentinel-2
sentinel_path = 'Sentinel2.tif'  # Podmień na właściwą ścieżkę
with rasterio.open(sentinel_path) as dataset:
    img = dataset.read()  # Odczytaj wszystkie pasma
    profile = dataset.profile  # Pobierz metadane
    
# 2. Przygotowanie danych do K-Means
bands, height, width = img.shape
img_reshaped = img.reshape(bands, -1).T  # Przekształcenie na format [piksele, cechy]

# 3. Wykonaj klasyfikację K-Means
n_clusters = 5  # Liczba klas
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(img_reshaped)
classified = kmeans.labels_.reshape(height, width)

# 4. Zapisz wynikową klasyfikację
classified_path = 'Sentinel2_KMeans.tif'
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

# 6. Pobranie i przygotowanie mapy LULC (zakładamy, że LULC jest w tej samej rozdzielczości)
lulc_path = 'LULC_Reference.tif'  # Ścieżka do mapy referencyjnej
lulc = rasterio.open(lulc_path).read(1)

# 7. Wykonanie analizy dokładności (zakładamy, że accuracy.py jest w tym samym folderze)
import os
os.system(f'python accuracy.py {classified_path} {lulc_path}')
