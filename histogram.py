import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(image):
    histogram = np.zeros(256, dtype=int)
    for row in image:
        for pixel_value in row:
            histogram[pixel_value] += 1
    return histogram

def cumulative_histogram(histogram):
    cumulative_histogram = np.zeros(256, dtype=int)
    cumulative_histogram[0] = histogram[0]
    for i in range(1, 256):
        cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i]
    return cumulative_histogram

def histogram_equalization(image):
    image_height, image_width = image.shape
    total_pixel_count = image_height * image_width
    histogram_values = histogram(image)
    cumulative_histogram_values = cumulative_histogram(histogram_values)

    equalized_image = np.zeros_like(image)

    min_cumulative_value = next(value for value in cumulative_histogram_values if value > 0)
    for row in range(image_height):
        for col in range(image_width):
            pixel_value = image[row, col]
            equalized_image[row, col] = round((cumulative_histogram_values[pixel_value] - min_cumulative_value) / (total_pixel_count - min_cumulative_value) * 255)

    return equalized_image

def histogram_stretching(image):
    stretched_image = np.zeros_like(image)
    min_pixel_value = np.min(image)
    max_pixel_value = np.max(image)

    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            stretched_image[row, col] = round((image[row, col] - min_pixel_value) / (max_pixel_value - min_pixel_value) * 255)

    return stretched_image


img = cv2.imread('tree.jpeg', cv2.IMREAD_GRAYSCALE)

equalized = histogram_equalization(img)
stretched = histogram_stretching(img)

plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1)
plt.title('Görüntü')
plt.imshow(img, cmap='gray')
plt.subplot(2, 3, 2)
plt.title('Histogram Eşitlemeli Görüntü')
plt.imshow(equalized, cmap='gray')
plt.subplot(2, 3, 3)
plt.title('Histogram Germeli Görüntü')
plt.imshow(stretched, cmap='gray')

plt.subplot(2, 3, 4)
plt.title('Görüntü Histogramı')
plt.plot(histogram(img))
plt.subplot(2, 3, 5)
plt.title('Eşitlenmiş Görüntü Histogramı')
plt.plot(histogram(equalized))
plt.subplot(2, 3, 6)
plt.title('Genişletilmiş Görüntü Histogramı')
plt.plot(histogram(stretched))

plt.tight_layout()
plt.show()
