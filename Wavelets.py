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