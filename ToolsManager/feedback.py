from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from datetime import datetime
import MenuPrincipal


class fb:
    def __init__(self):
        root=Tk()
        root.focus_force()
        root.title("Feedback")
        root.geometry("1080x720+400+200")
        root.resizable(False, False)

        mainframe=ttk.Frame(root, padding="3 3 12 12")

        mainframe.grid(row=0, column=0, sticky=(N,S,E,W))

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        t=datetime.now()


        ################################Fonction #############################"
        def launch_MP(event=0):
            root.destroy()
            MenuPrincipal.MP()

        #affiche dans un fichier users.txt qui sera créé les informations de l'utilisateur
        def envoyer(event=0):
            with open('users.txt', 'a') as users:
                if entr_nom.get()=='':
                    users.write("Nom: Anonyme"+'\n')
                else:
                    users.write("Nom: "+entr_nom.get()+'\n')
                entr_nom.delete(0,END)
             
                users.write("Optimisation: "+note_optim.get()+'\n')
                note_optim.delete(0,"end")
                note_optim.insert(0,0)
                users.write("Contenu: "+note_contenu.get()+'\n')
                note_contenu.delete(0,"end")
                note_contenu.insert(0,0)
                if len(text.get("1.0",END))==1:
                    users.write("Commentaire: Aucun"+'\n')
                else:
                    users.write("Commentaire: "+text.get("1.0",END))
                text.delete(1.0,END)
                users.write('Connecté à {}'.format(t)+'\n'+'\n')

                mb.showinfo("Enquête de satisfaction", "Merci d'avoir laissé un commentaire")

                users.close()

                root.destroy()
                MenuPrincipal.MP()
                


        ##################################################
                
        first=Label(mainframe, text="Remplis ce qui te convient pour nous aider à progresser", font='Arial 16')
        first.grid(row=0, column=1, columnspan=3, pady=10,sticky='nsew')


        nom=Label(mainframe, text="Quel est ton nom ? :")
        nom.grid(row=2, column=0, pady=20)

        entr_nom= ttk.Entry(mainframe)    
        entr_nom.grid(column=1, row=2, columnspan=3, padx=10, sticky=(E,W),pady=20)



        optim=Label(mainframe, text="Trouvez-vous l'application bien optimisée (sur 10) ? ")
        optim.grid(row=3, column=0, columnspan=2, pady=10, sticky='nsew')

        note1= StringVar()

        note_optim=Spinbox(mainframe, from_=0, to=10 ,textvariable=note1, stat='readonly')
        note_optim.grid(row=3, column=3, pady=10)



        contenu=Label(mainframe, text="Trouvez-vous que les contenus des outils convenables (sur 10) ? ")
        contenu.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')


        note2= StringVar()

        note_contenu=Spinbox(mainframe, from_=0, to=10 ,textvariable=note2, stat='readonly')
        note_contenu.grid(row=4, column=3, pady=10)







        com=Label(mainframe, text="COMMENTAIRES :")
        com.grid(row=7, column=0, pady=20)

        #permet d'écrire un texte dans un champ qui fait un retour à la ligne pour un mot en fin de ligne

        text= Text(mainframe, width=50, height=3, wrap=WORD)#wrap=WORD: ne coupe pas le WORD en fin de file
        text.grid(row=7, column=1, padx=10, columnspan=2)



        send=ttk.Button(mainframe, text='Envoyer', command=envoyer)
        send.grid(row=8, column=2, pady=15)

        ttk.Button(mainframe, text= "Revenir au Menu Principal", command= launch_MP).grid(row=0, column=10)

        root.bind("<Return>", envoyer)
        root.bind("<Escape>", launch_MP)


        root.mainloop()
