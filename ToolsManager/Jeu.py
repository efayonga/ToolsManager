from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from random import *
import MenuPrincipal


class jeu:
    """
        Lorsqu'un objet de cette classe est instancié, la fenêtre de jeu s'affiche.
    """
    def __init__(self):
        ##############FENETRE#################
        win= Tk()
        win.focus_force()
        win.geometry("800x480+700+100")
        win.title("Le jeu du Pendu")
        win.resizable(False, False)
        ######################################

        #nb_chance initial
        nb_chance=7


        global pays, find, labels, histo, ent_inp
        pays= ''
        find= ''
        labels= ''
        histo= [] #Contiendra l'historique des lettres tapées
         
        ##############FONCTIONS################
        def launch_MP(event=0):
            """
                Lance le menu principal
            """
            win.destroy()
            MenuPrincipal.MP()

            
        def yes(self=0):
            """
                Fonction lancée quand on gagne/perd : si il est invoqué sans paramètre c'est la victoire,
                dans le cas contraire c'est la défaite.
                Affiche ensuite une messagebox pour demander à l'utilisateur si il veut arrêter ou continuer. 
            """
            if(self!=0):
                yesno= mb.askyesno("Perdu ...", "Recommencer ?")          
                

            else:
                yesno= mb.askyesno("Félicitations !!!!", "Le pays etait bien {} !\nRecommencer ?".format(pays.upper()))
            
            if(yesno):
                start()

                
            else:
                launch_MP()


            
        def checkMot(inp, choix):
            """
                Fonction qui regarde si la lettre ou le mot entré est dans ou est le mot a chercher
            """
            global nb_chance
            found= False
            for i in range(len(histo)):        
                if (inp==histo[i]):
                          find[i]=1
                          mb.showinfo("Jeu du pendu", "Vous avez déjà rentré cette lettre")
                          found=True
                          ent_inp.delete(0, END)
                          return

            histo.append(inp)
            if(choix==-1): #l'utilisateur entre une lettre
                for i in range(len(pays)):
                    
                    if (inp==pays[i]):
                        find[i]=1                
                        mb.showinfo("Jeu du pendu", "Bonne réponse")
                        found=True
                    
                if( not found):
                    nb_chance-=1
                    mb.showwarning("Mauvaise Réponse", "La lettre que vous avez entré est fausse"+'\n'+
                                   'Il vous reste {} chance(s)'.format(nb_chance))

                            
                
                    
                updateMot()
                
            

            elif(choix==1): #mot entier
                if(inp==pays):
                    yes()
                    return True
                
                if(inp!=pays):
                    nb_chance-=1
                    mb.showwarning("Mauvaise Réponse", "La lettre que vous avez entré est fausse"+'\n'+
                                   'Il vous reste {} chance(s)'.format(nb_chance))
                    

            


            if(nb_chance==0):
               yes(1)

            return False  

        def updateMot(self=0):
            """
                Fonction qui actualise l'affichage du mot sur l'écran
            """
            global labels
            
            l=0

            for i in labels:
                i.destroy()
                
            labels=[]
            
            

            for i in range(len(pays)):
                labels.append(Label(f_show, text=(pays[i] if find[i]==1 else '_')))
                labels[i].grid(row=0, column= l, padx=5, pady=2, sticky= NSEW)
                l+=1

            if (find[0: len(labels)]==[1 for i in range(len(labels))]):
                yes()
            
            

            
        def getInput(self=0):
            """
                Renvoie le contenu de ent_inp si il y a
            """
            global ent_inp, pays
            
            inp= ent_inp.get().lower()

            if(b_sel.get()>0 ): #Si on selectionne un Mot entier
                pass

            else: #Si on selectionne une lettre
                pass

            
            #######Warnings######    
            if(len(inp) ==0):
                mb.showinfo("Attention !", "Vous devez entrer "+('un mot' if b_sel.get()>0 else 'une lettre')+" dans le champ ! ")
                return

            elif (b_sel.get()==1 and len(inp)!=len(pays)):
                mb.showinfo("Attention !", "Votre mot n'est pas de la bonne longueur")
                return

            elif(b_sel.get()==-1 and len(inp)!=1):
                mb.showinfo("Attention !", "Vous ne devez entrer qu'une seule lettre")
                return
            ####################
            
            else:
                state= checkMot(inp, b_sel.get())
                if(state==False):
                    ent_inp.delete(0, END)
                
                return


        def ranPays(self=0):
            """
                Prend un pays au hasard dans "pays.txt"
            """
            global pays, find, labels
            pays= [ mot[0:len(mot)-1].lower() for mot in open("pays.txt", "r")]

            pays= pays[randint(0, len(pays)-1)]

            find=[0 for i in range (len(pays))]

            updateMot()

            


        def start():
            """
                Lance le jeu
            """
            global nb_chance, histo
            ent_inp.delete(0, END)
            nb_chance=7
            for i in labels:
                i.destroy()
            histo= []    
            ranPays()



        def regle(event=0):
            """
                Fonction activée lors d'un clic sur le clic droit. Affiche les réègles du jeu. 
            """
            mb.showinfo("Règles du jeu", "Les règles du jeu sont simples."+"\n"+"\n"+ "Vous devez trouver le mot caché en donnant des lettres ou mot entier."+"\n"+"\n"+
                        "MAIS ATTENTION. Si vous donnez une lettre fausse ou un mot faux, vous aurez une chance en moins."+"\n"+"\n"+
                        "La partie s'arrête si vous trouvez le mot ou que vous avez épuisé toutes vos tentatives"+"\n"+"\n"+
                        "Bonne chance.")
        #######################################

        ##############BINDS####################
        win.bind("<Return>", getInput)
        win.bind("<Button-3>", regle)
        win.bind("<Escape>", launch_MP)
        #######################################
        
        
        ############INTERFACE####################
        ##FRAME SHOW###
        f_show= Frame(win)
        f_show.grid(row= 0, column=0, sticky= NSEW)

        ###############




        ##FRAME INPUT
        f_i= Frame(win)
        f_i.grid(row= 1, column=2)

        ent_inp= ttk.Entry(f_i)
        ent_inp.grid(row= 0, column=2, columnspan=2)

        Label(f_i, text='Voulez-vous donner une lettre ou un mot entier ?').grid(row=1, column=2, columnspan=2)

        b_sel= IntVar()

        b_sel.set(-1) #selection de lettre par défaut

        b_l= Radiobutton(f_i, text= 'Lettre', variable= b_sel, value= -1) #bouton selection lettre
        b_l.grid(row= 2, column=2)

        b_m= Radiobutton(f_i, text='Mot entier', variable= b_sel, value= 1) #bouton selection mot
        b_m.grid(row= 2, column= 3)


        ttk.Button(win, text= "Revenir au Menu Principal", command= launch_MP).grid(row=0, column=10)


        ##############

        #######################################

        start()

        label=Label(win, text="Pour des raisons de problème de caractères, certains pays sont écris en anglais")
        label.grid(row=4, column=2, columnspan=2)

        welcome=Label(win, text="Bienvenue sur le jeu du Pendu", font='Arial 14')
        welcome.grid(row=5, column=2, pady=20)

        rule=Label(win, text="Pour vous rappeler des règles, faites un clique droit", font='Arial 14')
        rule.grid(row=6, column=2)


        

        win.mainloop()





            
