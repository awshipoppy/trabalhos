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
podendo escolher combinações diferentes baseadas nos ruídos, filtros e transformações existentes no código, onde ele teria apenas que mudar uma linha do código, que é o nome da imagem que está selecionado.

### Exemplos
![image](https://github.com/user-attachments/assets/7c89928c-c669-4774-8b6d-3c4452c0ab5b)
Nesta imagem, esta aplicado o ruido de Sal e Pimenta junto com o Filtro Mediana, selecionado pelo usuário

![image](https://github.com/user-attachments/assets/f49f6f04-5771-4826-99b0-6d5552c70f17)
Nesta imagens, diversos efeitos estão sendo aplicados, fazendo com que pareça ainda mais antigo do realmente é, como se tivesse borrada

![image](https://github.com/user-attachments/assets/3b756d57-0044-4885-a706-6f732d124858)
Outro exemplo com vários efeitos selecionados a mão, dando um aspecto bizarro a foto

# Melhorando a imagem
Pelos os meus testes, a melhor imagem vai sempre ser a original! Onde colocando os efeitos, quaisquer que seja, detalhes de rostos ou da paisagem de trás vão se perdendo entre elas, mas acredito que uma boa combinação seja = Sal e Pimeta Mediana e Wavelets
![image](https://github.com/user-attachments/assets/dd370595-f747-4cb8-bec6-48efb4a502b6)
Onde não estraga a imagem e ainda fica visível os detalhes, mesmo que um pouco fosco

# Melhor Transformação
Acredito que a de Wavelets tenha mais funções para usos de imagens em geral do que a de Fourier, já que a mesma é centrada em criar algo no centro, onde para mim não vejo muitas utilidades nisso
![image](https://github.com/user-attachments/assets/2cac39ae-59a7-4553-90ef-4d73107f2ff3)

![image](https://github.com/user-attachments/assets/0a43da3d-c2b9-4889-a735-dd443b07accf)
