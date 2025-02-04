import laspy
import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree

def load_dem(file_path):
    """Loads DEM from an SHP file and returns a geopandas DataFrame."""
    return gpd.read_file(file_path)

def load_lidar_data(file_path):
    """Loads a point cloud from a LAZ file and returns an XYZ matrix."""
    las_data = laspy.read(file_path)
    return np.column_stack((las_data.x, las_data.y, las_data.z))

def calculate_height_difference(lidar_points, dem_data):
    """Calculates the height difference between the point cloud and the DEM model."""
    dem_points = np.array([(geom.x, geom.y, height) for geom, height in zip(dem_data.geometry, dem_data['Z'])])
    
    dem_kdtree = cKDTree(dem_points[:, :2])
    _, nearest_indices = dem_kdtree.query(lidar_points[:, :2])
    
    dem_heights = dem_points[nearest_indices, 2]
    return lidar_points[:, 2] - dem_heights

def compute_error_metrics(height_differences):
    """Calculates accuracy metrics for the height difference."""
    return {
        "Mean Bias": np.mean(height_differences),
        "Standard Deviation": np.std(height_differences),
        "Root Mean Square Error (RMSE)": np.sqrt(np.mean(height_differences ** 2)),
        "Min Difference": np.min(height_differences),
        "Max Difference": np.max(height_differences),
    }

def main():
    dem_path = "Lubin_2024_03_27_pc_t2.shp"
    lidar_path = "Lubin_2021_09_26_pc.laz"
    
    print("Loading data...")
    dem = load_dem(dem_path)
    lidar_points = load_lidar_data(lidar_path)
    
    print("Calculating height difference...")
    height_diff = calculate_height_difference(lidar_points, dem)
    
    print("Accuracy analysis...")
    metrics = compute_error_metrics(height_diff)
    
    print("\n Analysis results:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

if __name__ == "__main__":
    main()
