##PROGRAMME SOUS LICENSE G.P.L ........ Joris Placette ........ 2017

global appVersion #Variable contenant le numero de version du porgramme (écrit avec les données)

global palette

global posxmax

comValue =0
posxmax = 200
appVersion = "0.0.1"
helpPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/README.md" #lien pages d'aide à consulter
githubPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/"

cacheData = {
"angleinter":    0,
"angletotal":   0,
"posx":   0,
"versys":   appVersion,
}# cachedata , données fournies par l'utilisateur, en attente d'être envoyées à la carte ou enregistrées
##boutons

'''à changer'''
def rbfcbutton():  #fonction appelée pour ouvrir un fichier existant
   global cacheData
   datatampon = cacheData
   cacheData = datasheets.pickread()
   if cacheData["versys"] == "fail!": ##
      print("Erreur: Fichier ouvert mais lu sans succès")
   print("nouvelles données en ram: {}".format(cacheData))

'''à changer'''
def wbfcbutton(): #fonction appelée pour écrire les valeurs dans un fichier
   datasheets.pickwrite(cacheData) # se référer à datasheets.py

'''à changer'''
def verifbutton(): #vérification des données fournies par l'utilisateur
   nberror = 0
   if nberror == 0: #si tout est valide
      pulldata()
      refreshcanvas(cacheData)
      guivalidation()
      print("Les informations saisies ne contiennes visiblement pas d' erreures")

'''à changer'''
#réccupération des données de l'utilisateur
def pulldata():
    #récupération des données
   '''cacheData["angletotal"] = saisieangletotal.get()
   cacheData["angleinter"] = saisieangleinter.get()
   cacheData["posx"] = saisieposx.get()'''

'''à ne surtout pas changer <3'''
def donothing(): #ne fait rien, comme son nom l'indique
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
   print("Fenêtre qui ne fait rien ouverte")

'''à changer'''
def forcesave():
   print("tentative de sauvegarde forcée")
   pulldata()
   wbfcbutton()

'''à changer'''
#gui refreshers
def guimessage(color, context, reason):
   messageframe = LabelFrame(root, text=context, fg=color )
   messageframe.pack(fill="both", expand="no", side=BOTTOM)

   destroybutton= Button(messageframe, text="x", command=messageframe.destroy)
   destroybutton.pack(side=LEFT)

   left = Label(messageframe, text=reason, fg=color)
   left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

   root.mainloop()

'''à changer'''
def guivalidation():
   validationframe = LabelFrame(root, text="Tout semble correct :) ", fg="green" )
   validationframe.pack(fill="both", expand="no", side=BOTTOM)

   destroybutton= Button(validationframe, text="x", command=validationframe.destroy)
   destroybutton.pack(side=LEFT)

   savebutton= Button(validationframe, text="enregistrer", command=wbfcbutton, fg="green")
   savebutton.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

   desc= Label(validationframe, text="posx: {}  angle total: {}  angle intermidiaire: {}".format(cacheData["posx"],cacheData["angletotal"],cacheData["angleinter"]), fg="green")
   desc.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
   root.mainloop()


## init tkinter
#importation des bibliotheques pyhton
try: #schéma classique verbeux, afin que l'utilisateur sache quels fichiers sont manquants
    from tkinter import *
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    from tkinter.filedialog import *
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    from tkinter.messagebox import askokcancel, askyesno,askquestion
    print("bibliothèque importée avec succès :  tkinter")
except:
    print("Impossible d'importer la bibliothèque :  tkinter")
try:
    import pickle
    print("bibliothèque importée avec succès :  pickle")
except:
    print("Impossible d'importer la bibliothèque :  pickle")
try:
    from lib import web
    print("bibliothèque importée avec succès :  lib\web")
except:
    print("Impossible d'importer la bibliothèque :  lib\web")
try:
    from lib import datasheets
    print("bibliothèque importée avec succès :  lib\datasheets")
except:
    print("Impossible d'importer la bibliothèque :  lib\datasheets")

root=Tk() #création de la fenêtre tkinter racine

root.wm_title('Super Pano GUI')#definition du titre
root.wm_iconbitmap('ressources\supano.ico')#definition de l'icone



##Barre de Menu suppérieur
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0) #sous menu

filemenu.add_command(label="Ouvrir une sauvegarde", command=rbfcbutton)
filemenu.add_command(label="Sauvegarder sans validation", command=forcesave)
filemenu.add_separator()

filemenu.add_command(label="Quitter", command=root.destroy)
menubar.add_cascade(label="Fichier", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0) #sous menu
helpmenu.add_command(label="Version de l'application : {}".format(appVersion), command=web.help)
helpmenu.add_command(label="Ouvrir une aide sur le web", command=web.help)
menubar.add_cascade(label="Aide", menu=helpmenu)

devmenu = Menu(menubar, tearoff=0) #sous menu
menubar.add_cascade(label="Developpement", menu=devmenu)

root.config(menu=menubar)

##Titre
header = Label(root, text="Super-Conway. Version {}".format(appVersion))
header.pack(fill="both", expand="no")

##Panneau lateral
aside = Frame(root)
aside.pack(side=LEFT)

##init canvas
w = Canvas(aside, width=600, height=600)
w.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

'''à changer'''
def refreshcanvas(cacheData):
   w.delete("all")
   rectangle = w.create_rectangle(10, 30, 190, 40, fill="white")

   print("canvas actualisé avec succès !")

##panneau  translation
aside = LabelFrame(root, text="Coucou ,  je suis aside LabelFrame !")
aside.pack(fill="both", expand="yes", side=TOP)

left = Label(aside, text="Position linéaire :")
left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

saisieposx = Spinbox(aside, from_=0, to=100,)
saisieposx.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

##panneau  rotat°

checkbutton= Button(root, text="Verifier", command=verifbutton)
checkbutton.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

root.mainloop()
