# Trabalhos
Trabalhos para o dia 13/11, aqui estão as atividades de transformação de wavelets e ruido de sal e pimenta e o trabalho de arrumar uma imagem

## Atividade da Transformação de wavelets
A atividade de transformação de wavelets, ela foi usando as aproximações e os detalhes mostrados em uma imagem de um jogo conhecido como Castlevania "Simphony of the Night", mostrando versões onde a imagem está sendo puxada e empurrada

### Exemplo:

![image](https://github.com/user-attachments/assets/018f086c-5326-4b82-a962-6672d4dede43)

Alguns usos melhores seriam usar em uma girafa, onde suas cores amarelas e pretas seriam saltadas.

#### Código
O código para ver a execução é 'sal_pimenta.py'

## Atividade de Ruidos 
Outra atividade que fizemos foi em relação aos ruidos que podem ser aplicados na imagem para depois serem tratados, uma estrátegia para entender algo melhor, estudamos dois ruídos sendo eles:

### Ruido de Sal e Pimenta
O ruido de Sal e Pimenta funciona de forma onde é posto alguns pontos brancos e pretos na imagem, deixando ela com um tom de rabiscado

### Ruido Gaussiano
O ruido gaussiano funciona de maneira pouco similar ao filtro gaussiano, porém neste um ruído branco é aplicado, deixando a imagem um pouco mais transparente

### Exemplo:

![image](https://github.com/user-attachments/assets/4f7d78d0-a8b1-4f49-a82b-7bd038747bd6)

As imagens após serem aplicadas com os ruidos e serem aplicadas os filtros para tentar melhorar a qualidade

# Projeto para Prova
Código feito para que o próprio usuário edite a imagem de acordo com os filtros que queira, ajustando as melhores opções para sua imagem

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Carrega a imagem fornecida
imagem = cv2.imread("familia.jpg", cv2.IMREAD_GRAYSCALE)

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
efeitos = ''

# Aplica o ruído sal e pimenta
resposta = input('\nAplicar Sal e Pimenta? [S] ou [N] = ')
if resposta == 'S':
    imagem_modificada = ruido_sal_pimenta(imagem)
    efeitos += ' Sal e Pimenta '

# Aplica o ruído Gaussiano
resposta = input('\nAplicar ruído Gaussiano? [S] ou [N] = ')
if resposta == 'S':
    imagem_modificada = ruido_gaussiano(imagem_modificada)
    efeitos += ' Ruído Gaussiano '

# Aplica o filtro de média
resposta = input('\nAplicar filtro de Média? [S] ou [N] = ')
if resposta == 'S':
    imagem_modificada = cv2.blur(imagem_modificada, (5, 5))
    efeitos += ' Média '

# Aplica o filtro de mediana
resposta = input('\nAplicar filtro Mediana? [S] ou [N] = ')
if resposta == 'S':
    imagem_modificada = cv2.medianBlur(imagem_modificada, 5)
    efeitos += ' Mediana '

# Aplica o filtro Gaussiano
resposta = input('\nAplicar filtro Gaussiano? [S] ou [N] = ')
if resposta == 'S':
    imagem_modificada = cv2.GaussianBlur(imagem_modificada, (5, 5), 1)
    efeitos += ' Filtro Gaussiano '

# Aplica o filtro de Sobel
resposta = input('\nAplicar filtro Sobel? [S] ou [N] = ')
if resposta == 'S':
    sobel_x = cv2.Sobel(imagem_modificada, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(imagem_modificada, cv2.CV_64F, 0, 1, ksize=5)
    imagem_modificada = cv2.magnitude(sobel_x, sobel_y).astype(np.uint8)
    efeitos += ' Sobel '

# Aplica a Transformada de Fourier
resposta = input('\nAplicar transformação de Fourier? [S] ou [N] = ')
if resposta == 'S':
    f_transformada = np.fft.fft2(imagem_modificada)
    f_transformada_centralizada = np.fft.fftshift(f_transformada)
    imagem_modificada = np.log(1 + np.abs(f_transformada_centralizada))
    efeitos += ' Fourier '

# Aplica a Transformada Wavelet
resposta = input('\nAplicar Transformação de Wavelet? [S] ou [N] = ')
if resposta == 'S':
    coeffs2 = pywt.dwt2(imagem_modificada, 'haar')
    LL, (LH, HL, HH) = coeffs2
    imagem_modificada = np.log(np.abs(LL) + 1)
    efeitos += ' Wavelets '

# Exibe as imagens lado a lado
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

