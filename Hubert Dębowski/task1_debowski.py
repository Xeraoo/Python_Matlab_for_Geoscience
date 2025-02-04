import rasterio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#read temp 1 ndvi1
file_paths = {
    "NDVI Spring": ("data_task1/t1_ndvi2024May.tif", "Greens"),
    "NDVI Summer": ("data_task1/t1_ndvi2023_Jul_Aug.tif", "Greens"),
    "Temperature Spring": ("data_task1/t1_lst2024May.tif", "coolwarm"),
    "Temperature Summer": ("data_task1/t1_lst2023_Jul_Aug.tif", "coolwarm")
}

def read_tif(filepath):
    with rasterio.open(filepath) as dataset:
        return dataset.read(1)

data_dict = {key: read_tif(path) for key, (path, _) in file_paths.items()}

#display images
def plot_images(data_dict, file_paths):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    for ax, (title, data) in zip(axes.flat, data_dict.items()):
        cmap = file_paths[title][1]
        img = ax.imshow(data, cmap=cmap)
        ax.set_title(title)
        fig.colorbar(img, ax=ax)
    plt.tight_layout()
    plt.show()

plot_images(data_dict, file_paths)

#create histograms
def plot_histograms(data_dict):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # NDVI Histogram
    sns.histplot(data_dict["NDVI Spring"].flatten(), bins=30, kde=True, ax=ax[0], color='green', label='NDVI Spring')
    sns.histplot(data_dict["NDVI Summer"].flatten(), bins=30, kde=True, ax=ax[0], color='darkgreen', alpha=0.7, label='NDVI Summer')
    ax[0].set_title('NDVI Histogram')
    ax[0].legend()

    # Temperature Histogram
    sns.histplot(data_dict["Temperature Spring"].flatten(), bins=30, kde=True, ax=ax[1], color='blue', label='Temperature Spring')
    sns.histplot(data_dict["Temperature Summer"].flatten(), bins=30, kde=True, ax=ax[1], color='red', alpha=0.7, label='Temperature Summer')
    ax[1].set_title('Temperature Histogram')
    ax[1].legend()

    plt.show()

plot_histograms(data_dict)

#scatter plot (NDVI vs Temperature)
def plot_scatter(data_dict):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data_dict["NDVI Spring"].flatten(), y=data_dict["Temperature Spring"].flatten(), color='blue', alpha=0.5, label='Spring')
    sns.scatterplot(x=data_dict["NDVI Summer"].flatten(), y=data_dict["Temperature Summer"].flatten(), color='red', alpha=0.5, label='Summer')
    plt.xlabel('NDVI')
    plt.ylabel('Temperature')
    plt.title('Scatter Plot: NDVI vs Temperature')
    plt.legend()
    plt.show()

plot_scatter(data_dict)
