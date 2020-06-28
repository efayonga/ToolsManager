from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog
import MenuPrincipal



class Comptmot:
    def __init__(self):
        
        root=Tk()
        root.focus_force()
        root.title("Compteur de mots")
        root.geometry("1080x720+400+200")
        root.resizable(False, False)

        #########################FONCTIONS########

        ## Cette fonction sert à fermer cette fenêtre pour revenir au menu principal de notre logiciel. On la retrouve dans tous les programmes

        def launch_MP(event=0):
            root.destroy()
            MenuPrincipal.MP()
            return
            


            
        def compte_mots(self=0):
            # file_path nous permet de trouver le chemin du fichier et renvoie un message d'erreur si il n'y a aucun fichier
            try:
                file_path
            except:
                mb.showwarning("Attention! ", "Il faut d'abord entrer un fichier, appuyez sur le bouton du dessus !")
                return

            # renvoi une erreur si le fichier est vide 
            if(len(file_path)==0):
                mb.showwarning("Attention! ", "Il faut d'abord entrer un fichier, appuyez sur le bouton du dessus !")
                return #Si l'utilisateur annule l'entrée de fichier

            #ouvre le fichier et décompose selon la commande choisie
            with open(file_path, 'r') as file:
                if compteur.get()=='caractères':
                    file= file.read()
                    nb_char= len(file)
                    show_count.config(text='Il y a {} caractères dans le fichier {} !'.format(nb_char, selected_file))
                
                if compteur.get()=='mots':
                    file= file.read().split(" ")
                    nb_mots= len(file)
                    show_count.config(text='Il y a {} mots dans le fichier {} !'.format(nb_mots, selected_file))

                if compteur.get()=='phrases':
                    file= file.read().split(".")
                    nb_phrases= len(file)
                    show_count.config(text='Il y a {} phrases dans le fichier {} !'.format(nb_phrases, selected_file))
         # cette fonction permet de récupérer le chemin du fichier choisi 
        def inserer(event=0):
            global file_path, selected_file
            file_path= filedialog.askopenfilename()
            
            if(len(file_path) != 0): #Pour extraire le nom du fichier choisi
                for i in range(len(file_path)):
                    if(file_path[-i]=="/"):
                        selected_file= file_path[-i+1:-1]+file_path[-1]
                        show_selected.config(text='Vous avez selectionné le fichier \"'+selected_file+'\"')
                        return

            else:
                return
        #############################################

            
        ################FRAMES#################

        mainframe=ttk.Frame(root)
        mainframe.pack(expand=True)

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        ###########################################




        ################INTERFACE#######################
        label=Label(mainframe, text="Insérer un fichier texte :")
        label.grid(row=2, column=0, sticky='nsew')

        show_selected= Label(mainframe, text='')
        show_selected.grid(row=3, column= 0, sticky=NSEW)

        show_count= Label(mainframe, text='')
        show_count.grid(row=4, sticky=NSEW)

        compter=Label(mainframe, text='Compter les')
        compter.grid(row=0, column=0, sticky='nsew')

        compteur=ttk.Combobox(mainframe, values=('caractères', 'mots', 'phrases'), stat='readonly')
        compteur.grid(row=0, column=1, sticky='nsew')

        ttk.Button(mainframe, text='Insérer', command=inserer
                   ).grid(column=1, row=2, columnspan=3, pady=10)



        ttk.Button(mainframe, text='Compter', command= compte_mots
                   ).grid(column=0, row=5, columnspan=2, pady=10)

        ttk.Button(mainframe, text='Revenir au Menu Principal', command= launch_MP
                   ).grid(row=0, column= 5, padx= 19)


        ps=Label(mainframe, text="PS: Les fichiers .docx ne sont pas compatibles")
        ps.grid(row=7, column=0, columnspan= 2, sticky='nsew', pady=10)
        ###############################################

        root.bind("<Return>", compte_mots)
        root.bind("<Escape>", launch_MP)

