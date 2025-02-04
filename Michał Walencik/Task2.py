import laspy
import geopandas as gpd
import rasterio
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree

# 1. Load DEM from SHP file (2024)
def read_dem(shp_path):
    dem = gpd.read_file(shp_path)
    return dem

# 2. Load point cloud (LAZ 2021)
def read_point_cloud(laz_path):
    las = laspy.read(laz_path)
    return np.vstack((las.x, las.y, las.z)).T  # XYZ matrix

# 3. Compute height difference deltaH = Z_LAZ - Z_DEM
def compute_dh(point_cloud, dem):
    # Create a spatial tree with DEM points
    dem_coords = np.array(list(zip(dem.geometry.x, dem.geometry.y, dem['Z'])))  # height = DEM height
    dem_tree = cKDTree(dem_coords[:, :2])

    # Find the nearest DEM point for each point in the cloud
    distances, indices = dem_tree.query(point_cloud[:, :2])

    # Get the heights from the DEM for the found points
    z_dem = dem_coords[indices, 2]

    # Compute deltaH
    delta_h = point_cloud[:, 2] - z_dem
    return delta_h

# 4. Compute accuracy metrics
def compute_accuracy(delta_h):
    metrics = {
        "Mean Error (Bias)": np.mean(delta_h),
        "Standard Deviation": np.std(delta_h),
        "RMSE": np.sqrt(np.mean(delta_h**2)),
        "Min ΔH": np.min(delta_h),
        "Max ΔH": np.max(delta_h),
    }
    return metrics

# Main function
def main():
    shp_path = "C:/EGZ/Lubin_2024_03_27_pc_t3.shp"  
    laz_path = "C:/EGZ/DTM/Lubin_2021_09_26_pc.laz"  

    print("📥 Loading data...")
    dem = read_dem(shp_path)
    point_cloud = read_point_cloud(laz_path)

    print("📊 Calculating height differences...")
    delta_h = compute_dh(point_cloud, dem)

    print("📈 Calculating accuracy metrics...")
    metrics = compute_accuracy(delta_h)

    # Display results
    print("\n🔹 Results:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

# Run the script
if __name__ == "__main__":
    main()
