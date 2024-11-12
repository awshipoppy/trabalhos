# Trabalhos
Trabalhos para o dia 13/11, aqui estão as atividades de transformação de wavelets e ruido de sal e pimenta e o trabalho de arrumar uma imagem

#Atividade da Transformação de wavelets

import cv2
import pywt
import matplotlib.pyplot as plt

# carregar imagem  e deixar em tons de cinza
image = cv2.imread('castlevania.jpg', cv2.IMREAD_GRAYSCALE)

# realizar a decomposição da imagem em wavelets
coeffs2 = pywt.dwt2(image, 'haar')

# LL: Aproximações - HL, LH, HH: detalhes
LL, (LH, HL, HH) = coeffs2

# Mostrar as imagens

plt.figure(figsize=(10,10))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(LL, cmap='gray')
plt.title('Aproximações')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(LH, cmap='gray')
plt.title('Detalhes (LH)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(HL, cmap='gray')
plt.title('Detalhes (HL)')
plt.axis('off')

plt.tight_layout()
plt.show()

![image](https://github.com/user-attachments/assets/018f086c-5326-4b82-a962-6672d4dede43)


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
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Carrega a imagem fornecida
imagem = cv2.imread("familia.jpg", cv2.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
else:
    # Função para adicionar ruído sal e pimenta
    def ruido_sal_pimenta(imagem, proporcao_sal=0.02, proporcao_pimenta=0.02):
        imagem_ruidosa = np.copy(imagem)
        num_sal = int(proporcao_sal * imagem.size)
        num_pimenta = int(proporcao_pimenta * imagem.size)

        # Aplica o ruído sal
        coords_sal = [np.random.randint(0, i - 1, num_sal) for i in imagem.shape]
        imagem_ruidosa[coords_sal[0], coords_sal[1]] = 255

        # Aplica o ruído pimenta
        coords_pimenta = [np.random.randint(0, i - 1, num_pimenta) for i in imagem.shape]
        imagem_ruidosa[coords_pimenta[0], coords_pimenta[1]] = 0

        return imagem_ruidosa

    # Função para adicionar ruído Gaussiano
    def ruido_gaussiano(imagem, sigma=25):
        ruido = np.random.normal(0, sigma, imagem.shape).astype(np.float32)
        imagem_ruidosa = imagem.astype(np.float32) + ruido
        imagem_ruidosa = np.clip(imagem_ruidosa, 0, 255).astype(np.uint8)
        return imagem_ruidosa

    imagem_modificada = imagem
    resposta = ''
    efeitos = ''
    certo = False

    # Aplica o ruído sal e pimenta
    while certo == False:
        resposta = input('\nAplicar Sal e Pimenta? [S] ou [N] = ')
        if resposta == 'S':
            imagem_modificada = ruido_sal_pimenta(imagem)
            efeitos = efeitos + ' Sal e Pimenta '
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica o ruído Gaussiano
    while certo == False:
        resposta = input('\nAplicar ruído Gaussiano? [S] ou [N] = ')
        if resposta == 'S':
            imagem_modificada = ruido_gaussiano(imagem_modificada)
            efeitos = efeitos + ' Ruído Gaussiano ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica o filtro de média
    while certo == False:
        resposta = input('\nAplicar filtro de Média? [S] ou [N] = ')
        if resposta == 'S':
            imagem_modificada = cv2.blur(imagem_modificada, (5, 5))
            efeitos = efeitos + ' Média ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica o filtro de mediana
    while certo == False:
        resposta = input('\nAplicar filtro Mediana? [S] ou [N] = ')
        if resposta == 'S':
            imagem_modificada = cv2.medianBlur(imagem_modificada, 5)
            efeitos = efeitos + ' Mediana ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica o filtro Gaussiano
    while certo == False:
        resposta = input('\nAplicar filtro Gaussiano? [S] ou [N] = ')
        if resposta == 'S':
            imagem_modificada = cv2.GaussianBlur(imagem_modificada, (5, 5), 1)
            efeitos = efeitos + ' Filtro Gaussiano ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica o filtro de Sobel
    while certo == False:
        resposta = input('\nAplicar filtro Sobel? [S] ou [N] = ')
        if resposta == 'S':
            sobel_x = cv2.Sobel(imagem_modificada, cv2.CV_64F, 1, 0, ksize=5)
            sobel_y = cv2.Sobel(imagem_modificada, cv2.CV_64F, 0, 1, ksize=5)
            imagem_modificada = cv2.magnitude(sobel_x, sobel_y).astype(np.uint8)
            efeitos = efeitos + ' Sobel ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica a Transformada de Fourier
    while certo == False:
        resposta = input('\nAplicar transformação de Fourier? [S] ou [N] = ')
        if resposta == 'S':
            f_transformada = np.fft.fft2(imagem_modificada)
            f_transformada_centralizada = np.fft.fftshift(f_transformada)
            imagem_modificada = np.log(1 + np.abs(f_transformada_centralizada))
            efeitos = efeitos + ' Fourier ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    certo = False
    # Aplica a Transformada Wavelet
    while certo == False:
        resposta = input('\nAplicar Transformaçãod de Wavelet? [S] ou [N] = ')
        if resposta == 'S':
            coeffs2 = pywt.dwt2(imagem_modificada, 'haar')
            LL, (LH, HL, HH) = coeffs2
            imagem_modificada = np.log(np.abs(LL) + 1)
            efeitos = efeitos + ' Wavelets ' 
            certo = True
        elif resposta == 'N':
            certo = True
        else:
            print('Resposta Inválida')

    plt.figure(figsize=(12, 6))

    # Imagem original
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title("Imagem Original")
    plt.axis('off')

    # Imagem com todos os efeitos aplicados
    plt.subplot(1, 2, 2)
    plt.imshow(imagem_modificada, cmap='gray')
    plt.title(f"Imagem com {efeitos}")
    plt.axis('off')

    plt.show()

    


    ![image](https://github.com/user-attachments/assets/96b9232d-c6fb-463e-a9f4-143cfe4528d6)

