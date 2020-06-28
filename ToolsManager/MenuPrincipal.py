from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import Comptmots, feedback, Jeu, Conversion, Moyenne

class MP:
    def __init__(self):
        def Launch(name):
            #S'il n'y a rien, utilisateur a appuyé sans avoir selectionné de programme a lancer
            if(len(name)==0): 
                return

            root.destroy()
            #éxécute une fenêtre choisie dans la combobox
            if (name=="Multi-Compteur"):
                Comptmots.Comptmot()

            if (name=="Mini-jeu"):
                Jeu.jeu()

            if (name=="Feedback"):
                feedback.fb()

            if (name=="Calcul de la moyenne"):
                Moyenne.Moyenne()

            if (name=="Convertisseur d'unité"):
                Conversion.conversion()

            


        root = Tk()
        root.focus_force()
        root.title("Menu Principal ")
        root.geometry("1080x720+400+200")
        root.resizable(False, False)
        ##############FRAMES#####################
        mainframe=ttk.Frame(root, padding="3 3 12 12")

        mainframe.pack(expand=True)

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
##########################################
        

        outils=Label(mainframe, text="OUTILS :")
        outils.grid(row=0, column=0)

        ordre=StringVar()
        apps=ttk.Combobox(mainframe, textvariable= ordre,
                        values=('Calcul de la moyenne', 'Convertisseur d\'unité',
                                'Multi-Compteur','Mini-jeu'),
                        stat='readonly')
        apps.grid(row=0, column=1, columnspan=2, sticky=(W, E))


        com=ttk.Button(mainframe, text="FeedBack", command=lambda : Launch("Feedback"))
        com.grid(row=0, column=5, sticky='nsew')

####################Labels#####################
        msg1=Label(mainframe, text="BIENVENUE SUR TOOLS MANAGER")
        msg1.grid(row=3, column=2, sticky='nsew', pady=10)


        msg2=Label(mainframe, text="Cliquez dans la fenêtre outils pour utiliser l'outil de votre choix")
        msg2.grid(row=4, column=1, columnspan=3, sticky='nsew')

        msg3=Label(mainframe, text="Laissez-nous un commentaire en cliquant sur le bouton Feedback")
        msg3.grid(row=6, column=1, columnspan=3, pady=10, sticky='nsew')
################################################
        root.bind("<Escape>", lambda x : root.destroy())
        root.bind("<Return>", lambda x : Launch(ordre.get()))
        root.mainloop()
