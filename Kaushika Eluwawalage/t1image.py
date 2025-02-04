import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import rasterio  # For reading raster images

# Function to load the image
def load_image(file_path):
    with rasterio.open(file_path) as src:
        return src.read(1)  # Read the first band

# Load your images (update the path as necessary)
t1_lst2023_Jul_Aug = load_image(r"c:\Users\Kaushi\Downloads\t1_lst2023_Jul_Aug.tif")
t1_lst2024May = load_image(r"c:\Users\Kaushi\Downloads\t1_lst2024May.tif")
t1_ndvi2023_Jul_Aug = load_image(r"c:\Users\Kaushi\Downloads\t1_ndvi2023_Jul_Aug.tif")
t1_ndvi2024May = load_image(r"c:\Users\Kaushi\Downloads\t1_ndvi2024May.tif")

# Display Images
def display_images(temp, ndvi, title):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(temp, cmap='hot')
    plt.colorbar()
    plt.title(f'{title} - Temperature')

    plt.subplot(1, 3, 2)
    plt.imshow(ndvi, cmap='Greens')
    plt.colorbar()
    plt.title(f'{title} - NDVI')

    plt.subplot(1, 3, 3)
    plt.imshow(temp, cmap='hot', alpha=0.6)
    plt.imshow(ndvi, cmap='Greens', alpha=0.4)
    plt.colorbar()
    plt.title(f'{title} - Combined')

    plt.show()

display_images(t1_lst2023_Jul_Aug, t1_ndvi2023_Jul_Aug, "2023 July-August")
display_images(t1_lst2024May, t1_ndvi2024May, "2024 May")

# Histograms
def plot_histograms(temp, ndvi, title):
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.hist(temp.flatten(), bins=30, color='red', alpha=0.7)
    plt.title(f'{title} - Temperature Histogram')
    
    plt.subplot(1, 2, 2)
    plt.hist(ndvi.flatten(), bins=30, color='green', alpha=0.7)
    plt.title(f'{title} - NDVI Histogram')
    
    plt.show()

plot_histograms(t1_lst2023_Jul_Aug, t1_ndvi2023_Jul_Aug, "2023 July-August")
plot_histograms(t1_lst2024May, t1_ndvi2024May, "2024 May")

# Scatter Plot
def scatter_plot(ndvi, temp, title):
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=ndvi.flatten(), y=temp.flatten(), alpha=0.5)
    plt.xlabel('NDVI')
    plt.ylabel('Temperature')
    plt.title(f'Scatter Plot ({title})')
    plt.show()

scatter_plot(t1_ndvi2023_Jul_Aug, t1_lst2023_Jul_Aug, "2023 July-August")
scatter_plot(t1_ndvi2024May, t1_lst2024May, "2024 May")
