%% File paths for the data
ndvi_spring = 't2_ndvi2024.tif';
ndvi_summer = 't2_ndvi2023.tif';
temp_spring = 't2_lst2024.tif';
temp_summer = 't2_lst2023.tif';

% Function to read a tif file
function data = read_tif(filepath)
    data = imread(filepath); % Use imread to load the image data from the TIFF file
end

%% Read the data
ndvi_spring = read_tif(ndvi_spring);
ndvi_summer = read_tif(ndvi_summer);
temp_spring = read_tif(temp_spring);
temp_summer = read_tif(temp_summer);

%% Plot histograms
figure;

% Plot Temperature histograms
subplot(1, 2, 1);
hold on;
histogram(temp_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#0000FF', 'EdgeColor', 'black');  % Blue for spring temperature
histogram(temp_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#FF0000', 'EdgeColor', 'black');  % Red for summer temperature
title('Temperature Histogram');
legend('Temperature Spring', 'Temperature Summer');
hold off;

% Plot NDVI histograms
subplot(1, 2, 2);
hold on;
histogram(ndvi_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#00FF00', 'EdgeColor', 'black');  % Green for spring NDVI
histogram(ndvi_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#006400', 'EdgeColor', 'black');  % Dark Green for summer NDVI
title('NDVI Histogram');
legend('NDVI Spring', 'NDVI Summer');
hold off;

%% Plotting the images
figure;

% Set up a 2x2 grid for subplots to display the images
subplot(2, 2, 1);
imagesc(ndvi_spring);  % Display the NDVI spring image
colormap('spring');  % Use the 'spring' colormap for NDVI visualization
colorbar;
title('NDVI Spring');

subplot(2, 2, 2);
imagesc(ndvi_summer);  % Display the NDVI summer image
colormap('spring');  % Use the 'spring' colormap for NDVI visualization
colorbar;
title('NDVI Summer');

subplot(2, 2, 3);
imagesc(temp_spring);  % Display the temperature spring image
colormap('cool');  % Use the 'cool' colormap for temperature visualization
colorbar;
title('Temperature Spring');

subplot(2, 2, 4);
imagesc(temp_summer);  % Display the temperature summer image
colormap('hot');  % Use the 'hot' colormap for temperature visualization
colorbar;
title('Temperature Summer');

% Adjust the layout by adding some space between subplots
sgtitle('NDVI and Temperature Images'); % Title for the entire figure
set(gcf, 'Position', [100, 100, 800, 600]); % Adjust the size of the figure window

%% Scatter plot of NDVI vs Temperature
figure;
hold on;
scatter(ndvi_spring(:), temp_spring(:), 20, 'blue', 'filled', 'MarkerFaceAlpha', 0.5, 'DisplayName', 'Spring');
scatter(ndvi_summer(:), temp_summer(:), 20, 'red', 'filled', 'MarkerFaceAlpha', 0.5, 'DisplayName', 'Summer');
xlabel('NDVI');
ylabel('Temperature');
title('Scatter Plot: NDVI vs. Temperature');
legend;
hold off;
