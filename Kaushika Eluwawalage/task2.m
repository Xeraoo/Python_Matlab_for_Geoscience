% Function to load DEM from a shapefile
function dem = load_dem(dem_path)
    % Check if the file exists at the given path
    if exist(dem_path, 'file') == 2
        % Load DEM as a geospatial table using readgeotable
        dem = readgeotable(dem_path);
        disp('DEM loaded successfully.');
    else
        error('The DEM file does not exist or the path is incorrect.');
    end
end

% Function to load LIDAR data from a shapefile
function lidar_points = load_lidar_data(lidar_path)
    % Check if the shapefile exists
    if exist(lidar_path, 'file') == 2
        % Read shapefile and extract coordinates (X, Y, Z)
        lidar_data = readgeotable(lidar_path);  % Read shapefile into a geospatial table
        lidar_points = [lidar_data.X, lidar_data.Y, lidar_data.Z];  % Convert to XYZ matrix
        disp('LIDAR data loaded successfully.');
    else
        error('The LIDAR shapefile does not exist or the path is incorrect.');
    end
end

% Function to calculate height difference between LIDAR and DEM
function height_diff = calculate_height_difference(lidar_points, dem_data)
    % Extract X, Y, and Z from DEM
    dem_points = [dem_data.X, dem_data.Y, dem_data.Z];
    
    % Perform a nearest neighbor search between LIDAR points and DEM points
    [~, nearest_indices] = knnsearch(dem_points(:, 1:2), lidar_points(:, 1:2));
    
    % Get corresponding DEM heights
    dem_heights = dem_points(nearest_indices, 3);
    
    % Calculate height differences (LIDAR Z - DEM Z)
    height_diff = lidar_points(:, 3) - dem_heights;
end

% Function to compute error metrics
function metrics = compute_error_metrics(height_differences)
    % Calculate various accuracy metrics
    metrics.MeanBias = mean(height_differences);
    metrics.StandardDeviation = std(height_differences);
    metrics.RMSE = sqrt(mean(height_differences .^ 2));
    metrics.MinDifference = min(height_differences);
    metrics.MaxDifference = max(height_differences);
end

% Main script to execute the analysis
% Update the paths to the correct locations
dem_path = 'C:\Users\Kaushi\Downloads\files3\Lubin_2024_03_27_pc_team3\Lubin_2024_03_27_pc_team3.shp';  % Path to DEM shapefile
lidar_path = 'C:\Users\Kaushi\Downloads\files3\Lubin_2024_03_27_pc_team3\Lubin_2024_03_27_pc_team3.shp';  % Path to LIDAR shapefile

% Ensure the files exist before processing
if exist(dem_path, 'file') == 2
    disp('DEM file found.');
else
    error('DEM file not found at specified path.');
end

if exist(lidar_path, 'file') == 2
    disp('LIDAR file found.');
else
    error('LIDAR file not found at specified path.');
end

fprintf('Loading data...\n');

% Load DEM and LIDAR data
dem = load_dem(dem_path);
lidar_points = load_lidar_data(lidar_path);

fprintf('Calculating height difference...\n');

% Calculate height differences
height_diff = calculate_height_difference(lidar_points, dem);

fprintf('Accuracy analysis...\n');

% Compute error metrics
metrics = compute_error_metrics(height_diff);

% Display the results
fprintf('\nAnalysis Results:\n');
fprintf('Mean Bias: %.4f\n', metrics.MeanBias);
fprintf('Standard Deviation: %.4f\n', metrics.StandardDeviation);
fprintf('Root Mean Square Error (RMSE): %.4f\n', metrics.RMSE);
fprintf('Min Difference: %.4f\n', metrics.MinDifference);
fprintf('Max Difference: %.4f\n', metrics.MaxDifference);




