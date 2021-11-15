from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im = image.binarisation(S)
    im = im.localisation()
    liste_similitude = []
    for i in range (len(liste_modeles)) :
        im = im.resize(liste_modeles[i].H, liste_modeles[i].W)
        reco = im.similitude(liste_modeles[i])
        liste_similitude.append(reco)
        
    maxListe= 0
    max_simil = liste_similitude[0]
    for j in range (1,len(liste_similitude)):
        if liste_similitude[j] > max_simil :
            maxListe= j
            max_simil = liste_similitude[j]
            
    return maxListe
