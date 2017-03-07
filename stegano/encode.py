# coding: utf8
from stegano import *

# charge le fichier à cacher
size, message = image_load('message.jpg')

# charge le fichier servant à cacher
size2, mask = image_load('mask.jpg')

# verifie que les deux ont la même taille
assert size == size2

# crée une nouvelle image de résultat
result = image_new(size)

# ici votre code d'encodage
for i in range(len(mask)):
	result[i] = high(mask[i],4)|high(message[i],4)>>4

# sauvegarde l'image
image_save(result, size, 'resultat_encode.png')
