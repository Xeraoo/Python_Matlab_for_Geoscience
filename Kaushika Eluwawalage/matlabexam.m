% Load Images
t1_lst2023_Jul_Aug = imread('c:\Users\Kaushi\Downloads\t1_lst2023_Jul_Aug.tif');
t1_lst2024May = imread('c:\Users\Kaushi\Downloads\t1_lst2024May.tif');
t1_ndvi2023_Jul_Aug = imread('c:\Users\Kaushi\Downloads\t1_ndvi2023_Jul_Aug.tif');
t1_ndvi2024May = imread('c:\Users\Kaushi\Downloads\t1_ndvi2024May.tif');
% Display Images for 2023 July-August
figure;
subplot(1,3,1); imagesc(t1_lst2023_Jul_Aug); colormap hot; colorbar; title('2023 July-Aug - Temperature');
subplot(1,3,2); imagesc(t1_ndvi2023_Jul_Aug); colormap summer; colorbar; title('2023 July-Aug - NDVI');
subplot(1,3,3); imagesc(t1_lst2023_Jul_Aug + t1_ndvi2023_Jul_Aug); colorbar; title('2023 July-Aug - Combined');

% Display Images for 2024 May
figure;
subplot(1,3,1); imagesc(t1_lst2024May); colormap hot; colorbar; title('2024 May - Temperature');
subplot(1,3,2); imagesc(t1_ndvi2024May); colormap summer; colorbar; title('2024 May - NDVI');
subplot(1,3,3); imagesc(t1_lst2024May + t1_ndvi2024May); colorbar; title('2024 May - Combined');
% Histogram for 2023 July-August
figure;
subplot(1,2,1); histogram(t1_lst2023_Jul_Aug(:), 30, 'FaceColor', 'r'); title('2023 July-Aug - Temp Histogram');
subplot(1,2,2); histogram(t1_ndvi2023_Jul_Aug(:), 30, 'FaceColor', 'g'); title('2023 July-Aug - NDVI Histogram');

% Histogram for 2024 May
figure;
subplot(1,2,1); histogram(t1_lst2024May(:), 30, 'FaceColor', 'r'); title('2024 May - Temp Histogram');
subplot(1,2,2); histogram(t1_ndvi2024May(:), 30, 'FaceColor', 'g'); title('2024 May - NDVI Histogram');
% Scatter plot for 2023 July-August
figure;
scatter(t1_ndvi2023_Jul_Aug(:), t1_lst2023_Jul_Aug(:), 'b.');
xlabel('NDVI'); ylabel('Temperature');
title('Scatter Plot - 2023 July-Aug');

% Scatter plot for 2024 May
figure;
scatter(t1_ndvi2024May(:), t1_lst2024May(:), 'b.');
xlabel('NDVI'); ylabel('Temperature');
title('Scatter Plot - 2024 May');
% Save the scatter plot as a PNG file
saveas(gcf, 'scatter_plot_2023_Jul_Aug.png');
