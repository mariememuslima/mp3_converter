import os
from moviepy.editor import *

monRepertoire="/home/marieme/Vidéos/Diine/Cours fiqh - Rachid Eljay/6  LES CONDITIONS DE L'ABLUTION..mp4"

try:
	import moviepy.editor
	if moviepy.editor:
		pass
	else:
		os.system("pip install moviepy")
except:
	print("veuillez installer manuellement pytube avec  la commande 'pip install moviepy' dans votre  terminal")

try:
	from moviepy.editor import *
except:
	print("Vous n'avez pas intallez le module pytube, faites 'pip install moviepy dans votre terminal'")


print("""
	1. Utiliser le chemin du fichier .mp4
	2. Utiliser le chemin du répertoire où se trouve mes fichiers .mp4
	NB: Verifiez si le chemin est correct
""")
choice = int(input('faites votre choix: '))


def fileMP4ToMP3(file):
    FILETOCONVERT = VideoFileClip(file)
    FILETOCONVERT.audio.write_audiofile(file[:-4]+".mp3")
    FILETOCONVERT.close()
    
def directorieMP4ToMP3(directory):
    files=os.listdir(directory)
    os.mkdir(directory+"/converted_files")
    print()
    for file in files:
        if str(file[-4:])==".mp4":
            FILETOCONVERT = VideoFileClip(directory+"/"+file)
            FILETOCONVERT.audio.write_audiofile(directory+"/converted_files"+"/"+file[:-4]+".mp3")
            FILETOCONVERT.close()

if choice == 1:
    file =  input('veuillez coller ici le chemin de la video: ' )
    try :
        fileMP4ToMP3(file)
        print("Fichier converti disponible à l'emplacement : "+file[:-4]+".mp3")
    except:
        print("Le fichier n'a pas pu être téléchargé")
elif choice == 2:
    directory =  input('veuillez coller ici le chemin du repertoire: ')
    try :
        directorieMP4ToMP3(directory)
        print("Les fichiers sont disponibles au répertoire"+directory)
    except:
        print("Les fichiers n'ont pas pu être téléchargés")

print('Fin' )



print("<Marieme_Muslima_Code/>")


# MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
# MoviePy - Writing audio in /Full/File/Path/ToSong.mp3