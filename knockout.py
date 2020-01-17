import os, pickle

with open('matchs_2', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    matchs = mon_depickler.load()

for i in matchs:
    print(i)

os.system("pause")