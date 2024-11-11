# Trabalhos
Trabalhos para o dia 13/11

# Atividade de Ruido de Sal e Pimenta 

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


# Projeto para Prova
Apliquei todos os filtros, ruídos e transformações diferentes em uma imagem que encontrei na internet antiga para ver qual seria a melhor para fazer a limpeza dela, o código foi o seguinte

import cv2
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

# Carrega a imagem
imagem = cv2.imread("familia.jpg", cv2.IMREAD_GRAYSCALE)

# Função corrigida para adicionar ruído sal e pimenta
def ruido_sal_pimenta(imagem, proporcao_sal=0.02, proporcao_pimenta=0.02):
    imagem_ruidosa = np.copy(imagem)
    num_sal = int(proporcao_sal * imagem.size)
    num_pimenta = int(proporcao_pimenta * imagem.size)

    # Aplica o ruído sal
    coords_sal = [np.random.randint(0, i, num_sal) for i in imagem.shape]
    imagem_ruidosa[coords_sal[0], coords_sal[1]] = 255

    # Aplica o ruído pimenta
    coords_pimenta = [np.random.randint(0, i, num_pimenta) for i in imagem.shape]
    imagem_ruidosa[coords_pimenta[0], coords_pimenta[1]] = 0

    return imagem_ruidosa

# Função corrigida para adicionar ruído Gaussiano
def ruido_gaussiano(imagem, sigma=25):
    ruido = np.random.normal(0, sigma, imagem.shape).astype(np.float32)
    imagem_ruidosa = imagem.astype(np.float32) + ruido
    imagem_ruidosa = np.clip(imagem_ruidosa, 0, 255).astype(np.uint8)
    return imagem_ruidosa


# Aplica o filtro de média
imagem_media = cv2.blur(imagem, (5, 5))

# Aplica o filtro de mediana
imagem_mediana = cv2.medianBlur(imagem, 5)

# Aplica o filtro gaussiano
imagem_gaussiana = cv2.GaussianBlur(imagem, (5, 5), 1)

# Aplica o filtro de Sobel
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)
imagem_sobel = cv2.magnitude(sobel_x, sobel_y)

# Transformada de Fourier
f_transformada = np.fft.fft2(imagem)
f_transformada_centralizada = np.fft.fftshift(f_transformada)
espectro = np.log(1 + np.abs(f_transformada_centralizada))

# Transformada Wavelet
import pywt
coeffs2 = pywt.dwt2(imagem, 'haar')
LL, (LH, HL, HH) = coeffs2
imagem_wavelet = np.log(np.abs(LL) + 1)

# Adiciona ruídos
imagem_sal_pimenta = ruido_sal_pimenta(imagem)
imagem_gaussiano = ruido_gaussiano(imagem)

# Exibe os resultados
plt.figure(figsize=(12, 10))
plt.subplot(3, 3, 1), plt.imshow(imagem, cmap='gray'), plt.title("Original")
plt.subplot(3, 3, 2), plt.imshow(imagem_media, cmap='gray'), plt.title("Filtro de Média")
plt.subplot(3, 3, 3), plt.imshow(imagem_mediana, cmap='gray'), plt.title("Filtro de Mediana")
plt.subplot(3, 3, 4), plt.imshow(imagem_gaussiana, cmap='gray'), plt.title("Filtro Gaussiano")
plt.subplot(3, 3, 5), plt.imshow(imagem_sobel, cmap='gray'), plt.title("Filtro de Sobel")
plt.subplot(3, 3, 6), plt.imshow(espectro, cmap='gray'), plt.title("Transformada de Fourier")
plt.subplot(3, 3, 7), plt.imshow(imagem_wavelet, cmap='gray'), plt.title("Transformada Wavelet")
plt.subplot(3, 3, 8), plt.imshow(imagem_sal_pimenta, cmap='gray'), plt.title("Ruído Sal & Pimenta")
plt.subplot(3, 3, 9), plt.imshow(imagem_gaussiano, cmap='gray'), plt.title("Ruído Gaussiano")

plt.tight_layout()
plt.show()
![image](https://github.com/user-attachments/assets/c42cbe53-ee6c-4b41-bbae-dc15d20ec79f)
$ Consideração
Como da para ver, a transformação de wavelets ficou consideravelmente melhor do que a de Fourier, outra que o filtro de gaussiano continua dando esse erro estranho, não consegui arruma-lo
