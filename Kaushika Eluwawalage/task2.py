import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
import os

def load_dem(file_path):
    """Loads DEM from a shapefile and returns a GeoDataFrame."""
    if os.path.exists(file_path):
        dem = gpd.read_file(file_path)
        print(f"DEM file loaded from {file_path}")
        return dem
    else:
        raise FileNotFoundError(f"DEM file not found at {file_path}")

def load_lidar_data(file_path):
    """Loads LIDAR point cloud from a shapefile and returns a numpy array of XYZ points."""
    if os.path.exists(file_path):
        lidar_data = gpd.read_file(file_path)
        lidar_points = np.column_stack((lidar_data.geometry.x, lidar_data.geometry.y, lidar_data['Z']))
        print(f"LIDAR data loaded from {file_path}")
        return lidar_points
    else:
        raise FileNotFoundError(f"LIDAR shapefile not found at {file_path}")

def calculate_height_difference(lidar_points, dem_data):
    """Calculates height difference between LIDAR points and DEM."""
    dem_points = np.column_stack((dem_data.geometry.x, dem_data.geometry.y, dem_data['Z']))
    
    # Nearest neighbor search using cKDTree
    dem_kdtree = cKDTree(dem_points[:, :2])
    _, nearest_indices = dem_kdtree.query(lidar_points[:, :2])
    
    # Retrieve the corresponding DEM heights
    dem_heights = dem_points[nearest_indices, 2]
    
    # Calculate height difference (LIDAR Z - DEM Z)
    height_diff = lidar_points[:, 2] - dem_heights
    return height_diff

def compute_error_metrics(height_differences):
    """Computes accuracy metrics for the height differences."""
    metrics = {
        "Mean Bias": np.mean(height_differences),
        "Standard Deviation": np.std(height_differences),
        "RMSE": np.sqrt(np.mean(height_differences ** 2)),
        "Min Difference": np.min(height_differences),
        "Max Difference": np.max(height_differences),
    }
    return metrics

def main():
    # Define the paths to your files
    dem_path = r'c:\Users\Kaushi\Downloads\files3\Lubin_2024_03_27_pc_t5\Lubin_2024_03_27_pc_team3.shp'  # Path to DEM shapefile
    lidar_path = r'c:\Users\Kaushi\Downloads\files3\Lubin_2024_03_27_pc_t5\Lubin_2024_03_27_pc_team3.shp'  # Path to LIDAR shapefile

    # Load DEM and LIDAR data
    try:
        dem = load_dem(dem_path)
        lidar_points = load_lidar_data(lidar_path)
    except FileNotFoundError as e:
        print(e)
        return

    print("Calculating height differences...")

    # Calculate height differences between LIDAR and DEM
    height_diff = calculate_height_difference(lidar_points, dem)

    print("Performing accuracy analysis...")

    # Compute accuracy metrics
    metrics = compute_error_metrics(height_diff)

    # Display the metrics
    print("\nAnalysis Results:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

if __name__ == "__main__":
    main()
