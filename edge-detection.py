import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def prewitt_edge_detection(img_array):
    Gx = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]])

    Gy = np.array([[-1, -1, -1],
                   [0, 0, 0],
                   [1, 1, 1]])

    height, width = img_array.shape
    edges = np.zeros((height, width), dtype=np.float32)

    for y in range(1, height-1):
        for x in range(1, width-1):
            region = img_array[y-1:y+2, x-1:x+2]
            gx = np.sum(Gx * region)
            gy = np.sum(Gy * region)
            edges[y, x] = np.sqrt(gx**2 + gy**2)

    return edges

def roberts_edge_detection(img_array):
    Gx = np.array([[1, 0],
                   [0, -1]])

    Gy = np.array([[0, 1],
                   [-1, 0]])

    height, width = img_array.shape
    edges = np.zeros((height, width), dtype=np.float32)

    for y in range(height-1):
        for x in range(width-1):
            region = img_array[y:y+2, x:x+2]
            gx = np.sum(Gx * region)
            gy = np.sum(Gy * region)
            edges[y, x] = np.sqrt(gx**2 + gy**2)

    return edges

def main():
    image = Image.open('bina.jpg').convert('L')
    img_array = np.array(image)

    prewitt_edges = prewitt_edge_detection(img_array)
    roberts_edges = roberts_edge_detection(img_array)

    prewitt_image = Image.fromarray(np.clip(prewitt_edges, 0, 255).astype('uint8'))
    roberts_image = Image.fromarray(np.clip(roberts_edges, 0, 255).astype('uint8'))

    _, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].imshow(image, cmap='gray')
    axs[0].set_title('Original')
    axs[0].axis('off')

    axs[1].imshow(prewitt_image, cmap='gray')
    axs[1].set_title('Prewitt Kenar Belirleme')
    axs[1].axis('off')

    axs[2].imshow(roberts_image, cmap='gray')
    axs[2].set_title('Roberts Kenar Belirleme')
    axs[2].axis('off')

    plt.show()

if __name__ == '__main__':
    main()
