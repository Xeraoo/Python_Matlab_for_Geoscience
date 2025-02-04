% File paths for the data
files = struct('ndvi_spring', 'C:\EGZ\taks1\t3_ndvi2024May.tif', ...
               'ndvi_summer', 'C:\EGZ\taks1\t3_ndvi2023_Jul_Aug.tif', ...
               'temp_spring', 'C:\EGZ\taks1\t3_lst2024May.tif', ...
               'temp_summer', 'C:\EGZ\taks1\t3_lst2023_Jul_Aug.tif');

% Function to load a TIFF file
function img = load_image(file)
    img = imread(file);  % Load the image from the file
end

% Load the data using a loop
data = struct();
fields = fieldnames(files);
for i = 1:length(fields)
    data.(fields{i}) = load_image(files.(fields{i}));
end

% Set colormap options for the plots
colormap_spring = 'spring';
colormap_temp = {'cool', 'hot'};

% Create the images and display them
figure;
subplot(2, 2, 1);
imshow(data.ndvi_spring, []); % Display NDVI Spring image
colormap(colormap_spring);
colorbar;
title('NDVI Spring');

subplot(2, 2, 2);
imshow(data.ndvi_summer, []); % Display NDVI Summer image
colormap(colormap_spring);
colorbar;
title('NDVI Summer');

subplot(2, 2, 3);
imshow(data.temp_spring, []); % Display Temperature Spring image
colormap(colormap_temp{1});
colorbar;
title('Temperature Spring');

subplot(2, 2, 4);
imshow(data.temp_summer, []); % Display Temperature Summer image
colormap(colormap_temp{2});
colorbar;
title('Temperature Summer');

% Main title for the figure
sgtitle('NDVI and Temperature Images');
set(gcf, 'Position', [100, 100, 800, 600]);  % Set the figure window size

% Plot the histograms
figure;
hold on;
% NDVI histograms
subplot(1, 2, 1);
histogram(data.ndvi_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#00FF00', 'EdgeColor', 'black');
histogram(data.ndvi_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#006400', 'EdgeColor', 'black');
title('NDVI Histogram');
legend('NDVI Spring', 'NDVI Summer');

% Temperature histograms
subplot(1, 2, 2);
histogram(data.temp_spring(:), 30, 'Normalization', 'pdf', 'FaceColor', '#0000FF', 'EdgeColor', 'black');
histogram(data.temp_summer(:), 30, 'Normalization', 'pdf', 'FaceColor', '#FF0000', 'EdgeColor', 'black');
title('Temperature Histogram');
legend('Temperature Spring', 'Temperature Summer');
hold off;

% Scatter plot: NDVI vs Temperature
figure;
hold on;
scatter(data.ndvi_spring(:), data.temp_spring(:), 20, 'blue', 'filled', 'MarkerFaceAlpha', 0.5);
scatter(data.ndvi_summer(:), data.temp_summer(:), 20, 'red', 'filled', 'MarkerFaceAlpha', 0.5);
xlabel('NDVI');
ylabel('Temperature');
title('Scatter Plot: NDVI vs. Temperature');
legend('Spring', 'Summer');
hold off;
