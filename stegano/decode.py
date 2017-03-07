# coding: utf8
# chargement des fonctionalité d'image ainsi que de low et high
from stegano import *

# charge le fichier
#size, image = image_load('exercices/message_x.png')
size, image = image_load('exercices/message_x_cool.png')
#size, image = image_load('resultat_encode.png')

# crée une nouvelle image de résultat
result = image_new(size)

# ici votre code de decodage
for i in range(len(image)):
	#message x
	#result[i] = low(image[i],4)*16
	#message x cool
	result[i] = high(image[i],2)|low(image[i],4)*4
	#decode encode
	#result[i] = low(image[i],4)*16

# sauvegarde l'image
#image_save(result, size, 'resultat.png')
image_save(result, size, 'resultat_cool.png')
#image_save(result, size, 'resultat_decode.png')
