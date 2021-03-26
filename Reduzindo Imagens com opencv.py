#Carregando imagem de teste

import matplotlib.pyplot as plt
import cv2

url = "/content/coliseu2.png"
image = cv2.imread(url)
#convertendo de BGR para RGB
image = cv2.cvtColor(image,cv2.color_BGR2RGB)

fig, ax = plt.subplots(nrows=1, figsize=(16, 10))
ax.imshow(image)
ax.set_title("Imagem Original: "+str(image.shape))

fig, [ax1,ax2] = plt.subplots(nrows=2, ncols=1, figsize=(16, 10))
ax1.imshow(image)
ax1.set_title("Imagem Original: "+str(image.shape))

image2 = cv2.resize(image, (240,240))
ax2.imshow(image2)
ax2.set_title("Imagem com 240 x 240")

#Definindo a largura em 240 a naova altura deve ser a altura antiga x a proporção

proporcao = 240.0 / image.shape[1]
nova_altura = int(image.shape[0] * r)
dim = (240, nova_altura)

#resize da Imagem
image3 = cv2.resize(image, dim)
ax3.imshow(image3)
ax3.set_title("Imagem com aspecto ratio: "+str(image3.shape))

fig, ax3 = plt.subplot(nrows=1, ncols=1, figsize=(16,10))
image3 = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
ax3.imshow(image3)
ax3.set_title("Imagem com aspect ratio e interpolação: "+ str(image3.shape))
