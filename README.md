# Trabalhos
Trabalhos para o dia 13/11, aqui estão as atividades de transformação de wavelets e ruido de sal e pimenta e o trabalho de arrumar uma imagem

## Atividade da Transformação de wavelets
A atividade de transformação de wavelets, ela foi usando as aproximações e os detalhes mostrados em uma imagem de um jogo conhecido como Castlevania "Simphony of the Night", mostrando versões onde a imagem está sendo puxada e empurrada

### Exemplo:

![image](https://github.com/user-attachments/assets/018f086c-5326-4b82-a962-6672d4dede43)

Alguns usos melhores seriam usar em uma girafa, onde suas cores amarelas e pretas seriam saltadas.

#### Código
O código para ver a execução é 'Wavelets.py'

## Atividade de Ruidos 
Outra atividade que fizemos foi em relação aos ruidos que podem ser aplicados na imagem para depois serem tratados, uma estrátegia para entender algo melhor, estudamos dois ruídos sendo eles:

### Ruido de Sal e Pimenta
O ruido de Sal e Pimenta funciona de forma onde é posto alguns pontos brancos e pretos na imagem, deixando ela com um tom de rabiscado

### Ruido Gaussiano
O ruido gaussiano funciona de maneira pouco similar ao filtro gaussiano, porém neste um ruído branco é aplicado, deixando a imagem um pouco mais transparente

### Exemplo:

![image](https://github.com/user-attachments/assets/4f7d78d0-a8b1-4f49-a82b-7bd038747bd6)

As imagens após serem aplicadas com os ruidos e serem aplicadas os filtros para tentar melhorar a qualidade

#### Código
O código para ver a execução é 'sal_pimenta.py'

# Projeto para Prova
Pelo que foi proposto, era para nós usarmos tudo que aprendemos durante o semestre sobre filtros, ruídos e transformações para selecionar uma imagem e tentar melhorara o máximo possível

# O que aprendemos?
De maneira resumida, nós aprendemos os seguintes tópicos

### Ruído Sal e Pimenta
Um tipo de ruído onde pixels aleatórios são definidos para valores máximos (sal, ou branco) ou mínimos (pimenta, ou preto). Ele cria pontos brancos e pretos dispersos pela imagem e é frequentemente causado por falhas na captura ou transmissão de dados.
### Ruído Gaussiano
Um ruído que segue uma distribuição normal (gaussiana) e afeta o valor de intensidade dos pixels de maneira aleatória. É frequentemente usado para simular variações aleatórias em sensores e dispositivos de captura.
### Filtro Gaussiano
É um filtro de suavização que usa uma função gaussiana para suavizar ou desfocar uma imagem. O filtro gaussiano aplica uma "média ponderada" nos pixels próximos, dando mais peso aos pixels mais próximos do ponto central. É muito útil para reduzir ruídos, especialmente o ruído gaussiano.
### Filtro de Média
Este filtro calcula a média dos valores de intensidade dos pixels vizinhos e substitui o valor do pixel central por essa média. É um método simples de suavização, porém pode desfocar detalhes importantes da imagem.
### Filtro de Mediana
Este filtro substitui o valor de um pixel pelo valor mediano dos pixels em sua vizinhança. É eficaz para remover ruído "sal e pimenta", pois preserva bordas e evita a criação de novos valores extremos.
### Filtro Sobel
Um filtro de detecção de bordas que calcula gradientes de intensidade em uma imagem, destacando áreas onde há grandes mudanças, como bordas. Ele usa máscaras horizontais e verticais para identificar essas transições.
### Transformada de Fourier
Uma técnica matemática que decompõe uma imagem (ou sinal) em suas frequências constituintes. No contexto de imagens, ajuda a identificar padrões e remover ruídos de alta frequência (ruído granular) ou destacar frequências específicas.
### Transformada Wavelet
Uma técnica de decomposição que representa uma imagem ou sinal em diferentes escalas, capturando tanto informações de frequência quanto de localização. É útil para compressão e remoção de ruído em imagens e sinais, pois permite focar em detalhes específicos.

# O que eu fiz?
Baseado em todos esses elementos, ao invés de fazer um código unico para melhorar apenas uma imagem, eu fiz com que o próprio usuário adicionasse os efeitos que gostaria a sua imagem para a visualização no final,
podendo escolher combinações diferentes baseadas nos ruídos, filtros e transformações existentes no código, onde ele teria apenas que mudar uma linha do código, que é o nome da imagem que está selecionado

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

