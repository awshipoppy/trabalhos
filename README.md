# trabalhos
Trabalhos para o dia 13/11
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para adicionar ruído sal e pimenta
def add_salt_and_pepper_noise(img):
    row, col = img.shape  # Ajuste para imagem em escala de cinza
    out = np.copy(img)

    number_of_pixels = 100000
    for _ in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        out[y_coord, x_coord] = 255  # Sal (branco)

    for _ in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        out[y_coord, x_coord] = 0  # Pimenta (preto)

    return out

# Função para adicionar ruído gaussiano
def add_gaussian_noise(img):
    row, col = img.shape  # Ajuste para imagem em escala de cinza
    mean = 0
    sigma = 50  # Desvio padrão
    gauss = np.random.normal(mean, sigma, (row, col)).astype('uint8')  # 1 canal para escala de cinza
    noisy = cv2.add(img, gauss)
    return noisy

# Carregar a imagem em escala de cinza
img = cv2.imread('moto.33.20-1.jpeg', cv2.IMREAD_GRAYSCALE)

# Adicionar ruído
salt_and_pepper = add_salt_and_pepper_noise(img)
gaussian_noise = add_gaussian_noise(img)

# Aplicar filtros no sal e pimenta
mean_filtered = cv2.GaussianBlur(salt_and_pepper, (5, 5), 0)
median_filtered = cv2.medianBlur(salt_and_pepper, 5)
bilateral_filtered = cv2.bilateralFilter(salt_and_pepper, 9, 75, 75)

# Aplicar filtros no gaussiano
mean_g_filtered = cv2.GaussianBlur(gaussian_noise, (5, 5), 0)
median_g_filtered = cv2.medianBlur(gaussian_noise, 5)
bilateral_g_filtered = cv2.bilateralFilter(gaussian_noise, 9, 75, 75)

# Visualizar os resultados
plt.figure(figsize=(12, 10))

plt.subplot(3, 3, 1)
plt.title('Imagem Original')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.title('Ruído Sal e Pimenta')
plt.imshow(salt_and_pepper, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.title('Ruído Gaussiano')
plt.imshow(gaussian_noise, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.title('Filtro da Média (Gaussiano) Sal e Pimenta')
plt.imshow(mean_filtered, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.title('Filtro da Mediana Sal e Pimenta')
plt.imshow(median_filtered, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.title('Filtro Bilateral Sal e Pimenta')
plt.imshow(bilateral_filtered, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.title('Filtro de Média (Gaussiano) Ruído Gaussiano')
plt.imshow(mean_g_filtered, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 8)
plt.title('Filtro da Mediana Ruído Gaussiano')
plt.imshow(median_g_filtered, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 9)
plt.title('Filtro Bilateral Ruído Gaussiano')
plt.imshow(bilateral_g_filtered, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
![image](https://github.com/user-attachments/assets/4f7d78d0-a8b1-4f49-a82b-7bd038747bd6)
