% File paths for the data
ndvi_spring = 'data_task1/t1_ndvi2024May.tif';
ndvi_summer = 'data_task1/t1_ndvi2023_Jul_Aug.tif';
temp_spring = 'data_task1/t1_lst2024May.tif';
temp_summer = 'data_task1/t1_lst2023_Jul_Aug.tif';

% Function to read a tif file
function data = read_tif(filepath)
    data = imread(filepath); % Use imread to load the image
end

% Read the data
ndvi_spring = read_tif(ndvi_spring);
ndvi_summer = read_tif(ndvi_summer);
temp_spring = read_tif(temp_spring);
temp_summer = read_tif(temp_summer);

% Plotting the images
figure;

% Set up a 2x2 grid for subplots
subplot(2, 2, 1);
imagesc(ndvi_spring);
colormap('spring');  % Use the 'spring' colormap for NDVI
colorbar;
title('NDVI Spring');

subplot(2, 2, 2);
imagesc(ndvi_summer);
colormap('spring');  % Use the 'spring' colormap for NDVI
colorbar;
title('NDVI Summer');

subplot(2, 2, 3);
imagesc(temp_spring);
colormap('cool');  % Use the 'cool' colormap for Temperature
colorbar;
title('Temperature Spring');

subplot(2, 2, 4);
imagesc(temp_summer);
colormap('hot');  % Use the 'hot' colormap for Temperature
colorbar;
title('Temperature Summer');

% Adjust the layout by adding some space between subplots
sgtitle('NDVI and Temperature Images'); % Title for the entire figure
set(gcf, 'Position', [100, 100, 800, 600]); % Adjust the size of the figure window

% Plot histograms
figure;

% Plot NDVI histograms
subplot(1, 2, 1);
hold on;
histogram(ndvi_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#00FF00', 'EdgeColor', 'black');  % Green
histogram(ndvi_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#006400', 'EdgeColor', 'black');  % Dark Green
title('NDVI Histogram');
legend('NDVI Spring', 'NDVI Summer');
hold off;

% Plot Temperature histograms
subplot(1, 2, 2);
hold on;
histogram(temp_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#0000FF', 'EdgeColor', 'black');  % Blue
histogram(temp_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#FF0000', 'EdgeColor', 'black');  % Red
title('Temperature Histogram');
legend('Temperature Spring', 'Temperature Summer');
hold off;

% Scatter plot of NDVI vs Temperature
figure;
hold on;
scatter(ndvi_spring(:), temp_spring(:), 20, 'blue', 'filled', 'MarkerFaceAlpha', 0.5, 'DisplayName', 'Spring');
scatter(ndvi_summer(:), temp_summer(:), 20, 'red', 'filled', 'MarkerFaceAlpha', 0.5, 'DisplayName', 'Summer');
xlabel('NDVI');
ylabel('Temperature');
title('Scatter Plot: NDVI vs. Temperature');
legend;
hold off;
