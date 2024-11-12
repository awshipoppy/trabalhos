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

    
