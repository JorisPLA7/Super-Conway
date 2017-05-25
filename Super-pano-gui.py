##PROGRAMME SOUS LICENSE G.P.L ........ Joris Placette ........ 2017

global appVersion #Variable contenant le numero de version du porgramme (écrit avec les données)

global palette

global posxmax

comValue =0
posxmax = 200
appVersion = "0.3.6 : Serializeu (commenté)"
helpPage = "https://github.com/Kouskali/super-pano-editor/blob/master/README.md" #lien pages d'aide à consulter
githubPage = "https://github.com/Kouskali/super-pano-editor/"

cacheData = {
"angleinter":    0,
"angletotal":   0,
"posx":   0,
"versys":   appVersion,
}# cachedata , données fournies par l'utilisateur, en attente d'être envoyées à la carte ou enregistrées
##boutons
def rbfcbutton():  #fonction appelée pour ouvrir un fichier existant
   global cacheData
   datatampon = cacheData
   cacheData = datasheets.pickread()
   if cacheData["versys"] == "fail!": ##
      print("Erreur: Fichier ouvert mais lu sans succès")
   print("nouvelles données en ram: {}".format(cacheData))

def wbfcbutton(): #fonction appelée pour écrire les valeurs dans un fichier
   datasheets.pickwrite(cacheData) # se référer à datasheets.py

def verifbutton(): #vérification des données fournies par l'utilisateur
   nberror = 0
   if int(saisieangleinter.get()) < 0 or int(saisieangleinter.get()) > 50:
      guimessage("red", "Il y a un problème :'(  !", "l'angle entre 2 positions doit être compris entre 0 et 50° !")
      nberror +=1
   if int(saisieangletotal.get()) < 0 or int(saisieangletotal.get()) > 720 :
      guimessage("red", "Il y a un problème :'(  !", "l'angle total doit être compris entre 0 et 720° !")
      nberror +=1

   if int(saisieposx.get()) < 0 or int(saisieposx.get()) > posxmax:
      guimessage("red", "Il y a un problème :'(  !", "La position linéaire doit être comprise entre 0 et {} !".format(posxmax))
      nberror +=1

   if nberror == 0: #si tout est valide
      pulldata()
      refreshcanvas(cacheData)
      guivalidation()
      print("Les informations saisies ne contiennes visiblement pas d' erreures")

def serialsetbbutton():
   serializer.establish(comValue, cacheData)
def serialsendbutton():
   serialzer.send(cacheData)

#réccupération des données de l'utilisateur
def pulldata():
   cacheData["angletotal"] = saisieangletotal.get()
   cacheData["angleinter"] = saisieangleinter.get()
   cacheData["posx"] = saisieposx.get()

def donothing(): #ne fait rien, comme son nom l'indique
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
   print("Fenêtre qui ne fait rien ouverte")


def forcesave():
   print("tentative de sauvegarde forcée")
   pulldata()
   wbfcbutton()

#gui refreshers
def guimessage(color, context, reason):
   messageframe = LabelFrame(root, text=context, fg=color )
   messageframe.pack(fill="both", expand="no", side=BOTTOM)

   destroybutton= Button(messageframe, text="x", command=messageframe.destroy)
   destroybutton.pack(side=LEFT)

   left = Label(messageframe, text=reason, fg=color)
   left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

   root.mainloop()

#
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
    from lib import graphiti
    print("bibliothèque importée avec succès :  lib\graphiti")
except:
    print("Impossible d'importer la bibliothèque :  lib\graphiti")
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
try:
    from lib import serializer
    print("bibliothèque importée avec succès :  lib\serializer")
except:
    print("Impossible d'importer la bibliothèque :  lib\ser")
root=Tk() #création de la fenêtre tkinter racine

root.wm_title('Super Pano GUI')#definition du titre
root.wm_iconbitmap('ressources\supano.ico')#definition de l'icone



##Barre de Menu suppérieur
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0) #sous menu

filemenu.add_command(label="Ouvrir une sauvegarde", command=rbfcbutton)
filemenu.add_command(label="Sauvegarder sans validation", command=forcesave)
filemenu.add_separator()

serialmenu = Menu(filemenu) #sous² menu
for i in range (0,10):
   serialmenu.add_radiobutton(label="Ouvrir une lisaison série COM{}".format(i), variable=comValue, value=i, command=serializer.establish)
filemenu.add_cascade(label="Etablir une liaison série", menu=serialmenu)
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
header = Label(root, text="Outil de configuration du trépied. Version {}".format(appVersion))
header.pack(fill="both", expand="no")

##Panneau lateral
aside = Frame(root)
aside.pack(side=LEFT)

##init canvas
w = Canvas(aside, width=200, height=300)
w.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

def refreshcanvas(cacheData):
   w.delete("all")
   rectangle = w.create_rectangle(10, 30, 190, 40, fill="white")

   posxdisp = int(int(cacheData["posx"]) / posxmax * 180 +10)

   w.create_line(posxdisp, 25, posxdisp, 45) # curseur représentant la posx sur une échelle de  à posxmax
   angletotrest = cacheData["angletotal"]
   angleinterrest = cacheData["angleinter"]

   coord1 = 2, 50, 200, 250 ##xcoinsupp, ycoinsupp, xcoininf, ycoininf
   coord2 = 2, 50, 190, 250 ##xcoinsupp, ycoinsupp, xcoininf, ycoininf
   arctot = w.create_arc(coord1, start=10, extent=cacheData["angletotal"], fill="white") #arc de cercle dont l'angle d'extension est proportionnel à : angle renseigné [360]
   arcinter = w.create_arc(coord2, start=20, extent=cacheData["angleinter"], fill="black")

   print("canvas actualisé avec succès :  !")

##panneau  translation
translatif = LabelFrame(root, text="Module translatif")
translatif.pack(fill="both", expand="yes", side=TOP)

left = Label(translatif, text="Position linéaire :")
left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

saisieposx = Spinbox(translatif, from_=0, to=100,)
saisieposx.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

##panneau  rotat°
rotatif = LabelFrame(root, text="Module rotatif")
rotatif.pack(fill="both", expand="yes", side=TOP)

   ## pann subrotat1
subrotatif1 = Frame(rotatif)
subrotatif1.pack(fill="both", expand="yes", side=TOP)

titreangleinter = Label(subrotatif1, text="angle entre deux positions (degrés) :")
titreangleinter.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

saisieangleinter = Spinbox(subrotatif1, from_=0, to=50)
saisieangleinter.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
#cacheData["angleinter"] = saisieangleinter.get()

   ## pann subrotat2
subrotatif2 = Frame(rotatif)
subrotatif2.pack(fill="both", expand="yes", side=TOP)

titreangletotal = Label(subrotatif2, text="angle total du mouvement (degrés) :")
titreangletotal.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

saisieangletotal = Spinbox(subrotatif2, from_=0, to=50)
saisieangletotal.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

checkbutton= Button(root, text="Verifier", command=verifbutton)
checkbutton.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

root.mainloop()
