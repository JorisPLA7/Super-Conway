##PROGRAMME SOUS LICENSE G.P.L (see README.md) ........ Joris Placette ........ 2017


'''à changer'''
def rbfcbutton():  #fonction appelée pour ouvrir un fichier existant
   global cacheData
   cacheData = datasheets.pickread()
   global MyDraw
   MyDraw = listes.Draw(cacheData['xLen'],cacheData['yLen'],cacheData['p'])
   MyDraw.applyDraw(cacheData['draw'])
   checkbutton.pack()

   print("nouvelles données en ram: {}".format(cacheData))

'''à changer'''
def wbfcbutton(): #fonction appelée pour écrire les valeurs dans un fichier
   datasheets.pickwrite(cacheData) # se référer à datasheets.py

def createNewDraw():
    pulldata()
    global MyDraw
    MyDraw = listes.Draw(cacheData['xLen'],cacheData['yLen'],cacheData['p'])
    refreshcanvas()
    checkbutton.pack()


def startbutton():
    nberror = 0
    if nberror == 0: #si tout est valide
        pulldata()

        sTime = time.time()
        MyDraw.increment(cacheData["increment"])
        fTime = time.time()
        passedTime = fTime - sTime

        chrono = Label(bench, text="Temps écoulé : {}".format(passedTime))
        chrono.pack()

        refreshcanvas()


'''à changer'''
#réccupération des données de l'utilisateur
def pulldata():
    #récupération des données
   cacheData["increment"] = int(increment.get())
   cacheData["p"] = int(p.get())
   cacheData["xLen"] = int(xLen.get())
   cacheData["yLen"] = int(yLen.get())

def refreshcanvas():
   w.delete("all")


   cacheData["draw"] = MyDraw.getCurrentDraw()

   for x in range(0,len(cacheData['draw'])):
       for y in range(0,len(cacheData['draw'][x])):#abcd
           #print('x = {} y = {}  b = {}'.format(x,y,cacheData['draw'][x][y]))
           a = (x/MyDraw.xLen*600, y/MyDraw.yLen*600)
           b = ((a[0]+ 600/MyDraw.xLen), a[1]+600/MyDraw.yLen)
           #if cacheData['draw'][x][y] == 0 : w.create_rectangle(a[0], a[1], b[0], b[1], fill="white")
           if cacheData['draw'][x][y] == 1 : w.create_rectangle(a[0], a[1], b[0], b[1], fill="green", outline="")


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

## init tkinter
#importation des bibliotheques pyhton
try:
    from tests import listes
    print("bibliothèque importée avec succès :  listes")
except:
    print("Impossible d'importer la bibliothèque :  listes")

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

try:
    import time
    print("bibliothèque importée avec succès :  time")
except:
    print("Impossible d'importer la bibliothèque :  time")


global appVersion #Variable contenant le numero de version du porgramme (écrit avec les données)

global palette

global posxmax

global thereIsADraw

global passedTime
passedTime = 800
#MyDraw = listes.Draw(200,200,0.3)

appVersion = "1"
helpPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/README.md" #lien pages d'aide à consulter
githubPage = "https://github.com/JorisPLA7/Super-Conway/blob/master/"

cacheData = {}


root=Tk() #création de la fenêtre tkinter racine

root.wm_title('Super Conway')#definition du titre
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
header = Label(root, text="Super-Conway version {}".format(appVersion))
header.pack(fill="both", expand="no")

##Panneau lateral
aside = Frame(root)
aside.pack(side=LEFT)

##init canvas
w = Canvas(aside, width=600, height=600, background='white')
w.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)


##panneau  init
starter = LabelFrame(root, text="Configuration : initiale")
starter.pack(fill="both", expand="yes", side=TOP)

left = Label(starter, text="probabilité de présence de vie sur une case (%)")
left.pack()
p = Scale(starter,from_=1, to=100,)
p.pack()

left2 = Label(starter, text="Taille de la grille (x,y)")
left2.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

xLen = Spinbox(starter, from_=20, to=1000,)
xLen.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)
yLen = Spinbox(starter, from_=20, to=1000,)
yLen.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

creatbutton= Button(starter, text="CREER", command=createNewDraw)
creatbutton.pack()

#increment
aside = LabelFrame(root, text="Configuration : tache de fond")
aside.pack(fill="both", expand="yes", side=TOP)

left = Label(aside, text="increment :")
left.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

increment = Spinbox(aside, from_=1, to=1000,)
increment.pack() #on intègre le module déclaré à sa fenêtre (pack(sans paramètre) donc simplement à la suite du reste)

#bench
bench = LabelFrame(root, text="Benchmark")
bench.pack(fill="both", expand="yes", side=TOP)



checkbutton= Button(root, text="GO", command=startbutton)
#checkbutton.pack() #on le pack quand draw est init

root.mainloop()
